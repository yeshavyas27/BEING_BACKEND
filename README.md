# BEING BACKEND SERVER
Marketplace to rent outdoor media space

Setup
1. Clone the repo
2. Switch to the current directory
    ```
    cd /path/to/BEING_BACKEND
    ```
3. Create the docker image of the application 
    ```
    docker build -t being_backend .
    ```
4. Add values of mongo db host, user and passwork in docker-compose.yml
5. Run the image / make a container
   ```
   docker-compose up
   ```
