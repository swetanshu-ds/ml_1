##  machine_learning_project

## Start machine learning project

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS CODE IDE](https://code.visualstudio.com/download)
4. [Git CLI](https://git-scm.com/downloads)
5. [Git command documentation](https://docs.github.com/en/get-started/using-git/about-git)
6. [To run any python.py file](use -> python file_name.py)


Steps: 
1. Create repo from github
2. Include a gitignore file, apache license while creating a repo.
3. Add a readmy file
4. Then create a virtual environment using command
   --    conda create -p name python==3.x -y
   This will create a env in your local root folder where you want to build the machine learning project and not in the C drive


5.   Make a requirements.txt file 
6.   Now create an app.py file  
7.   Now create heroku account and then create docker file as - "Dockerfile"
8. Then create file -  ".dockerignore"
9. create a folder in root dir  - ".github" and inside this create another folder - "workflows"  and inside this create another file as "main.yaml"
10. Create a folder in root dir - name as "housing"
11. Then create a file setup.py in root dir
12. Create a file __init__.py inside housing
13. Now ,within housing ,create folder as component,config, entity, exception, logger, pipeline and withing each folder , create __init__.py file
14. Start coding with exception and logging
15. Create stages of pipeline , like data ingestion data_validation , etc in components folder
16. Create pipeline.py in pipeline folder
17. Now in entity folder create config_entity.py
18. Now in root dir create config folder and inside it create config.yaml
19. Now within housing -> config create configuration.py file 
20. In housing , create util folder and within make util.py file and __init__.py
21. Now withing housing folder, create constant folder and inside it create  __init__.py
22. Now, inside entity folder, create artifact_entity.py
23. Difference between config_entity and artifact_entity.py is that config_entity is input schema and artifact_entity.py is output schema. 
24. Now create demo.py in root dir
25. 