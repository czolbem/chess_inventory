pipeline {
    agent {
        dockerfile {
            filename             'Dockerfile'
            dir                  'docker'
            args                 '-v /tmp:/tmp'
        }
    }
    environment {
        DJANGO_SECRET_KEY = 'ThisIsMySecretKey'
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip config set global.cert /etc/ssl/certs/ca-certificates.crt'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Unittest') {
            steps {
                sh 'python manage.py test'
            }
        }
        stage("build & SonarQube analysis") {
            agent any
            def scannerHome = tool 'SonarScanner 5.0';
            steps {
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