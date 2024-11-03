# CI/CD for Minecraft Server in Jenkins using Docker! 🚀

I decided to automate the deployment and testing of the Minecraft Bedrock server using Jenkins, Docker, and a few smart steps in the Jenkinsfile. Below you will find a brief analysis of the entire pipeline process, which can be useful for anyone who wants to learn something new about CI/CD and games!

In the Jenkinsfile, the pipeline is divided into several stages that work closely together to ensure smooth operation:

1. **Stage Clone Repository** - First, we clone the repository to have access to the latest code. This is a crucial step to ensure that all subsequent stages operate on the most recent version.

2. **Stage Install Python Dependencies** - We install the required Python dependencies, including the `pip` package manager, to run the scripts that help download the latest version of the server.

3. **Stage Create Python Virtual Environment** - We create a Python virtual environment where we install all the necessary libraries, such as `requests` and `beautifulsoup4`. This environment is used to run the script that downloads the latest version of the server.

4. **Stage Download Bedrock Server** - A key component is a Python script that automatically accepts the terms of use and downloads the latest version of the Minecraft Bedrock server without manual intervention. This ensures we always have access to the current server version.

5. **Stage Build Docker Image** - We pull the Docker image for the Minecraft Bedrock server, configure all the required dependencies, and then build our own image. This is the foundation of the entire automation.

6. **Stage Test Docker Image** - We test the Docker image by running it in a test environment. We verify that the server files are present and that the environment is functioning correctly.

7. **Stage Deploy to Test Environment** - We use Docker to deploy the server to a test machine, with Jenkins starting the container with the appropriate ports. We make sure that the server has started correctly by analyzing the logs.

8. **Stage Automated Tests** - We automatically test the server's operation, verifying that the ports are properly listened to from an external perspective. This ensures that the server is available to players.

9. **Stage Backup Existing Production** - Before deploying to production, we make a backup of the current server state to easily restore data if necessary.

10. **Stage Deploy to Production** - We deploy the latest version of the server to the production environment, replacing the previous container. If necessary, we restore the backup of the world.

11. **Stage Monitor Production Server** - We monitor the production server, ensuring that it is available from an external perspective and that the ports are correctly listened to.

The entire pipeline is designed to work both on a local server and in Oracle Cloud, making it a universal solution for many environments. Docker plays a key role, providing portability and repeatability of the environment.

Want to see how it all works? Check out my GitHub repository:
https://github.com/pcmagik/ci-cd-minecraft-bedrock-jenkins-server-game

This is just the beginning of the CI/CD adventure for games! 🎮

#devops #jenkins #docker #cicd #minecraft #automation #oraclecloud

[🇵🇱 Polish version of this file](README_PL.md)