pipeline {
    agent none
    tools {
        jdk 'jdk17'
    }
    environment {
        DJANGO_SECRET_KEY = 'ThisIsMySecretKey'
    }
    stages {
        stage('Build and Test') {
            agent {
                dockerfile {
                    filename             'Dockerfile'
                    dir                  'docker'
                    args                 '-v /tmp:/tmp'
                }
            }
            stages {
                stage('Build') {
                    steps {
                        sh 'python --version'
                    }
                }
                stage('Unittest') {
                    steps {
                        sh 'python --version'
                    }
                }
            }
        }
        stage('SonarQube') {
            agent {
                label 'built-in'
            }
            stages {
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
    }
}