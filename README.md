# docker_fastapi

# docker locally

    - docker build -t fastapi-app-simple .

        write small application in main.py and  write docker.

        fastapi-app-simple(image name) and . represents present directory.


    - docker run -d -p 80:8000 fastapi-app-simple

        80 for docker.

        8000 for local machine.


# set the secret key and password

    - In the repository go to settings -> secerts and variables -> Action

    DOCKER_ACCESS_TOKEN : your docker password.

    DOCKER_USERNAME : docker user name


# Folder structure in the ec2

    - In ec2 instance

        *** webhook/hooks.json ***

        [
            {
            "id": "update-docker-image",
            "execute-command": "/home/ubuntu/webhook/script.sh",
            "command-working-directory": "/tmp"
            }
        ]

        - webhook/script.sh

            File name  :  script.sh

            #!/bin/bash

            set -e

            echo "Starting Docker login process..."
            # Docker login
            echo -n "Docker password" | docker login --username dockerusername --password-stdin && echo "Docker login successful." || { echo "Docker login failed."; exit 1; }

            echo "Pulling the latest image of dockerusername/image nmae..."
            # Pull the latest image
            docker pull dockerusername/image nmae:latest && echo "Successfully pulled latest image." || { echo "Failed to pull the latest image."; exit 1; }

            echo "Stopping existing container named container name(fastapi-app-simple-container)..."
            # Stop the existing container (ignore errors if it does not exist)
            docker stop container name >/dev/null 2>&1 && echo "Successfully stopped fastapi-app-simple-container." || true

            echo "Removing existing container named fastapi-app-simple-container..."
            # Remove the existing container (ignore errors if it does not exist)
            docker rm container name(fastapi-app-simple-container) >/dev/null 2>&1 && echo "Successfully removed Container name(fastapi-app-simple-container)." || true

            echo "Removing all but the latest image of dockerusername/image name..."
            # Remove all images except the latest
            docker images dockerusername/imagename -q | tail -n +2 | xargs -r docker rmi && echo "Old images removed." || true

            echo "Running a new container from the latest image..."
            # Run a new container from the latest image with a specific name
            docker run -d --name container name -p 8000:8000 docker user name/imagename:latest && echo "Container started successfully." || { echo "Failed to start the container."; exit 1; }
            echo "Script execution completed."

- Permission for the files

    chmod +x /home/ubuntu/webhook/script.sh

- aws hooks command: 

    webhook -hooks /home/ubuntu/webhook/hooks.json -verbose -port 7000

    Run the above command in aws ec2.


- Docker commands for running the Docker inside:

    1) docker build -t fastapi-app-simple .

    2) docker run -d --name fastapi-app-simple-container -p 8000:8000 fastapi-app-simple


- aws Change security

    Secutity --> security group -> inbound rules -> Alltraffic , anywhere -> save changes.

- sudo apt install webhook <- in ec2
  

