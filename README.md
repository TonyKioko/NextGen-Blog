Blog
===================
## Description
[Blog](https://nextgenblog.herokuapp.com/) is a website where users post and share their opinions on various topics. Users can also subscribe to the app to be informed of new posts via email.

------------------------------------------------------------------------
## User Stories
* As a user, I would like to view the blog posts submitted
* As a user, I would like to comment on blog posts
* As a user, I would like to view the most recent posts
* As a user, I would like to alerted when a new post is made by joining a subscription.
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Create user account | **Click Sign Up button** | New user registered |
| Welcome email | **On sign Up** | sends welcome email to new user|
| Display posts | **On the Home page** | PostS by writers displayed per time of posting |
| See full post | **Click reaf full post/post title** | Read full post and view comments |
| Create post | **Click New Post**  | Directed to form where writer fill post title and content  |
| Update Post | **Click Update button** | Post created directed to form to update post |
| Delete post | **Click Delete Post button** | Post deleted |

### Live Link ###
[Blog](https://nextgenblog.herokuapp.com/)
## Getting started

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3.6

### Cloning the repository
```bash
git clone https://github.com/TonyKioko/NextGen-Blog && cd NextGen- Blog
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
For this project you will need the following configurations plus email setup for email registration hmac verification.
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running the server
```bash
python manage.py runserver
```

### Admin Dashboard
Use django admin to manage the different users and posts.

### Deploying to heroku
Refer to this guide: [deployment to heroku](https://github.com/Benard18/Deployment_to_heroku_django)

## Running the tests
```bash
python manage.py app test
```

## Live Demo

The web app can be accessed from the following link:
[Blog](https://nextgenblog.herokuapp.com/)

## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)

## Test Driven Development
* Testing was done using python inbuild test tool called unittest


## Known Bugs
There are no known bugs.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license,Copyright (c) 2018 [Tony Kioko](https://github.com/tonykioko/)
