# US Visa Approval Prediction System

## An end-to-end Machine Learning system that predicts US Visa approval outcomes and is fully productionized with MLOps best practices, CI/CD automation and AWS cloud deployment.

---

## Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [CI/CD Workflow](#-cicd-workflow)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [API Usage](#-api-usage)

---

## Overview

This project predicts whether a US visa application will be **Approved or Denied** based on structured applicant and case-level features.

Beyond the ML model, it demonstrates a **production-grade MLOps pipeline**:

| Capability | Tool |
|---|---|
| Model Training & Evaluation | Scikit-learn |
| REST API | FastAPI |
| Containerization | Docker |
| CI/CD Automation | GitHub Actions |
| Cloud Deployment | AWS EC2 + ECR + S3 |

---

## Problem Statement

US visa approval decisions hinge on a combination of factors that are often opaque. This system leverages historical data to make **data-driven predictions** based on:

- Applicant profile & background
- Employer details & credibility
- Prevailing wage & job information
- Case status history

---

## Architecture

┌──────────────┐
  User Request ────▶│  FastAPI App  │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   ML Model   │◀──── Model Artifacts (AWS S3)
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │Docker Container│
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  AWS EC2     │◀──── Image Pull (AWS ECR)
                    └──────────────┘


---

## Tech Stack

**Machine Learning**
`Python` `Scikit-learn` `Pandas` `NumPy`

**Backend & API**
`FastAPI` `Uvicorn`

**MLOps & Infrastructure**
`Docker` `GitHub Actions` `AWS EC2` `AWS ECR` `AWS S3` `MongoDB`

---

## Project Structure

US_Visa/
│
├── components/             # Data ingestion, transformation, model training
├── pipeline/               # Training & prediction pipeline orchestration
├── entity/                 # Config entities & data schema classes
├── Cloud_Storage/          # AWS S3 read/write interaction
├── app.py                  # FastAPI entry point
├── Dockerfile              # Container build instructions
├── requirements.txt        # Python dependencies
└── .github/
└── workflows/          # GitHub Actions CI/CD pipeline

---

## CI/CD Workflow
Push to main
│
▼
GitHub Actions Triggered
│
├──▶ Build Docker Image
│
├──▶ Push Image to AWS ECR
│
└──▶ EC2 Pulls Latest Image & Restarts Container

Every push to `main` triggers a fully automated build → push → deploy cycle with **zero manual intervention**.

---

## Getting Started

### Prerequisites
- Python 3.8+
- Docker
- AWS account with configured IAM credentials
- MongoDB connection URI

### 1. Clone the Repository

```bash
git clone https://github.com/banerjee-sarnab/US_Visa_Approval_Prediction.git
cd US_Visa_Approval_Prediction
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=your_region
export MONGODB_URL=your_mongo_uri
```

### 5. Run the Application

```bash
python app.py
```

API will be live at `http://localhost:8080`

---

## Environment Variables

| Variable | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | AWS IAM access key |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM secret key |
| `AWS_DEFAULT_REGION` | AWS region (e.g. `us-east-1`) |
| `MONGODB_URL` | MongoDB connection string |

---

