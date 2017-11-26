## Background

- **Git Tutorial:**

	[Liao's Tutorial - in simplifed Chinese](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
	
	[Run Git on your browser](https://try.github.io/)

- **Python3 Tutorial:**

	[Tutorialspoint's Python3](https://www.tutorialspoint.com/python3/)
	
	[Liao's Tutorial(CH)](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
	 
	
- **Django Tutorial:**

	[Django Tutorial(EN)](https://docs.djangoproject.com/en/1.11/releases/1.8.2/)
	
	[Django Tutorial(CH)](http://usyiyi.cn/translate/django_182/index.html)
	
	**Notes**: If you know nothing about Django, please try the first demo in this tutorial, please.

- **Bootstrap Tutorial:**

	[Offical Tutorial(EN)](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
	
	[Offical Tutorial(CH)](http://www.bootcss.com)
	


## Clone this Project
```
$ git clone https://github.com/SamuelXing/MedicationManager.git

```

## How to make it run
1. **Downloading Docker** (suggesting stable version)
	
	- for Mac: [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
	- for Windows: [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)

2. **Make it Run**
	- Make sure you have already start your docker service
	- goto the **root** directory of your project and run
	```$ docker-compose up``` 
	
	- you will see outputs like below (or equivalents) and then check [http://0.0.0.0:8000/](http://0.0.0.0:8000/) to see it works or not.
	
```djangosample_db_1 is up-to-date
Creating djangosample_web_1 ...
Creating djangosample_web_1 ... done
Attaching to djangosample_db_1, djangosample_web_1
db_1   | The files belonging to this database system will be owned by user "postgres".
db_1   | This user must also own the server process.
db_1   |
db_1   | The database cluster will be initialized with locale "en_US.utf8".
db_1   | The default database encoding has accordingly been set to "UTF8".
db_1   | The default text search configuration will be set to "english".

. . .

web_1  | May 30, 2017 - 21:44:49
web_1  | Django version 1.11.1, using settings 'composeexample.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```
			

####Note:

>On certain platforms (Windows 10), you might need to edit ALLOWED_HOSTS inside settings.py and add your Docker host name or IP address to the list. For demo purposes, you can set the value to:
>
> ```ALLOWED_HOSTS = ['*']```
>
>Please note this value is not safe for production usage. Refer to the Django documentation for more information.


## Contributing
1. **The Github Flow**

-	GitHub is designed around a particular collaboration workflow, centered on Pull Requests. This flow works whether you’re collaborating with a tightly-knit team in a single shared repository, or a globally-distributed company or network of strangers contributing to a project through dozens of forks. It is centered on the Topic Branches workflow covered in Git Branching.

-	**Here’s how it generally works:** **[Code Example(IMPORTANT)](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/)**

	1. Fork the project

	2. Create a topic branch from master.

	3. Make some commits to improve the project.

	4. Push this branch to your GitHub project.

	5. Open a Pull Request on GitHub.

	6. Discuss, and optionally continue committing.

	7. The project owner merges or closes the Pull Request.


## TODO

- [x] UserModule (Working on)
- [ ] DrugModule (done the framework)
- [ ] PlanModule (done the framework)
- [ ] Search(Spider?)
- [ ] Front-End(html, css, js) (Wroking on)

## Notes

**superuser**

username: tiger, password: tiger

**docker commands to migrate DB**

```
$ docker ps  # check the running container
$ docker exec -t -i <container_id> bash  # entering the container env
$ python manage.py makemigrations
$ python manage.py migrate

```
	
