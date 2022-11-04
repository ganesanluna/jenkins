pipeline {
    agent {
        docker { image 'node:ubuntu' }
    }
    stages {
        stage('Test') {
            steps {
                sh cat /etc/os-release
                sh pwd
            }
        }
    }
}
