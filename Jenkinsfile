pipeline {
    agent any

    triggers {
        // Automatically check for new GitHub commits every 2 minutes
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ChristianAlAlam/Csc-263-Movie-Assignment-.git'
            }
        }

        stage('Build in Minikube Docker') {
            steps {
                bat '''
                echo === Switch Docker to Minikube environment ===
                call minikube docker-env --shell=cmd > docker_env.bat
                call docker_env.bat

                echo === Build Django image inside Minikube ===
                docker build -t website:latest .
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                echo === Deploy to Kubernetes ===
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                kubectl rollout status deployment/website-deployment
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                bat '''
                kubectl get pods -o wide
                kubectl get svc
                '''
            }
        }
    }
}
