Project Summary: CyberGirls Assessment 2 - Flask API Development and Deployment
Overview

This project serves as a comprehensive guide for the CyberGirls Assessment 2, detailing the process of developing, containerizing, and deploying a Flask API. It emphasizes the importance of security measures and the implementation of a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions to streamline the development workflow.

Objectives

    . Develop a Flask API capable of handling user requests.
    . Containerize the API using Docker for easier deployment and management.
    . Deploy the containerized application to a Kubernetes cluster using KinD (Kubernetes in Docker).
    . Implement a CI/CD pipeline using GitHub Actions to automate the build and deployment processes.
    . Ensure the security of the API through best practices in Kubernetes.

Steps Taken to Complete the Project
1. Fork and clone the Flask App Repository
    Clone the existing Flask application from GitHub to your account for further development.

2. Install Docker and KinD
   Follow the official guides to install Docker and KinD on your local machine, setting the stage for containerization and Kubernetes deployment.

3. Containerization Process 
  The API was containerized using Docker to ensure a consistent and reproducible deployment environment across various platforms. The containerization process involved the following steps:

1. **Creating the Dockerfile**: Defines the application environment, including dependencies and runtime configurations.
2. **Building the Docker Image**: The Docker image is built using the following key elements:
   - **Base Image**: Utilizes the official Python image for a lightweight and secure environment.
   - **Dependency Installation**: All necessary Python packages are installed from the `requirements.txt` file.
   - **Copying Application Code**: The Flask application code and necessary files are copied into the container.
   - **Exposing Ports**: The container exposes the necessary ports to allow communication with the application.
   - **Setting the Entry Point**: Specifies the command to run the application when the container starts.
#Check the dockerfile
    
4. CI/CD Process

This project employs a CI/CD pipeline using GitHub Actions to automate the build, test, and deployment process. The CI/CD workflow consists of the following steps:

    Build Stage:
       1. The code is checked out from the repository.
       2. Docker Buildx is set up for building multi-platform images.
       3. Docker Login: Authenticates with Docker Hub using credentials stored in GitHub Secrets.
       4.The Docker image is built and pushed to Docker Hub, making it available for deployment.

    Deploy Stage:
        1.After a successful build, the workflow sets up kubectl and creates a local kind Kubernetes cluster.
        2.The KUBECONFIG is configured to access the kind cluster.
        3.Kubernetes manifests are applied to deploy the API and related services.

GitHub Actions Workflow
#See the full CI/CD configuration in .github/workflows/ci-cd.yaml

5. Kubernetes Deployment

The API is deployed to a local kind cluster using the Kubernetes manifests located in the k8s directory. The deployment process involves:

    Deployment: Defines how the API pods are managed, including the number of replicas and container specifications.

    # See the full deployment manifest in the deployment.yaml file

    Service: Exposes the API to allow external access via a NodePort or LoadBalancer.

    # See the  full service manifest in the service.yaml file

6. Security measures implemented
    The project incorporates several security measures to safeguard the API and its data:
    1. Sensitive information such as secret keys are managed through environment variables and stored securely in GitHub Secrets.
    2. HTTPS Support: The app is now configured to run over HTTPS using the specified certificate files (cert.pem and key.pem). This encrypts the data in transit.
    3. Secure Cookies: Cookies are set with the Secure and HttpOnly flags to enhance cookie security.
    4. Error Handling: Custom error handlers for 404 and 500 errors are included to provide meaningful error messages.
    5. Rate Limiting: The Flask-Limiter library is utilized to limit the /how-are-you endpoint to 5 requests per minute to prevent abuse.

