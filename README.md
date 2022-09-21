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
  
