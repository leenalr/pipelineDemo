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
                  script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            } 
        }
        stage('push our image') { 
            steps { 
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                } 
            }
        }   
    }
}
