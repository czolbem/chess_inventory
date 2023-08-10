pipeline {
    agent any
    environment {
        DJANGO_SECRET_KEY = 'ThisIsMySecretKey'
    }
    stages {
        stage("build & SonarQube analysis") {
            steps {
                script {
                    def scannerHome = tool 'SonarQube Scanner 5.0.1.3006';
                }
                withSonarQubeEnv('SonarQube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
          }
          stage("Quality Gate") {
            steps {
              timeout(time: 1, unit: 'HOURS') {
                waitForQualityGate abortPipeline: true
              }
            }
          }
    }
}