# Lab 02: Azure Kubernetes Service Deployment and Management

## Objective

Understand Kubernetes basics, deploy multi-container applications, use Helm, and manage Kubernetes resources using Minikube.

## Tools Used

- Docker
- Minikube
- kubectl
- Helm
- Kubernetes YAML manifests

## Folder Structure

```text
manifests/
helm/
scripts/
screenshots/

Tasks Performed
Verified Docker, kubectl, Minikube, and Helm
Started local Kubernetes cluster using Minikube
Created namespace webapp-demo
Deployed backend application
Deployed frontend application
Exposed frontend using NodePort
Tested application using Minikube IP
Installed Nginx using Helm
Created custom Helm chart
Scaled backend deployment
Upgraded Helm release
Practiced troubleshooting commands
Created deployment and cleanup scripts
Important Commands
minikube start --driver=docker
kubectl get all -n webapp-demo
helm list -n webapp-demo
kubectl logs -n webapp-demo -l app=frontend
kubectl describe pod -n webapp-demo -l app=frontend
Conclusion

This lab demonstrated Kubernetes deployment and management using Minikube. It also introduced Helm for application packaging and lifecycle management.
