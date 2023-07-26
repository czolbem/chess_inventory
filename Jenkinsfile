pipeline {
        agent {
            docker { image 'python:3.11' }
        }
        stages {
            stage('Build') {
                steps {
                    sh 'pip install -r requirements.txt'
                }
            }
            stage('Unittest') {
                steps {
                    sh 'python manage.py test'
                }
            }
        }
    }