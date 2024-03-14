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

