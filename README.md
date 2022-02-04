GamerGarage is my final project for CodeInstitute. It is an online shop for the pc/console gaming community where users can purchase gaming related products.

# User Experience

## Site Owner Goals

**As the site owner, I would like to:**
* Access the admin section of the site
* Create, Read, Update and Delete products in the database from a centralised location through the admin app

## User Stories

**As a user, I want:**  
* the website to look nice
* to be able to create an account
* to be able to navigate through the website with ease
* to be able to personalize my account
* to be able to purchase products
* to be able to read the description of a product
* to be able to log in
* to be able to log out
* to be able to search for specific items
* to be able to easily checkout

# Design

* hero image covers most of the screen to catch user's attention
* the yellow color fits in nicely with the dark-grey to provide a bright but inviting feel

# Features

## Existing Features

* __navbar__ - allows the user to navigate through product pages
* __about section__ - lets the user know more about the website
* __profile__ - lets the user see their order history and provide default delivery information
* __search bar__ - allows for an easier way to locate products

# Technologies Used

## Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML)
-I used html (HyperText Markup Language) as the markup language for this project

* [CSS3](https://en.wikipedia.org/wiki/CSS)
-I used css3 to style many aspects of the website

* [JavaScript](https://www.javascript.com/)
-I used javascript for backend development

* [Python](https://www.python.org/)
-I used python to work on the backend of my project

## Framework

* [Bootstrap](https://getbootstrap.com/)
-I used Bootstrap to help me with responsive design  

* [Stripe](https://stripe.com/ie?utm_campaign=paid_brand-IE_en_Search_Brand_Stripe-1615558792&utm_medium=cpc&utm_source=google&ad_content=307359047676&utm_term=kwd-295607662702&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=EAIaIQobChMIluDI-8Ok9AIVCLLtCh0hgQj7EAAYASAAEgK7V_D_BwE)
-I used stripe as a payment system for my project

* [Django](https://www.djangoproject.com/)
-I used django to build my web app

## Libraries

* [Google-Fonts](https://fonts.google.com/)
-I used google fonts to import 'audiowide', 'mono' and 'tourney' fonts

* [Font-Awesome](https://fontawesome.com/)
-I used font awesome to add icons in certain parts of the project

* [jQuery](https://jquery.com/)
-jQuery was included with bootstrap to work with some bootstrap features

## Programs

* [Git](https://git-scm.com/)
-I used gitpod's terminal to commit my code and then to push it to GitHub

* [GitHub](https://github.com/)
-I used GitHub to store my project code 

## Tools

* [Heroku](https://id.heroku.com/login)
-I used heroku to deploy my project

*[AWS](https://aws.amazon.com/)
-I used AWS for cloud storage

# Deployment

## Heroku

1. Sign in or create an account on Heroku

2. Create a new app and choose an app name and region

3. Connect your Heroku app to your repository and enable automatic deployment

4. Add Postgres as your database in resources section

5. Copy and Paste your envioroment variable into settings.py file

6. run migrations

7. create a superuser 

8. run your app and access your admin page by logging in with your superuser credentials

9. load your fixtures to postgres

10. create a Procfile

11. freeze your requirements.txt

12. add your Heroku url to ALLOWED_HOSTS

13. add. , commit and push your changes

14. deploy your app in Heroku

15. now push your changes to automatically push them to heroku

# Code

* For most of this project, I used the Boutique Ado walkthrough project to help me through my project and borrowed a large amount of code to help with the structure of it also

* I used the [Django Documentation](https://docs.djangoproject.com/en/4.0/) for the Allauth setup and also with other aspects of setting up my project

* I used [Bootstrap](https://getbootstrap.com/) to create and style many aspects of this project

* I used [Stack Overflow](https://stackoverflow.com/), [Slack](https://slack.com/intl/en-ie/) and Tutor Assistance to solve many issues I faced in development
