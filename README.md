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


# Folder structure

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

            echo "Starting Docker login process..."
            # Docker login
            echo "docker password" | docker login --username docker username --password-stdin && echo "Docker login successful." || echo "Docker login failed."

            echo "Pulling the latest image of your image name..."
            # Pull the latest image
            docker pull user/count-app:latest && echo "Successfully pulled latest image." || echo "Failed to pull the latest image."

            echo "Stopping existing container named count-app-container..."
            # Stop the existing container (ignore errors if it does not exist)
            docker stop count-app-container && echo "Successfully stopped count-app-container." || echo "No existing count-app-container to stop."

            echo "Removing existing container named count-app-container..."
            # Remove the existing container (ignore errors if it does not exist)
            docker rm count-app-container && echo "Successfully removed count-app-container." || echo "No existing count-app-container to remove."

            echo "Removing all but the latest image of arpit75/count-app..."
            # Remove all images except the latest
            docker images arpit75/count-app -q | tail -n +2 | xargs -r docker rmi && echo "Old images removed." || echo "No old images to remove."

            echo "Running a new container from the latest image..."
            # Run a new container from the latest image with a specific name
            docker run -d --name count-app-container -e AWS_ACCESS_KEY_ID=aws access key -e AWS_SECRET_ACCESS_KEY=aws secret key -e AWS_DEFAULT_REGION=ap-south-1 -p 8000:8000 user/count-app:latest && echo "Container started successfully." || echo "Failed to start the container."
            echo "Script execution completed."

- aws Change security

    Secutity --> security group -> inbound rules -> Alltraffic , anywhere -> save changes.
        

