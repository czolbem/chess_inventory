pipeline {
    agent {
        dockerfile {
            filename             'Dockerfile'
            dir                  'docker'
            args                 '-v /tmp:/tmp'
        }
    }
    tools {
        jdk 'jdk17'
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
        stage("SonarQube Analysis") {
            agent {
                label 'built-in'
            }
            environment {
                SCANNER_HOME = tool 'SonarQube Scanner 5';
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${env.SCANNER_HOME}/bin/sonar-scanner"
                }
            }
        }
        stage("Quality Gate") {
            agent {
                label 'built-in'
            }
            steps {
                timeout(time: 1, unit: 'HOURS') {
                waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}