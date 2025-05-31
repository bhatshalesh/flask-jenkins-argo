pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('flask-app')
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    docker.image('flask-app').run('-p 5000:5000')
                }
            }
        }
    }
}
