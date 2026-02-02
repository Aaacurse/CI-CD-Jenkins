pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        VENV = "env"
    }

    stages {

        stage("Echo Hello World") {
            steps {
                echo "Hello World"
            }
        }

        stage("Checkout Code") {
            steps {
                checkout scm
            }
        }

        stage("Setup Python") {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage("Install Dependencies") {
            steps {
                sh '''
                    . $VENV/bin/activate
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "No requirements.txt found"
                    fi
                '''
            }
        }

        stage("Run Tests") {
            steps {
                sh '''
                    . $VENV/bin/activate
                    if command -v pytest >/dev/null 2>&1; then
                        pytest
                    else
                        echo "pytest not installed"
                    fi
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build Successful'
        }
        failure {
            echo '❌ Build Failed'
        }
    }
}
