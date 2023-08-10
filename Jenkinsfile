pipeline {
    agent any
    environment {
        DJANGO_SECRET_KEY = 'ThisIsMySecretKey'
    }
    stages {
        stage("build & SonarQube analysis") {
            environment {
                SCANNER_HOME = tool 'Default';
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${env.SCANNER_HOME}/bin/sonar-scanner"
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