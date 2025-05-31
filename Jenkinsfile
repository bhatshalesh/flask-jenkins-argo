pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t flask-app .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Use a different port (like 5001) to avoid conflicts
                    sh 'docker run -d -p 5001:5000 flask-app'
                }
            }
        }
    }
}
