pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                echo 'Checking Python Version'

                bat '"C:\\Users\\selva\\AppData\\Local\\Python\\bin\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies'

                bat '"C:\\Users\\selva\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Pytest'

                bat '"C:\\Users\\selva\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v --html=report.html --self-contained-html'
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

        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}