pipeline {
    agent {
        docker { image 'ubuntu:latest' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'cat /etc/os-release'
                sh 'pwd'
                sh 'apt install python3'
                sh 'python3 class_add.py'
            }
        }
    }
}
