pipeline {
    agent {
        docker { image 'busybox:latest' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'apt-get update'
                sh 'apt-get install python3'
                sh 'python3 class_add.py'
            }
        }
    }
}
