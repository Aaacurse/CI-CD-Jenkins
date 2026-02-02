pipeline{
    agent any

    triggers {
        githubPush()
    }
    
    environment {
        VENV ="env"
    }

    stage {
        stage("Checkout code"){
            steps{
                checkout scm
            }
        }

        stage("Setup Python"){
            steps{
                sh '''
                    python3 --version
                    python3-m venv $VENV
                    .$VENV/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage("Install Dependencies"){
            steps{
                sh'''
                    .$VENV/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage("Run Test"){
            steps{
                sh'''
                    .$VENV/bin/activate
                    pytest
                '''
            }
        }
    }

    post{
        success{
            echco 'Build Sucessful'
        }
        failure{
            echo 'Build Failed'
        }
    }
}