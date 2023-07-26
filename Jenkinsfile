pipeline {
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
                sh 'export DJANGO_SECRET_KEY=ThisIsMySecretKey'
                sh 'pip config set global.cert /etc/ssl/certs/ca-certificates.crt'
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