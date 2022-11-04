pipeline {
    agent { docker { image 'ubuntu:latest' } }
      stages {
        stage('build') {
        steps {
            apt-get update
            # apt-get upgrade -y"
            # RUN "apt-get install -y python3"
            sh "chmod +x class_add.py"
            sh "./class_add.py"

      }
    }
  }
}
