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

            echo '========pipeline executed successfully ========'
            office365ConnectorSend color: '#00ff00',

                                   message: "ProjectX service build ${env.BUILD_ID} succeeded on ${env.BRANCH_NAME}.(space, space)",

                                   status: 'Success',
                                    
                                   Build_details:"${env.JOB_NAME} ${env.BUILD_NUMBER}"

                                   webhookUrl: "${teamsUrl}"

        }

        failure{

            echo '========pipeline execution failed========'

            office365ConnectorSend color: '#ff0000',

                                   message: "ProjectX service build ${env.BUILD_ID} failed on ${env.BRANCH_NAME}.(space, space)",

                                   status: 'Failure',

                                   webhookUrl: "${teamsUrl}"

        }
    }
}

