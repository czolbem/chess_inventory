pipeline {
        agent {
            docker { image 'python:3.11' }
        }
        stages {
            stage('Build') {
                steps {
                    sh 'python --version'
                }
            }
        }
    }