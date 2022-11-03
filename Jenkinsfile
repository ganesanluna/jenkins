pipeline {
    agent { docker { image 'ubuntu:latest' } }
      stages {
        stage('build') {
      steps {
        FROM ubuntu:20.04
        RUN apt-get update
        RUN apt-get upgrade -y
        RUN apt-get install -y python3

      }
    }
  }
}
