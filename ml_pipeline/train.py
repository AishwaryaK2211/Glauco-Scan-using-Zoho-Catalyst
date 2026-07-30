import os
import cv2
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split

print("TensorFlow Version:", tf.__version__)

DATA_DIR = r"d:/Glauco-scan/G1020/Images"
CSV_PATH = r"d:/Glauco-scan/G1020/G1020.csv"
MODEL_SAVE_PATH = "glaucoscan_model.h5"
IMG_SIZE = 224
BATCH_SIZE = 8
EPOCHS = 10  # Low for prototype

def load_data(max_samples=100):
    df = pd.read_csv(CSV_PATH)
    # Take first 100 samples for prototype
    df = df.head(max_samples)
    
    images = []
    labels = []
    
    print(f"Loading {len(df)} images...")
    for index, row in df.iterrows():
        img_name = row['imageID']
        label = row['binaryLabels']
        
        img_path = os.path.join(DATA_DIR, img_name)
        if not os.path.exists(img_path):
            print(f"Image not found: {img_path}")
            continue
            
        # Read and preprocess image
        img = cv2.imread(img_path)
        if img is None:
            continue
            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Optional: Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
        # We apply it on the L channel of LAB color space
        lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv2.merge((cl,a,b))
        img_clahe = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)
        
        img_resized = cv2.resize(img_clahe, (IMG_SIZE, IMG_SIZE))
        
        images.append(img_resized)
        labels.append(label)
        
    X = np.array(images, dtype=np.float32) / 255.0  # Normalize to [0, 1]
    y = np.array(labels, dtype=np.float32)
    return X, y

def build_model():
    base_model = EfficientNetB0(
        input_shape=(IMG_SIZE, IMG_SIZE, 3),
        include_top=False,
        weights='imagenet'
    )
    
    # Freeze base model
    base_model.trainable = False
    
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.5)(x)
    predictions = Dense(1, activation='sigmoid')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    
    model.compile(
        optimizer=Adam(learning_rate=1e-3),
        loss='binary_crossentropy',
        metrics=['accuracy', tf.keras.metrics.AUC(name='auc')]
    )
    return model

def main():
    X, y = load_data(max_samples=100)
    print(f"Dataset shape: X={X.shape}, y={y.shape}")
    
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    model = build_model()
    
    callbacks = [
        EarlyStopping(patience=3, monitor='val_loss', restore_best_weights=True),
        ModelCheckpoint(MODEL_SAVE_PATH, save_best_only=True, monitor='val_auc', mode='max')
    ]
    
    print("Starting training...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        callbacks=callbacks
    )
    
    print(f"Model saved to {MODEL_SAVE_PATH}")
    
if __name__ == '__main__':
    main()
