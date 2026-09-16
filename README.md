# Project 2 – Docker, Kubernetes & Monitoring

A Python Flask application containerized with Docker and deployed on a local Kubernetes cluster with monitoring, centralized logging, and CI/CD using GitHub Actions and Docker Hub.

## Architecture

```text
Developer
   |
   | git push
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   | build & push
   v
Docker Hub
   |
   | image
   v
Kubernetes
   |
   +----------------------+
   |                      |
   v                      v
project2-app          Monitoring
2 replicas            Prometheus
   |                  Grafana
   |                  Alertmanager
   |
   v
Fluent Bit
   |
   v
Loki
   |
   v
Grafana
Technologies Used
Python / Flask
Docker
Kubernetes
Git & GitHub
GitHub Actions
Docker Hub
Prometheus
Grafana
Fluent Bit
Loki
MinIO
Project Structure
project2-docker-kubernetes/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── monitoring/
│   └── ...
│
├── logging/
│   └── ...
│
└── .github/
    └── workflows/
        └── docker-build.yml

Update the folder names above if your actual project structure is different.

Application

The project contains a simple Python API.

API endpoint:

/api

Example response:

{
  "message": "Hello from the API!"
}

The application runs as two Kubernetes replicas for basic availability.

Docker

The application is packaged into a Docker image:

mayuri898/project2-app:latest

The image is stored in Docker Hub.

Docker Hub repository:

mayuri898/project2-app
Kubernetes

The application is deployed using Kubernetes.

The Deployment runs two replicas:

project2-app
├── Pod 1
└── Pod 2

A Kubernetes Service provides stable access to the application.

The deployment was verified using:

kubectl get pods
kubectl rollout status deployment/project2-app
Monitoring

Prometheus collects Kubernetes and application-related metrics.

Grafana is used to visualize the metrics.

The monitoring stack includes:

Prometheus
Grafana
Alertmanager
kube-state-metrics
Node Exporter
Centralized Logging

Fluent Bit collects Kubernetes container logs and sends them to Loki.

The logging flow is:

Application
    ↓
Container logs
    ↓
Fluent Bit
    ↓
Loki
    ↓
Grafana Explore

Logs can be queried in Grafana using Loki.

Example query:

{namespace="default"}
CI/CD

GitHub Actions is used to automate the Docker image build and push process.

Current workflow:

git push
   ↓
GitHub Actions
   ↓
Docker build
   ↓
Docker Hub login
   ↓
Push image

Workflow file:

.github/workflows/docker-build.yml

The image is pushed as:

mayuri898/project2-app:latest
Verification

The project was tested successfully with:

kubectl get pods

Application Pods:

project2-app-...   1/1   Running
project2-app-...   1/1   Running

The application API was also tested:

curl http://localhost:8081/api

Response:

{"message": "Hello from the API!"}

Logs were verified in Grafana through Loki.

Key Learning

This project demonstrates:

Containerizing a Python application with Docker
Deploying containers with Kubernetes
Running multiple replicas
Using Kubernetes Services
Monitoring workloads with Prometheus and Grafana
Centralizing logs with Fluent Bit and Loki
Building Docker images through GitHub Actions
Publishing Docker images to Docker Hub
Managing a complete local DevOps workflow
Future Improvements
Automatically deploy new images to Kubernetes
Add readiness and liveness probes
Add Kubernetes resource requests and limits
Use ConfigMaps and Secrets
Add application-specific Prometheus metrics
Add automated testing to GitHub Actions
Deploy the same architecture to a cloud Kubernetes cluster

Save the file.

Then run:

```bash
git add README.md
git commit -m "Add project documentation"
git push