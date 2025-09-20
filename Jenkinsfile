pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image from backend/Dockerfile...'
                sh 'docker build -t met-expense-tracker:latest -f backend/Dockerfile backend'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests inside container (override CMD)...'
                sh 'docker run --rm met-expense-tracker:latest pytest'
            }
        }

        //stage('Run (smoke)') {
        //    steps {
        //        echo 'Starting container for smoke test...'
        //        sh 'docker run -d --name expense-smoke -p 8000:8000 met-expense-tracker:latest'
        //        // simple curl check
        //        sh 'sleep 5 && curl -f http://localhost:8000/health || exit 1'
        //        sh 'docker rm -f expense-smoke || true'
        //    }
        //}
    }

    post {
        always {
            echo 'Cleaning up dangling images...'
            sh 'docker image prune -f'
        }
        failure {
            echo 'Pipeline failed — check console output.'
        }
    }
}
