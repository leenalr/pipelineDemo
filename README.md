<h1>Intro</h1>

This repo will help you to get started with dockerizing a simple python appllication and deploying it in kubernetes cluster

<h1>Sample output</h1>

https://flaskapp.trojanae.com/

<h1> Getting Started</h1>
In order to use this code, firstly clone the repo using git or download the zip file manually
        
        git clone https://github.com/leenalr/pipelineDemo.git
        cd pipelineDemo
        
<h1>How to run </h1>

<h3>Docker</h3>

<h5>1. Run a docker container for psql</h5>

        docker run -d --rm 
            \-p 5432:5432 
            \--name some-postgres 
            \-e POSTGRES_PASSWORD=mysecretpassword 
            \postgres
            
<h5>2.Creating a network</h5>

        docker network create appTopsql_network
 
Here, appTopsql_network is network name
To list the network,
    
        docker network ls
      
<h5>3.Build the Dockerfile</h5>

        docker build -t flaskapp:v1 .
  
To list the image,
  
        docker images 
<h5>4.Run the docker image</h5>
        
        docker run --rm 
        --name flaskapp\
        \--network appTopsql_network 
        \-p 5000:5000 
        \-ePSQL_URL="postgresql://postgres:mysecretpassword@some-postgres/postgres"
        \flaskapp:v1
        
        
 • check : http://127.0.0.1:5000
 
<h3>Docker-compose</h3>

<h5>To run the app USING Docker compose use this command</h5>

        docker-compose up -d
        
• check : http://127.0.0.1:5000

<h1> How to push docker image to docker hub</h1>

        docker login -u username -p password
        docker tag imagename:version reponame:version
        docker push reponame:version

<h1>Deploying in kubernetes</h1>

<h5>1.Create a namespace</h5>

        kubectl create ns flaskapp
<h5>2.Create secret for accessing your image repo</h5>
        Iam using docker hub
        
        kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
        
<h5>3.Deploy your application using helm</h5>
 
       cd k8s
       helm install flaskapp -n flaskapp .
       
<h5>4.Clone a chart for postgresql</h5>

        git clone https://github.com/helm/charts.git
        
<h5>5.Deploy postgresql</h5>

        cd charts/stable/postgresql
        helm install postgres -n flaskapp .
        

