from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="doctor") # doctor, admin, patient
    is_active = Column(Boolean, default=True)
    full_name = Column(String, default="Dr. Sarah Jenkins")
    department = Column(String, default="Ophthalmology")

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(DateTime)
    gender = Column(String)
    hospital_id = Column(Integer, ForeignKey("hospitals.id"), nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    medical_history = Column(Text, nullable=True)
    medications = Column(Text, nullable=True)
    
    scans = relationship("Scan", back_populates="patient", cascade="all, delete-orphan")
    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete-orphan")

class Hospital(Base):
    __tablename__ = "hospitals"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)

class Scan(Base):
    __tablename__ = "scans"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    original_image_path = Column(String)
    optic_disc_path = Column(String, nullable=True)
    optic_cup_path = Column(String, nullable=True)
    vessel_seg_path = Column(String, nullable=True)
    cdr_estimation = Column(Float, nullable=True)
    
    patient = relationship("Patient", back_populates="scans")
    prediction = relationship("Prediction", back_populates="scan", uselist=False, cascade="all, delete-orphan")

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    scan_id = Column(Integer, ForeignKey("scans.id"))
    prediction_score = Column(Float)
    risk_level = Column(String)
    estimated_cdr = Column(Float)
    confidence = Column(Float)
    heatmap_path = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    scan = relationship("Scan", back_populates="prediction")
    reports = relationship("Report", back_populates="prediction", cascade="all, delete-orphan")

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"))
    status = Column(String, default="Pending") # Pending, Approved, Rejected
    notes = Column(Text, nullable=True)
    doctor_notes = Column(Text, nullable=True)
    digital_signature = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    prediction = relationship("Prediction", back_populates="reports")

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime)
    status = Column(String, default="Scheduled") # Scheduled, Completed, Cancelled
    
    patient = relationship("Patient", back_populates="appointments")

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String)
    action = Column(String)
    details = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
