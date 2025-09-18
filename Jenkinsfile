pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'fastapi-app:latest'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building FastAPI Docker image...'
                sh 'docker build -t $DOCKER_IMAGE backend/'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'docker run --rm $DOCKER_IMAGE pytest'
            }
        }
        stage('Run') {
            steps {
                echo 'Running FastAPI app...'
                sh 'docker run -d -p 8000:8000 $DOCKER_IMAGE'
            }
        }
    }
}
