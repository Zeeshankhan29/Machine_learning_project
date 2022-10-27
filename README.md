# Machine_learning_project
Machine learning project 


software and account Requirements

1. [Github account](https://github.com)
2. [IDE vscode](https://code.visualstudio.com)
3. [Heroku Account](https://dashboard.heroku.com/login)
4. [Git Cli](https://git-scm.com/docs/gitcli)


Creating virtual environment in your project folder
```
conda create -p myenv python=3.10 -y

```

Activate the environment created
```
conda activate myenv/

```

```
pip install -r requirements.txt

```

To add all files to git

```
git add .

```

To add specific files to git

```
git add <file name>

```

> To ignore files or folder from git we can write name of file or folder

To check the git status

```
git status

```


To check all the version of Git

```
git log

```

To create version/commit aal changes by git 

```
git commit -m "your message"

```

To send version/changes to git

```
git push origin main

```

To check remote url

```
git remote -v

```

To set up CI/CD pipeline in heroku we need this information

```

1. HEROKU_EMAIL =   zeeshankhan29khan@gmail.com
2. HEROKU_API_KEY = cfa62bd4-213a-4e9f-a9c6-abf8b7332749
3. HEROKU_APP_NAME = machinelearningapp3

```

To build Docker image

```

docker build -t <image_name>:<tagname>

```


Note : Image name for docker should be in lowercase only

To list docker image

```

Run docker image

```

To Run docker image

```
docker run -p 5000:5000 -e PORT=5000 <docker image id>

```

To check running docker containers

```
docker ps

```

To stop docker container

```

docker stop <>container_id>

```