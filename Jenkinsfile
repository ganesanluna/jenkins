pipeline {
    agent { docker { image 'ubuntu:latest' } }
      stages {
        stage('build') {
      steps {
        FROM ubuntu:20.04
        sh "apt-get update"
        sh "apt-get upgrade -y"
        sh "apt-get install -y python3"
        sh "chmod +x class_add.py"
        sh "./class_add.py"

      }
    }
  }
}
