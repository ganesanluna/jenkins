pipeline {
    agent { docker { image 'ubuntu:latest' } }
      stages {
        stage('build') {
          steps {
            RUN apt-get update
            RUN apt-get upgrade -y
            RUN apt-get install -y python3
            RUN chmod +x class_add.py
            RUN ./class_add.py
      }
    }
  }
}
