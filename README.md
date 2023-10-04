# Milestone Project - 4 Lush Bakes

![Mock up]()

[Vist my website here](https://lush-bakes-p4-3fb0d4cd2c41.herokuapp.com/)

Milestone Project 4 calls for a full stack site based around business logic used to control a centrally-owned dataset. I have created an e-commerce site using Django, Python, HTML, Javascript and CSS for 'Lush Bakes by Lisa'. The site will display images of bakes that allows potential customers to order a celebration bake, read reviews and login.

## Owners Goal

The primary objective of the Lush Bakes website is to provide an online shopping experience for customers looking to purchase celebration cakes, cupcakes or cookie cakes.

1. Facilitate the ordering process of ordering bakes by allowing customers to view, select and items to their shopping bag.
2. Capture user interest and engagement, reading reviews and follow links to Lush Bakes social accounts.
3. Enables users to create an account to save their delivery details for future orders.
4. Efficient order management by implementing CRUD functionality, enabling users to manage their order by adding, amending or deleting items in their basket.

## Audience

The audience will include mostly females, between the ages of 25 - 55.

# UX

## The Strategy

The user experience strategy for the Lush Bakes website focuses on creating a user friendly and visually appealing interface with calming pastel hues to enhance the overall customer experience.

* User registration.
* Log in / Log out.
* View all bakes on offer.
* Select bakes to read description.
* Select category.
* Sort price order.
* Add item to the basket.
* Change quantity.
* Amend basket.
* Delete basket.
* View total price of line items.
* View delivery cost.
* View grand total.
* View a success message.
* View order number.
* Save delivery details.  

## The Scope

Within the Lush Bakes site I have ensured that the structure and organisation of content, features and functionalities have been designed in a logical and intuitive manner to facilitate easy navigation and access to bakes.

## The Structure

The website has a responsive navigation bar at the top of the page with clearly labelled pages along with a logo to navigate to the home page, shopping basket and account links. The landing page has a minimalist theme with a welcome message. The products available to buy are under the 'Bakes' page. Users can filter their specific category and then sort into price descending/ascending order if they wish. Users can read about Lush Bakes and read reviews. Social link in the footer will take the user to Lush Bakes social pages. Customers can select the bakes they wish to order, add them to the basket, amend or delete their quantity as well as see the total price of their basket. My account is where users can register, log in and view their profile.

## The Skeleton

The site has a number of pages clearly labelled in the nav bar. Along with linked buttons to take users to the relevant page.
Lush Bakes has been developed to be responsive enabling to use on small and large devices.

[Wire Frames]()

## The Surface

To maintain a consistent calming, light theme throughout the Lush Bakes website, pale green shades and a gradient effect have been used.

The fonts I have used are:

Heading Font
![Heading Font](/static/images/font-1.jpg)

Body Font
![Body Font](/static/images/font-2.jpg)

 The colours are consistent throughout the wiki.

![Colour Palette](/static/images/colours-green.jpg)

# Technologies Used

To help me create this website I used these technologies:

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Bootstrap](https://bootstrap.com/)
* [MDBootstrap](https://mdbootstrap.com/)
* [W3Schools](https://www.w3schools.com/)
* [Google Fonts](https://fonts.google.com/)
* [Bootstrap](https://bootstrap.com/)
* [Google Developer Tools](https://developer.chrome.com/docs/devtools/)
* [Github](https://github.com/)
* [Canva Colour Palette](https://www.canva.com/colors/color-palette-generator/)
* [Miro](https://miro.com/app/dashboard/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator)
* [Django](https://docs.djangoproject.com/en/4.2/)
* [Stack Overflow](https://stackoverflow.com/)
* [Heroku](https://heroku.com/)
* [ElephantSQL](https://api.elephantsql.com/)

# Database Schema

For this project I used a PostgreSQL database for its robust features and compatability with Heroku. To obtain this I opted for ElephantSQL - a cloud based PostgreSQL service, as per the learning materials in CI.

![Database Schema](/static/images/database.jpg)

User Profile enables registered users to save their delivery information for future orders, the form will be pre-filled to create an improved user experience. The model has a one-to-one field that is linked to the Django Allauth user account.

Order and Order line item are used in the 'Checkout' app. These are used to make purchases and make payment. Included in these are the total line price, quantity and grand total. It also contains information regarding the payment method, the Stripe PID, basket contents and checkout complete.

The product and category is within the 'Products' app. All products available to purchase can be individually added to the database. The products can be amended or deleted in the database by the admin user only. The category stores the different categories of bakes on offer.

# Testing

# Manual testing for my project

The project was tested on the browsers listed below:

* Chrome *v.116.0.5845.111*
* Opera *v.102.0.4871.0*
* Firefox *v.117.0*
* Safari *v.16.6*
* Edge *v.116.0.1938.62*

During development of this website, testing has played an important part in this project, to ensure a smooth and intuitive experience for the user. I have identified and resolved various issues during development. The most significant challenge being the views for the checkout and dealing with inconsistent styling across devices. Research and utilisation of responsive design principles allowed me to overcome most issues. Addition to this I encountered problems when deploying to Heroku and database queries.

By enduring the extensive testing I have overcome most problems.

![Further testing]()

# Validation
![Lighthouse](/static/images/light-house-lb.jpg)
![Lighthouse](/static/images/light-house-1.jpg)
![W3C CSS Validator](/static/images/css-val-lb.jpg.jpg)
# User Stories

## User - 1

First time visitor can intuiively navigate through the website.
![Landing page](/static/images/lush-bakes.jpg)

  Landing page shows a bakes that have been purchased, clearly shows navigation and icons for account and basket.
## User - 2

I am new to online shopping. will I know when I have made an order or added an item to the bag.

![Landing page](/static/images/completed-order.jpg)

User will see confirmation of order view. Along with this a toast message will pop up when a user registers, places an item in bag.
## User - 3

A regular customer does not have a desktop computer or laptop, can the site be viewed on modile devices.

![User-3](/static/images/mobile.jpg)

Lush Bakes is fully responsive
## User - 4

As a first time user can I sort the products by price order.

![User-4](/static/images/sort.jpg)

## User - 5

As a user, can I clearly see what I have added to my basket. If I change my mind can I delete it or amend the quantity.

![User-5](/static/images/basket-1.jpg)
Users can change the quantity of their item, or/and delete the item without leaving the basket page.

## User - 6

As the owner can I amend products or delete products

![User-6](/static/images/admin-1.jpg)
![User-6](/static/images/amend-1.jpg)

# User - 7

As the owner can I view orders in the database and change if needed.

![User-6](/static/images/database-1.jpg)

# Deployment

As part of the criteria for this project, Lush Bakes has to be deployed to Heroku.

To do this the following must be completed:

1. Create a requirements.txt file so Heroku can install the required dependencies to run the app. This can be done by typing in the terminal.

   * pip3 freeze --local > requirements.txt

2. Create a Procfile to tell Heroku what type of application is being deployed and how to run it.

   * web: gunicorn lush_bakes.wsgi:application

3. Sign up and create a Heroku account.

4. Select the 'New' tab and click create new app. Insert your app name and choose a region. Click create app.

5. Make your way to the Deploy tab. Select 'Connect to Github' for the deployment method. Select your correct repository and connect to it.

6. Before you click deploy, go to the Settings tab, click on the Reveal Config Vars tab to configure environmental variables. Insert the following
   * DATABASE_URL: taken from ElephantSQL
   * SECRET_KEY:  *Your own secret key*
   * STRIPE_PUBLIC_KEY: *Your own public key from Stripe*
   * STRIPE_SECRET_KEY: *Your own secret key from Stripe*
   * AWS_ACCESS_KEY_ID: *Your own access key from AWS*
   * AWS_SECRET_ACCESS_KEY: *Your own secret access key from AWS*
   * USE_AWS: True

7. Go back to the Deployment tab and select 'Deploy Branch'

8. You app should now be deployed.

## Stripe Payment

To make a payment using the Stripe test method use the card details from the documentation on Stripe site.

Use card number:

* 4242 4242 4242 4242

Use a valid future date:

* such as 24/24.

* any 3 digits for the CVC.
