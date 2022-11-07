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
            }
        stage('Deploy') {
            steps {
               	sh 'zip herd_010.zip class_add.py'
               	sh 'ls'
               	docker copy herd_o10.zip /home/ganesan/Desktop
            }    
        }
    }
}
