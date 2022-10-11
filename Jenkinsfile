pipeline { 
    environment { 
        registry = "leenalr/flaskapp" 
        registryCredential = 'dockerhub_leena' 
        dockerImage = ''
    }
    agent any 
   
    stages { 
        stage('Building our image') { 
            steps {
                
               sh 'docker build --network host -t flaskapp:$BUILD_NUMBER .' 
            } 
        }
        stage('Scan') {
             steps {
                script {
                    sh 'docker run --rm --network host -v /var/run/docker.sock:/var/run/docker.sock -v /var/jenkins_home/.cache:/root/.cache/ aquasec/trivy:0.18.3 image -f json -o /root/.cache/results.json flaskapp:$BUILD_NUMBER'     
                }
             }
        }
    stage('pushes our image') { 
        steps { 
            script { 
                docker.withRegistry( '', registryCredential ) { 
                        sh 'docker tag flaskapp:$BUILD_NUMBER leenalr/flaskapp:$BUILD_NUMBER'
                        sh 'docker push leenalr/flaskapp:$BUILD_NUMBER'
                    }
                } 
            }
        
        } 
    }
    post {
        success{
            sh 'printenv'

            echo '========pipeline executed successfully ========'
            office365ConnectorSend color: '#00ff00',

                                   message: " Job name : ${env.JOB_NAME} Build number: ${env.BUILD_NUMBER} Build id: ${env.BUILD_ID} Git branch: ${env.BRANCH_NAME}  Git commit: ${env.GIT_COMMIT} New image is pushed to ${env.registry} and build tag is ${env.BUILD_TAG} Log can be referenced : ${env.COPY_REFERENCE_FILE_LOG}",

                                   status: 'Success',
                                      
                                   webhookUrl: "https://datasirpiprivatelimited.webhook.office.com/webhookb2/756c1311-753c-4c87-8b8f-16df76ee44dc@69e0551c-0320-425f-b935-c3e87cb83212/JenkinsCI/9ac5dbbc962e4484a2c99c0552a673e9/47de5d67-1661-48fd-ab0f-6c7ca49d8cfc"

        }

        failure{

            echo '========pipeline execution failed========'

            office365ConnectorSend color: '#ff0000',


                                   message: " Job name : ${env.JOB_NAME} Build number: ${env.BUILD_NUMBER} Build id: ${env.BUILD_ID} Git branch: ${env.BRANCH_NAME}  Git commit: ${env.GIT_COMMIT} New image is pushed to ${env.registry} and build tag is ${env.BUILD_TAG} Log can be referenced : ${env.COPY_REFERENCE_FILE_LOG}",
                                   
                                   status: 'Failure',

                                   webhookUrl: "https://datasirpiprivatelimited.webhook.office.com/webhookb2/756c1311-753c-4c87-8b8f-16df76ee44dc@69e0551c-0320-425f-b935-c3e87cb83212/JenkinsCI/9ac5dbbc962e4484a2c99c0552a673e9/47de5d67-1661-48fd-ab0f-6c7ca49d8cfc"

        }
        always {
            archiveArtifacts artifacts: "/root/.cache/result.json", fingerprint: true
                
            publishHTML (target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: '/root/.cache',
                reportFiles: 'result.json',
                reportName: 'Trivy Scan',
                ])
            }
    }
}

