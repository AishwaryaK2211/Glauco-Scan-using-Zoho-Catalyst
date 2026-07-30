import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

IMG_SIZE = 224

def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    # First, we create a model that maps the input image to the activations
    # of the last conv layer as well as the output predictions
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )

    # Then, we compute the gradient of the top predicted class for our input image
    # with respect to the activations of the last conv layer
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    # This is the gradient of the output neuron (top predicted or chosen)
    # with regard to the output feature map of the last conv layer
    grads = tape.gradient(class_channel, last_conv_layer_output)

    # This is a vector where each entry is the mean intensity of the gradient
    # over a specific feature map channel
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    # We multiply each channel in the feature map array
    # by "how important this channel is" with regard to the top predicted class
    # then sum all the channels to obtain the heatmap class activation
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    # For visualization purpose, we will also normalize the heatmap between 0 & 1
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

def save_and_display_gradcam(img_path, heatmap, cam_path="cam.jpg", alpha=0.4):
    # Load the original image
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"Image not found at {img_path}")
        
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

    # Rescale heatmap to a range 0-255
    heatmap = np.uint8(255 * heatmap)

    # Resize heatmap to match original/resized image dimensions
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))

    # Use jet colormap to colorize heatmap
    jet = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    
    # Superimpose the heatmap on original image
    superimposed_img = cv2.addWeighted(jet, alpha, img, 1 - alpha, 0)

    # Save the superimposed image
    cv2.imwrite(cam_path, superimposed_img)
    return superimposed_img

class GlaucomaModel:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        # EfficientNetB0's last conv layer is typically 'top_conv'
        self.last_conv_layer_name = 'top_conv'
        
    def preprocess_image(self, img_path):
        img = cv2.imread(img_path)
        if img is None:
            raise ValueError(f"Image not found at {img_path}")
            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # CLAHE
        lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv2.merge((cl,a,b))
        img_clahe = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)
        
        img_resized = cv2.resize(img_clahe, (IMG_SIZE, IMG_SIZE))
        
        # Normalize and expand dims
        img_array = np.array(img_resized, dtype=np.float32) / 255.0
        return np.expand_dims(img_array, axis=0)

    def predict_with_explanation(self, img_path, output_heatmap_path="output_heatmap.jpg"):
        img_array = self.preprocess_image(img_path)
        
        # Predict
        prediction = self.model.predict(img_array)[0][0]
        risk_level = "High Risk" if prediction > 0.5 else "Low Risk"
        
        # Generate Grad-CAM
        heatmap = make_gradcam_heatmap(img_array, self.model, self.last_conv_layer_name)
        
        # Save visualization
        save_and_display_gradcam(img_path, heatmap, cam_path=output_heatmap_path)
        
        return {
            "prediction_score": float(prediction),
            "risk_level": risk_level,
            "heatmap_path": output_heatmap_path
        }

if __name__ == '__main__':
    # Test script if run directly
    print("Inference script ready. Usage: instantiate GlaucomaModel and call predict_with_explanation.")
