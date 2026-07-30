@echo off
echo Starting GlaucoScan Full Stack (Independent Architecture)...

:: Start the FastAPI Backend in a new window
start cmd /k "cd backend_fastapi && ..\venv\Scripts\activate.bat && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

:: Start the Next.js Frontend in a new window
start cmd /k "cd frontend && npm run dev"

echo Both services are booting up!
echo The frontend will be available at http://localhost:3000
echo The FastAPI backend is running at http://localhost:8000
