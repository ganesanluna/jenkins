pipeline {
    agent {
        docker { image 'ubuntu:latest' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'apt update'
                sh 'apt install python3 -y'
                sh 'python3 class_add.py'
            }
        }
    }
}
