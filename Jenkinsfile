pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Python Project'
                bat 'py --version'
            }
        }

        stage('Install') {
            steps {
                bat 'py -m pip install pytest'
            }
        }

        stage('Test') {
            steps {
                bat 'py -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'Build Successful!'
        }

        failure {
            echo 'Build Failed!'
        }
    }
}