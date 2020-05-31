pipeline {
  environment {
    registry = "appy385/flask-aws"
    registryCredential = 'docker-hub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Unit and Functional testing') {
       steps {
          sh '''
          python3 -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt
          python -m pytest --verbose --junit-xml test-reports/results.xml
          deactivate
          rm -rf venv
          '''

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
