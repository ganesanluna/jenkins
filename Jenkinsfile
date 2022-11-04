pipeline {
    agent {
        docker { image 'ubuntu:latest' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'python3 class_add.py'
            }
        }
    }
}
