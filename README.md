1. Run a docker container for psql

        docker run -d --rm 
            \-p 5432:5432 
            \--name some-postgres 
            \-e POSTGRES_PASSWORD=mysecretpassword 
            \postgres
            
2. Creating a network

        docker network create appTopsql_network
 
Here, appTopsql_network is network name

To list the network,
    
        docker network ls
      
3. Build the Dockerfile

        docker build -t flaskapp:v1 .
  
4.To list the image,
  
        docker images 
5. Run the docker image
        
        docker run --rm 
        \--name flaskapp 
        \--network appTopsql_network 
        \-p 5000:5000 
        \-ePSQL_URL="postgresql://postgres:mysecretpassword@some-postgres/postgres"
        \flaskapp:v1
        
        
 • check : http://127.0.0.1:5000
 
--------------------------------------------------------------------------------------------------------------------------------------------------------
Using docker-compose:

To run the app just use

        docker-compose up -d
        
• check : http://127.0.0.1:5000

-------------------------------------------------------------------------------------------------------------------------------------------------------

Deploying in kubernetes:

1. create a namespace

        kubectl create ns flaskapp
        
2. deploy using helm
 
       cd k8s
       helm install flaskapp -n flaskapp .
       
3. clone a chart for postgresql

        git clone https://github.com/helm/charts.git
        
4.deploy postgresql

        cd charts/stable/postgresql
        helm install postgres -n flaskapp .
        
