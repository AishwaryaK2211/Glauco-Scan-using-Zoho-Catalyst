# GlaucoScan — Zoho Catalyst Deployment-Ready Branch 🚀👁️

> **Lightweight, Cloud-Optimized Build for Serverless Zoho Catalyst Deployment**
> 
> *This branch (`catalyst-deploy`) contains a production-ready, lightweight configuration designed to stay well below Zoho Catalyst upload size limits (preventing Exit Code 137 memory / package size failures).*

---

[![Zoho Catalyst](https://img.shields.io/badge/Deploy-Zoho%20Catalyst-C8102E?style=for-the-badge&logo=zoho)](https://www.zoho.com/catalyst/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Frontend-Next.js%2015-000000?style=for-the-badge&logo=nextdotjs)](https://nextjs.org/)
[![Branch](https://img.shields.io/badge/Branch-catalyst--deploy-2EA44F?style=for-the-badge&logo=git)](https://github.com/AishwaryaK2211/Glauco-Scan-using-Zoho-Catalyst/tree/catalyst-deploy)

---

## 🌿 Branch Differences

| Feature / Artifact | `main` Branch | `catalyst-deploy` Branch |
|--------------------|---------------|--------------------------|
| **Primary Focus** | Complete repository & datasets | Serverless Zoho Catalyst Cloud Deployment |
| **Retinal Datasets** | Full dataset images included | Externalized (Fetched via Catalyst File Store) |
| **Package Size** | ~1.5 GB | **< 30 MB** (Deployment-optimized) |
| **Model & Weights** | Complete (`glaucoscan_model.h5`) | Kept intact for runtime inference |
| **Source Code & UI** | Full Next.js + FastAPI | Full Next.js + FastAPI |
| **Catalyst Config** | Base config | Pre-configured `catalyst.json` & Functions |

---

## ☁️ Zoho Catalyst Deployment Steps

### 1. Connect Repository to Zoho Catalyst
1. Log in to your [Zoho Catalyst Console](https://catalyst.zoho.com/).
2. Create a new **App** (e.g., `GlaucoScan-Intelligence`).
3. Under **App Logic / Functions & Web Client**, select **GitHub Integration**.
4. Choose repository: `AishwaryaK2211/Glauco-Scan-using-Zoho-Catalyst`.
5. Select branch: **`catalyst-deploy`**.

### 2. Configure Build & Install Commands
- **Frontend Web Client**:
  - Build Command: `npm run build`
  - Output Directory: `.next` (or `out`)
- **Backend Microservices / Functions**:
  - Runtime: `Python 3.10`
  - Entrypoint: `backend/functions/glaucoscan_api/main.py`

### 3. External File Store Setup
Large fundus datasets are served dynamically via **Zoho Catalyst File Store**:
- Create a bucket named `glaucoscan-retinal-scans` in Catalyst File Store.
- Set environment variable: `CATALYST_FILESTORE_URL=https://catalyst.zoho.com/filestore/v1/...`

---

## 💻 Local Setup & Testing

```bash
# Clone the deployment branch
git clone -b catalyst-deploy https://github.com/AishwaryaK2211/Glauco-Scan-using-Zoho-Catalyst.git
cd Glauco-Scan-using-Zoho-Catalyst

# Install frontend dependencies
cd frontend
npm install
npm run dev

# Install backend dependencies
cd ../backend_fastapi
pip install -r requirements.txt
uvicorn app.main:app --port 8000
```

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
