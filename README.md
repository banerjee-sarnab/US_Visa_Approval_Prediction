# US Visa Approval Prediction System

An end-to-end Machine Learning project that predicts the approval status of US visa applications using structured data. The project is fully productionized with CI/CD, Docker, AWS deployment, and real-time inference.

---

## Overview

This project builds a predictive model to classify whether a US visa application will be **Approved or Denied** based on applicant and case-related features.

It also demonstrates a complete MLOps pipeline:

- Model training & evaluation
- API deployment
- Docker containerization
- CI/CD using GitHub Actions
- Cloud deployment on AWS (ECR + EC2)

---

## Problem Statement

Visa approval decisions depend on multiple factors such as:

- Applicant profile
- Employer details
- Wage and job information
- Case Status history

---

## Project Architecture

```
User → Web/API → Docker Container → ML Model
                        ↓
                  AWS EC2 Instance
                        ↓
              Model artifacts (AWS S3)
```

---

## Tech Stack

### 🔹 Machine Learning

- Python
- Scikit-learn
- Pandas, NumPy

### 🔹 Backend & API

- FastAPI

### 🔹 MLOps & Deployment

- Docker
- GitHub Actions (CI/CD)
- AWS EC2 (hosting)
- AWS ECR (container registry)
- AWS S3 (model storage)

---

## Features

- ✅ End-to-end ML pipeline (training → prediction)
- ✅ Modular code structure
- ✅ Dockerized application
- ✅ CI/CD pipeline for automated deployment
- ✅ Cloud-based model serving
- ✅ Real-time predictions via API

---

## Project Structure

```
US_Visa/
│
├── components/            # Data ingestion, transformation, training
├── pipeline/              # Training & prediction pipelines
├── entity/                # Config & data classes
├── Cloud_Storage/         # AWS S3 interaction
├── app.py                 # API entry point
├── requirements.txt
├── Dockerfile
└── .github/workflows/     # CI/CD pipeline
```

---

## CI/CD Workflow

1. Push code to `main` branch
2. GitHub Actions:
   - Builds Docker image
   - Pushes image to AWS ECR

3. EC2 instance pulls latest image
4. Container runs automatically

---

## Deployment

The application is deployed on AWS EC2 and exposed via:

```
http://3.235.99.186:8080/
```

---

## Environment Variables

Set the following variables:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `MONGODB_URL`

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/banerjee-sarnab/US_Visa_Approval_Prediction.git
cd US_Visa_Approval_Prediction
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```
