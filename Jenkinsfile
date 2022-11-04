pipeline {
    agent {
        docker { image 'ubuntu:latest' }
    }
    stages {
        stage('Build') {
            steps {
                cat /etc/os-release
                pwd
                apt install python3
                python3 class_add.py
            }
        }
    }
}
