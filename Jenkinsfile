pipeline {
  agent any

  triggers {
    // Check GitHub every 2 minutes for new commits
    pollSCM('H/2 * * * *')
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/ChristianAlAlam/Csc-263-Movie-Assignment-'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat '''
        REM Configure Minikube Docker environment
        call minikube docker-env --shell=cmd > docker_env.bat
        call docker_env.bat

        REM Build Django website image inside Minikube
        docker build -t website:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml
        kubectl rollout status deployment/website-deployment
        '''
      }
    }
  }
}
