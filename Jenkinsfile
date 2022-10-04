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

                                   message: " ${env.JOB_NAME} with ${env.BUILD_NUMBER} and build_id ${env.BUILD_ID} succeeded on branch ${env.BRANCH_NAME} with Git commit hash ${env.GIT_COMMIT}.(space, space) New image is pushed to ${env.registry} and build tag is ${env.BUILD_TAG}",

                                   status: 'Success',
                                      
                                   webhookUrl: "https://datasirpiprivatelimited.webhook.office.com/webhookb2/756c1311-753c-4c87-8b8f-16df76ee44dc@69e0551c-0320-425f-b935-c3e87cb83212/JenkinsCI/9ac5dbbc962e4484a2c99c0552a673e9/47de5d67-1661-48fd-ab0f-6c7ca49d8cfc"

        }

        failure{

            echo '========pipeline execution failed========'

            office365ConnectorSend color: '#ff0000',

                                   message: "ProjectX service build ${env.BUILD_ID} failed on ${env.BRANCH_NAME}.(space, space)",

                                   status: 'Failure',

                                   webhookUrl: "https://datasirpiprivatelimited.webhook.office.com/webhookb2/756c1311-753c-4c87-8b8f-16df76ee44dc@69e0551c-0320-425f-b935-c3e87cb83212/JenkinsCI/9ac5dbbc962e4484a2c99c0552a673e9/47de5d67-1661-48fd-ab0f-6c7ca49d8cfc"

        }
    }
}

