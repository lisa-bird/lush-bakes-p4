# Milestone Project-4 Lush Bakes

![Mock up]()

[Vist my website here]()

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

# Features left to implement

* Features that are left to implement include 'admin rights' and a search or filter option. Time constraints have prevented me from developing these. These may be added in the future.

# Technologies Used

To help me create this website I used these technologies:

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Bootstrap](https://bootstrap.com/)
* [W3Schools](https://www.w3schools.com/)
* [Google Fonts](https://fonts.google.com/)
* [Google Developer Tools](https://developer.chrome.com/docs/devtools/)
* [Github](https://github.com/)
* [W3C Markup Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator)
* [Django](https://docs.djangoproject.com/en/4.2/)
* [Stack Overflow](https://stackoverflow.com/)
* [Heroku](https://heroku.com/)
* [ElephantSQL](https://api.elephantsql.com/)

# Data Schema

The data schema consists of tables. Each table is defined with spefic columns to store information related to users, articles and comments.
![User table](/flaskr/static/img/table-1.jpg)

As you can see from the screenshot above the 'id' is a unique identifier for each user. The username must be unique and cannot be Null.

![Article table](/flaskr/static/img/table-2.jpg)

Again a unique 'id' for each article. 'author_id': Foreign key referencing the 'id' column of the 'user' table, defining the author of the article. 'created' The timestamp of when the article was created, cannot be Null. 'title' 'summary' 'body' all cannot be Null. 'img' A field for storing the image associated with the article.

![Comments table](/flaskr/static/img/table-3.jpg)

Similar to the article table with the addition of 'article_id': Foreign key referencing the 'id' column of the article table. Identifying the article to which the comment belongs to.

# Testing



# Manual testing for my project

The project was tested on the browsers listed below:

* Chrome *v.116.0.5845.111*
* Opera *v.102.0.4871.0*
* Firefox *v.117.0*
* Safari *v.16.6*
* Edge *v.116.0.1938.62*

 When deploying the project I had some issues with Heroku. The main problem being that I did not have the correct file for Heroku to run the app. I added a run.py file to the project to include how the app runs, which solved the problem.

 During testing, once deployed, it become apparant that the users and the data being inserted into the app was not being saved. I was using SQLite for my database. Thorough reasearch led to reading Heroku's ephemeral file system makes it unsuitable for SQLite databases. Heroku's file system is read-only, and any changes made to the file system will be lost whenever the application is restarted or scaled up. I then changed my code to accomodate Postgresql, to finally get the deployment correct.

![Further testing](/flaskr/static/img/test-ex.jpg)

# User Stories

## User - 1

First time visitor wants to understand what the purpose of the website is.

* Landing page shows a large heading with paragraph, clear register tab in nav.

![Landing page](/flaskr/static/img/user-story-1.jpg)

## User - 2

First time visitor wants to be able to see some articles before they register. Articles are visible but user can not read them or add new article without registering and logging in.

![Landing page](/flaskr/static/img/user-story-2.jpg)

## User - 3

First time visitor has registered and logged in. They can add an article and read the existing articles, commenting if they wish.

![User-3](/flaskr/static/img/user-story-3.jpg)

## User - 4

The author of an article wants to update the information. This can only be done by the author, the edit button will be visible, taking the user to the correct view. The user can also delete the article form here.

![User-4](/flaskr/static/img/user-story-4a.jpg)

## User - 5

First time visitor wants to be able to read the full article and see when it was posted and by whom

![User-5](/flaskr/static/img/user-story-5.jpg)

## User - 6

First time users and existing users want to be able to comment on articles, developing a community. The comment button takes them to the comment view.

![User-6](/flaskr/static/img/user-story-6.jpg)

## User - 7

First time users and existing users want to delete the article they have posted.

![User-7](/flaskr/static/img/user-story-7.jpg)

# Validation

CSS

All CSS was passed through the W3C CSS Validation Service, no errors reported
![CSS](/flaskr/static/img/css-val1.jpg)

Lighthouse
![Lighthouse](/flaskr/static/img/lighthouse.jpg)

Pep8

All code is Pep8 compliant, no errors. [Pep8](https://peps.python.org/pep-0008/)

# Deployment

As part of the criteria for this project, the Barbie Wiki has to be deployed to Heroku.

To do this the following must be completed:

1. Create a requirements.txt file so Heroku can install the required dependencies to run the app. This can be done by typing in the terminal.
   * pip3 freeze --local > requirements.txt

2. Create a Procfile to tell Heroku what type of application is being deployed and how to run it.

   * echo web: python run.py > Procfile

3. Sign up and create a Heroku account.

4. Select the 'New' tab and click create new app. Insert your app name and choose a region. Click create app.

5. Make your way to the Deploy tab. Select 'Connect to Github' for the deployment method. Select your correct repository and connect to it.

6. Before you click deploy, go to the Settings tab, click on the Reveal Config Vars tab to configure environmental variables. Insert the following
   * IP:  0,0,0,0
   * PORT:  5000
   * DATABASE_NAME:  *Your db name*
   * SECRET_KEY:  *Your own secret key*

7. Go back to the Deployment tab and select 'Deploy Branch'

8. You app should now be deployed.
