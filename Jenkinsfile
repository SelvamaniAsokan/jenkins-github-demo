pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Python Project'
                bat '"C:\\Users\\selva\\AppData\\Local\\Python\\bin\\python.exe" --version'
            }
        }

        stage('Install') {
            steps {
                bat '"C:\\Users\\selva\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
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
    }
}s