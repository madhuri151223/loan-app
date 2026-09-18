pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest test_app.py -v'
            }
        }

        stage('Deploy') {
            steps {
                sh 'python3 deploy.py'
            }
        }
    }
}
