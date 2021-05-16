pipeline { 
    agent any 
    
    environment {
        JENKINS_NODE_COOKIE = 'dontKillMe'
        PORT = '5000'
        REACT_APP_ENV = 'staging'
    }

    stages {
        stage('Funny joke') { 
            steps {
                sh 'echo "taco about my feelings!!!"' 
            }
        }

        // stage('Deploy') {
        //     steps {
        //         script {
        //             try {
        //                 sh 'forever stop "react-ui"' 
        //             } catch(all) {
        //                 sh 'echo "react-ui is not running"'
        //             }
        //             sh 'forever --uid "react-ui" start -a -c "npm start" ./'
        //         }
        //     }
        // }
    }
}
