pipeline {
    stages {
        stage('Build') {
            steps {
                sh 'docker pull ubuntu:latest'
                step {
                   sh 'apt-get update'
                   sh 'apt-get install python3 -y'
                   sh 'python3 class_add.py'
                }
              }
            }
        }
    }
}
