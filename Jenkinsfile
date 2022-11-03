pipeline {
    agent { docker { image 'ubuntu:latest' } }
      stages {
        stage('build') {
      steps {
        sh "uname -a"
        sh  "apt install python3 -y"
        sh "python3 class_add.py"
      }
    }
  }
}
