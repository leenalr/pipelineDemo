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
   stage('Example stage 1') {
     steps {
       office365ConnectorSend webhookUrl: "https://datasirpiprivatelimited.webhook.office.com/webhookb2/756c1311-753c-4c87-8b8f-16df76ee44dc@69e0551c-0320-425f-b935-c3e87cb83212/JenkinsCI/9ac5dbbc962e4484a2c99c0552a673e9/47de5d67-1661-48fd-ab0f-6c7ca49d8cfc", 
                      message:"started ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)",
                      factDefinitions: [[name: "Commit Message", template: "${commit_message}"],
                                       [name: "Pipeline Duration", template: "${currentBuild.durationString.minus(' and counting')}"]]              }
        }
     }
  }
