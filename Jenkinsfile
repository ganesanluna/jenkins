pipeline {
    agent { docker { image 'ubuntu:latest' } }
      stages {
        stage('build') {
      steps {
        uname -a
        apt install python3
        python3 class_add.py
      }
    }
  }
}
