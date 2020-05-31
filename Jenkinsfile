pipeline {
  environment {
    registry = "appy385/flask-aws"
    registryCredential = 'docker-hub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Unit test') {
       steps {
          sh 'python3 -m venv venv'
          sh 'source venv/bin/activate'
          sh 'pip install -r requirements.txt'
          sh 'python -m pytest --verbose --junit-xml test-reports/results.xml'
          sh 'deactivate'
          sh 'rm -rf venv'

       }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry"
      }
    }
  }
}
