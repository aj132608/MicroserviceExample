Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:3.7.6-stretch' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('deploy') {
            steps {
                sh 'python -m microservice.app'
            }
        }
    }
}