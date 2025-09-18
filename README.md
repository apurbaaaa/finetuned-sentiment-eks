````markdown
# Finetuned Sentiment Analysis on AWS EKS 🚀

This project demonstrates the complete workflow of training, containerizing, and deploying a **finetuned BERT-based sentiment analysis model** as a REST API using **FastAPI, Docker, and Amazon EKS (Elastic Kubernetes Service)**.

---

## 📌 Features
- Fine-tunes `distilbert-base-uncased` on IMDB sentiment dataset.
- Exposes predictions via a FastAPI `/predict` endpoint.
- Packaged into a lightweight Docker image.
- Deployed on **AWS EKS** with a LoadBalancer Service for public access.
- End-to-end MLOps-style pipeline: training → containerization → cloud deployment.

---

## 🏗️ Architecture
```text
Fine-tuned BERT Model (DistilBERT)
           │
           ▼
    FastAPI App (app.py) → REST API /predict
           │
           ▼
   Docker Image → Pushed to Docker Hub
           │
           ▼
 AWS EKS Cluster (2 × t3.medium worker nodes)
           │
           ▼
Kubernetes Deployment + Service (LoadBalancer)
           │
           ▼
Public Endpoint (Elastic Load Balancer)
    → Accessible via curl or client apps
````

---

## ⚙️ How to Run Locally

### 1. Clone repository

```bash
git clone https://github.com/<your-username>/finetuned-sentiment-eks.git
cd finetuned-sentiment-eks
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train model (optional)

```bash
python train.py
```

* This fine-tunes the model and saves it into `./sentiment_model/`.

### 5. Run locally with FastAPI

```bash
uvicorn app:app --reload
```

### 6. Test the API

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text":"This project works perfectly"}'
```

---

## 🐳 Docker Build and Run

### 1. Build Docker image

```bash
docker build -t sentiment-api .
```

### 2. Run container

```bash
docker run -p 8080:8080 sentiment-api
```

### 3. Test

```bash
curl -X POST "http://127.0.0.1:8080/predict" \
     -H "Content-Type: application/json" \
     -d '{"text":"Docker container is running fine"}'
```

---

## ☁️ Deploy on AWS EKS

### 1. Push Docker image to Docker Hub

```bash
docker buildx build --platform linux/amd64 -t <your-dockerhub-username>/sentiment-api:latest . --push
```

### 2. Create EKS cluster (via eksctl)

```bash
eksctl create cluster \
  --name sentiment-cluster \
  --region ap-south-1 \
  --nodegroup-name worker-nodes \
  --node-type t3.medium \
  --nodes 2
```

### 3. Deploy app on EKS

```bash
kubectl apply -f deployment.yaml
kubectl get pods
kubectl get svc sentiment-api-service
```

### 4. Access the API

```bash
curl -X POST "http://<EXTERNAL-IP>/predict" \
     -H "Content-Type: application/json" \
     -d '{"text":"EKS deployment is successful and running"}'
```

---

## 📂 Repository Structure

```
.
├── app.py             # FastAPI app serving predictions
├── train.py           # Fine-tuning script
├── test_model.py      # Local test script
├── requirements.txt   # Python dependencies (CPU-only PyTorch)
├── Dockerfile         # Container definition
├── .dockerignore
├── .gitignore
├── deployment.yaml    # Kubernetes Deployment + Service
└── README.md
```

---

## 🧹 Cleanup

To avoid AWS charges after demo:

```bash
kubectl delete -f deployment.yaml
eksctl delete cluster --name sentiment-cluster --region ap-south-1
```

---

## 📸 Suggested Screenshots (for report/demo)

* EKS Cluster in AWS Console
* EC2 worker nodes (t3.medium)
* LoadBalancer in EC2 → Load Balancers
* Terminal `kubectl get pods` showing pod is running
* Successful `curl` request with sentiment output

---

## ✨ Credits

* Hugging Face Transformers
* FastAPI
* Amazon EKS
* IMDB Dataset

