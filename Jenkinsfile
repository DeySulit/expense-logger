pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "met-expense-tracker:latest"
        APP_PORT = "8000"
    }
    stages {
        stage('Checkout') {
            steps {
                // ensure repo is checked out to workspace
                checkout scm
                sh 'ls -la'
            }
        }
        stage('Build') {
            steps {
                echo "Building Docker image from backend/Dockerfile..."
                // -f points to Dockerfile and last arg is build context
                sh "docker build -t ${DOCKER_IMAGE} -f backend/Dockerfile backend"
            }
        }
        stage('Test') {
            steps {
                echo "Running tests inside container (override CMD)..."
                // override container command to run pytest; adjust if tests live elsewhere
                sh "docker run --rm ${DOCKER_IMAGE} pytest || (docker images && exit 1)"
            }
        }
        stage('Run (smoke)') {
            steps {
                echo "Running app container for a quick smoke test..."
                // remove any previous container with same name
                sh "docker rm -f fastapi-ci-run || true"
                sh "docker run -d --name fastapi-ci-run -p ${APP_PORT}:${APP_PORT} ${DOCKER_IMAGE}"
                // simple curl healthcheck (adjust to your app path)
                sh "sleep 2; curl -f http://localhost:${APP_PORT}/ || (docker logs fastapi-ci-run && exit 1)"
                // stop container when done (comment this if you want the container kept)
                sh "docker rm -f fastapi-ci-run || true"
            }
        }
    }
    post {
        always {
            echo "Cleaning up dangling images..."
            sh "docker image prune -f || true"
        }
        success {
            echo "Pipeline succeeded."
        }
        failure {
            echo "Pipeline failed — check console output."
        }
    }
}
