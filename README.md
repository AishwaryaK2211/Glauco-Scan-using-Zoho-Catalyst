# GlaucoScan — Vision Intelligence Platform 👁️✨

> **Enterprise-Grade AI-Powered Ophthalmology & Glaucoma Screening Platform**
> 
> *Precision Retinal Analytics, EfficientNet-B0 Deep Learning, Grad-CAM Explainability & Gemini Medical RAG Assistant for Modern Clinical Diagnostics.*

---

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Frontend-Next.js%2015-000000?style=for-the-badge&logo=nextdotjs)](https://nextjs.org/)
[![TensorFlow](https://img.shields.io/badge/AI-TensorFlow%20%2F%20Keras-FF6F00?style=for-the-badge&logo=tensorflow)](https://tensorflow.org/)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python)](https://python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=for-the-badge&logo=typescript)](https://typescriptlang.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite%20%2F%20SQLAlchemy-003B57?style=for-the-badge&logo=sqlite)](https://sqlite.org/)
[![Zoho Catalyst Ready](https://img.shields.io/badge/Cloud-Zoho%20Catalyst%20Ready-C8102E?style=for-the-badge)](https://www.zoho.com/catalyst/)

---

## 📌 Project Overview

**GlaucoScan** is a flagship, enterprise-grade ophthalmology intelligence platform designed to enable early detection, continuous tracking, and AI-assisted diagnosis of Glaucoma using fundus retinal photography.

By integrating state-of-the-art deep learning models (**EfficientNet-B0**), explainable AI (**Grad-CAM heatmaps**), automated **Cup-to-Disc Ratio (CDR)** estimation, and Retrieval-Augmented Generation (**Gemini 2.5 Flash Medical RAG Assistant**), GlaucoScan streamlines clinical workflows for ophthalmologists, optometrists, and healthcare systems.

---

## ✨ Features

- 🎯 **Deep Learning Screening**: High-accuracy classification of retinal images into *High Risk* (Glaucoma) and *Low Risk* (Normal).
- 🔥 **Grad-CAM Explainable AI**: Visual heatmaps pinpointing optic disc and optic cup lesion areas for full transparency.
- 📐 **Automated CDR Analysis**: Quantitative optic cup-to-disc ratio estimation to assist clinical grading.
- 🤖 **Gemini Medical RAG Assistant**: Multi-turn clinical chat assistant backed by patient records and cohort analytics.
- 📋 **Doctor Review Workspace**: Dedicated queue for ophthalmologists to review, annotate, and e-sign AI-generated diagnoses.
- 📈 **Longitudinal Progression Tracking**: Historical CDR trend charts per patient to monitor disease advancement over time.
- 📊 **Executive Analytics & Telemetry**: Cohort-wide metrics, risk distribution radar charts, and real-time processing stats.
- 📄 **Automated Clinical Reports**: One-click PDF/structured diagnostic report generation.

---

## 🛠️ System Architecture

```
                               ┌──────────────────────────────────────────┐
                               │       Next.js 15 Enterprise Frontend      │
                               │        (Lodestar Medical Intelligence)   │
                               └────────────────────┬─────────────────────┘
                                                    │ REST API / JSON
                               ┌────────────────────▼─────────────────────┐
                               │           FastAPI Backend Server         │
                               └──────────┬───────────────────┬───────────┘
                                          │                   │
                     ┌────────────────────▼─────┐       ┌─────▼────────────────────┐
                     │   EfficientNet-B0 Engine  │       │  SQLite / SQLAlchemy DB  │
                     │  - Classification        │       │  - 60+ Patient Records   │
                     │  - Grad-CAM Heatmaps     │       │  - Scans & Predictions   │
                     │  - CDR Calculation       │       │  - Diagnostic Reports    │
                     └──────────────────────────┘       └──────────────────────────┘
                                                              │
                                                        ┌─────▼────────────────────┐
                                                        │  Gemini Medical RAG Chat │
                                                        │  - Context Injection     │
                                                        │  - Cohort Knowledge      │
                                                        └──────────────────────────┘
```

---

## 📂 Project Directory Structure

```
Glauco-scan/
├── G1020/                   # G1020 Clinical Dataset (Images & Annotations)
│   ├── Images/              # 1020 High-Resolution Retinal Fundus Scans
│   ├── Masks/               # Optic Disc & Cup Segmentation Masks
│   └── G1020.csv            # Ground Truth Annotations & CDR Labels
├── ODIR-5K/                 # ODIR 5K Ophthalmic Dataset
├── ORIGA/                   # ORIGA Retinal Dataset
├── REFUGE/                  # REFUGE Glaucoma Benchmark Dataset
├── backend/                 # Legacy Backend Utilities
├── backend_fastapi/         # Production FastAPI Core Server
│   ├── app/
│   │   ├── main.py          # REST Endpoints & Service Routing
│   │   ├── models.py        # SQLAlchemy Data Models
│   │   ├── database.py      # Database Connection Engine
│   │   └── schemas.py       # Pydantic Request/Response Schemas
│   └── glaucoscan.db        # Live SQLite Database (Seeded with G1020)
├── frontend/                # Next.js 15 Web Application
│   ├── src/
│   │   ├── app/             # App Router & Main Dashboard Pages
│   │   └── components/      # UI Design System & Medical Widgets
│   ├── package.json         # Node Dependencies
│   └── tailwind.config.ts   # Styling Framework Configuration
├── ml_pipeline/             # Deep Learning Model Core
│   ├── inference.py         # Prediction & Grad-CAM Pipelines
│   ├── train.py             # EfficientNet Training Scripts
│   └── preprocess.py        # Image Normalization & Cropping
├── glaucoscan_model.h5      # Trained EfficientNet-B0 Model Weights
├── preprocessed_images/     # Pre-processed Retinal Cache
├── docker-compose.yml       # Container Deployment Config
├── start_glaucoscan.bat     # Windows 1-Click Launch Script
├── run_ml.bat               # ML Execution Script
└── README.md                # System Documentation
```

---

## 📊 Modules & Interface Overview

1. **Dashboard**: High-level telemetry bar, live retinal viewer, and intelligence widgets.
2. **AI Screening**: Real-time fundus image upload, Grad-CAM visualization, and instant risk scoring.
3. **Patients Registry**: Complete electronic health records (EHR) connected to real G1020 clinical data.
4. **Doctor Workspace**: Triage queue for high-risk patients requiring specialist validation and e-signature.
5. **Retinal Intelligence**: Detailed anatomical inspection with optic disc/cup contour analysis.
6. **Disease Progression**: Multi-visit CDR tracking curves to spot gradual glaucomatous changes.
7. **Analytics**: System-wide performance metrics, accuracy breakdown, and cohort demographics.
8. **Diagnostic Reports**: Generated formal clinical summaries ready for EHR export.
9. **AI Assistant**: RAG-powered medical assistant utilizing Gemini 2.5 Flash.
10. **Settings**: Engine configurations, risk threshold tuning, and database status.

---

## ⚡ Quick Start & Execution

### Prerequisites
- Python 3.10+
- Node.js 18+
- Git

### 1. Backend Setup (FastAPI)
```bash
# Navigate to backend
cd backend_fastapi

# Install Python dependencies
pip install -r requirements.txt

# Start the API server
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 2. Frontend Setup (Next.js)
```bash
# Navigate to frontend
cd frontend

# Install Node packages
npm install

# Run development server
npm run dev
```

Open `http://localhost:3000/dashboard` in your browser.

---

## 🚀 Future Zoho Catalyst Cloud Integration

GlaucoScan is architected specifically for serverless deployment on **Zoho Catalyst**:

- **App Server**: Hosting Next.js 15 Frontend via Catalyst Web Client / App Logic.
- **Advanced I/O & Functions**: Deploying FastAPI REST endpoints as Catalyst Python Microservices.
- **Data Store**: Migration from SQLite to Catalyst Relational Database (Data Store).
- **File Store**: Storing raw and pre-processed fundus images in Catalyst File Store.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍⚕️ Author & Credits

Developed with ❤️ by **Aishwarya K** & Team for modern clinical AI diagnostics.
