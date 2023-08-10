pipeline {
    agent any
    tools {
        jdk 'jdk11'
    }
    environment {
        DJANGO_SECRET_KEY = 'ThisIsMySecretKey'
    }
    stages {
        stage("build & SonarQube analysis") {
            environment {
                SCANNER_HOME = tool 'SonarQube Scanner 5';
            }
            steps {
                sh 'java -version'
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