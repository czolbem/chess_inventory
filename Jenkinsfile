pipeline {
    agent any
    tools {
        jdk 'jdk17'
    }
    environment {
        DJANGO_SECRET_KEY = 'ThisIsMySecretKey'
    }
    stages {
        stage('Build') {
            steps {
                sh 'java -version'
            }
        }
        stage('Unittest') {
            steps {
                sh 'python --version'
            }
        }
        stage("SonarQube Analysis") {
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
            steps {
                timeout(time: 1, unit: 'HOURS') {
                waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}