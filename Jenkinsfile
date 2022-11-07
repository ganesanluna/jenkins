pipeline {
    agent {
        docker { 
            image 'ubuntu:20.04' 
            args '-u root:sudo' 
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'apt update'
                sh 'apt install -y python3'
                sh 'python3 class_add.py'
                sh 'cat /etc/os-release'
            }
        }
    }
}
