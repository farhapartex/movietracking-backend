## Real time searching Movie info & tracking

### How to Setup Backend

* Clone this backend repo and navigate to the project folder
* Create your virtual environment & turn it on by `source venv/bin/activate` where venv is the virtual env directory name
* Install all packages by this command: `pip install -r requirementsx.txt`
* Create an account in `https://rapidapi.com/`
* Go to this link `link` & generate a rapid api key. You may need to add a card info, but it will not charge anything. There is a free subscription.
* Create an env file by `touch .env` & copy everything from `.sample.env` file
* Create a Database in PostgreSQL and put the information in `.env` file
* Don't forget to add rapid api key in the `.env` file
* Again back to the terminal
* Run DB migration by: `python manage.py migrate`
* Create a superuser: `python manage.py createsuperuser`, after provide a username & password. For username, please use an email
* Run the server: `python manage.py runserver` and open the link `http://localhost:8000/`


### Setup Frontend
* Clone repo from this link: https://github.com/farhapartex/movie-tracking-frontend
* Navigate to the project directory
* Install all packages by using `yarn` command
* Run the frontend server by `yarn start`

### How the system works

* For real time searching I used Rapid API data
* When user search with movie title, I pull information form the Rapid API server and try to match with the DB. Return a list of movie information with some extra information like, is the movie has been selected as `Watched` or as `Favorite`.
* In the search list, if any movie `Watched` or `Favorite` before, user can not request again to make it `Watcher` or `Favorite`. By this way we can prevent unused/unnecessary request to Rapid API server
* In the search list, if any movie is `Watcher` or `Favorite` before, the button in the frontend will be disabled automatically
* So now, when user click on `Add Watch` or `Add Favorite` button, from the search list, the system will send a request to Rapid API server to get full information and store it in the database. This happend only once. What does it mean. Suppose from the search list, user click on `Add Watch` button & system send request to the Rapid API server first time & pull all information & save data. So if user now wanna add the movie `X` as favorite & click on `Add favorite` button, our system will see that the movie already in the system. So it will not request Rapid API server again. But it will update some fields just.
* When user click on `Detail` button, system fetch information from system Database, not Rapid API server.


### Demonstration

You can watch, how it looks like & how it works actually from this link: https://youtu.be/hpnh9qnCFZg