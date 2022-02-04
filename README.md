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

# Structure

## Base template
The base template is used to hold elements that are displayed across the entire site i.e. navbar and logo.

## Home
The home page is where the user lands when accessing the website. It holds the store description, links and a large inviting image

## Products
The user can access any product from the navbar or view all products. Each product category can be sorted by price or rating.
The product card shows the product's rating, name, price, category and image.

## Product Details
The user can click on a product of their choice to view more details like description or enlarge product image for a better look.
This is also where the user can select the quantity of the product and add it to cart or return back to products page.

## Cart
The user can access the cart where all the products they have added are displayed along with the grand total price.
The user can increment/decrement the quantity of a product or even remove a product from cart if they wish to do so.

## Checkout 
Once the user is satisfied they can proceed to checkout to enter their delivery information and payment details.
if the user is signed in they will be able to check the option to save the checkout information to their profile.

## Profile
In the Profile page the user is able to view their orders and order details as well as update their delivery information

# Data Schema

## Profiles App
| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|User | user |	OneToOneField 'User'| on_delete=models.CASCADE
|Default Phone Number |	default_phone_number | CharField | max_length=20, null=True, blank=True
|Default Country | default_country | CountryField | blank_label='Country', null=True, blank=True
|Default Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
|Default Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True
|Default Street Address1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
|Default Street Address2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
|Default County | default_county | CharField | max_length=80, null=True, blank=True

## Products App
### Category
| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|Name | name | CharField | max_length=254
|Friendly Name | friendly_name | CharField | max_length=254, null=True

### Product
| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Category | category | ForeignKey |default='', max_length=254 | CharField
|Name | name | default='', max_length=254 | CharField
|Description | description | blank=True | TextField
|Price | price | max_digits=6, decimal_places=2 | DecimalField
|Image URL | image_url | blank=True | URLField
|Image| image| blank=True | ImageField

## Checkout App
### Order
| Name              | Database Key    | Field Type    | Type Validation                                                                       |
|-------------------|-----------------|---------------|---------------------------------------------------------------------------------------|
| Order Number      | order_number    | CharField     | max_length=32, null=False, editable=False                                             |
| User Profile      | user_profile    | ForeignKey    | UserProfile, on_delete=models.SET_NULL , null=True, blank=True, related_name='orders' |
| Full Name         | full_name       | CharField     | max_length=50, null=False, blank=False                                                |
| Email             | email           | EmailField    | max_length=254, null=False, blank=False                                               |
| Phone Number      | phone_number    | CharField     | max_length=20, null=False, blank=False                                                |
| Country           | country         | CountryField  | blank_label='Country'*, null=False, blank=False                                       |
| Postcode          | postcode        | CharField     | max_length=20, null=True, blank=True                                                  |
| Town or City      | town_or_city    | CharField     | max_length=40, null=False, blank=False                                                |
| Street Address 1  | street_address1 | CharField     | max_length=80, null=False, blank=False                                                |
| Street Address 2  | street_address2 | CharField     | max_length=80, null=True, blank=False                                                 |
| County            | county          | CharField     | max_length=80, null=True, blank=False                                                 |
| Date              | date            | DateTimeField | auto_now_add=True                                                                     |
| Delivery Cost     | delivery_cost   | DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                                 |
| Order Total       | order_total     | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                                |
| Grand Total       | grand_total     | Decimal Field | max_digits=10, decimal_places=2, null=False, default=0                                |
| Original cart     | original_cart   | TextField     | null=False, blank=False, default=''                                                   |
| Stripe Payment ID | stripe_pid      | CharField     | max_length=254, null=False, blank=False, default=''                                   |

### OrderLineItem
| Name            | Database Key   | Field Type   | Type Validation                                                                    |
|-----------------|----------------|--------------|------------------------------------------------------------------------------------|
| Order           | order          | ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product         | product        | ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE                         |
| Product Size    | product_size   | CharField    | max_length=2, null=True, blank=True                                                |
| Quantity        | quantity       | IntegerField | null=False, blank=False, default=0                                                 |
| Line Item Total | lineitem_total | DecimalField | max_length=6, decimal_places=2, null=False, blank=False, editable=False            |

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

# Tests



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
