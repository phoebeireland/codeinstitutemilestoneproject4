# Evergreen Funeral Home

* [Link to deployed website](https://evergreenfuneralhome.herokuapp.com/)
* [Link to github repository](https://github.com/phoebeireland/codeinstitutemilestoneproject4)


# Contents

1. UX
2. The Website
3. Testing the Site
4. Deployment
5. Credits


# UX

## The Project- Purpose and Business Goals

This Website aims to inform users about the Evergreen Funeral Home, as well as offering them the ability to browse various funeral options such as urns, cremation and coffins. As it is, the website is mostly store-based, with the main focus on the funeral products that are available for purchase. The main purpose of the website is commercial, though the people visiting the website can also find out some information regarding the funeral home, as well as offer condolences on the blog page that posts news of local deaths and upcoming services. The website is accessible to users who have a 'profile' on the site and to those who do not. The difference between a user who has an account versus one who does not, is that the user with an account is able to access their profile and review past orders made through the site. Although a user may use the condolences blog with an account, an account is not necessary for leaving a comment. Furthermore, for a user who is a superuser, they gain further access to the admin side of the website, where they can approve new comments to the condolences blog posts. Furthermore, when a user is logged into the superuser accont, they had an additional option in the "My Profile" dropdown menu for 'Product Management', where they are able to add a new product without haveing to navigate to the full admin interface. Another unique ability for a superuser is that on both the product pages and the blog pages, they are able to edit, delete and, in the case of the blog, they are able to add a new blog post. Once again, this option bypasses the need for a superuser to go to the full admin dashboard to perform these functions.


## User Stories
A New User to the site wants:
1. An easily navigatable website and shopping area
2. The ability to buy products for an upcoming funeral
3. An area to find out a bit of information about the funeral home and those who work in it
4. A nice arrangement of product options
5. The ability to see what services are coming up, and offer condolences to those who died
6. The ability to pay on the website itself, and be able to recieve confirmation emails regarding the order
7. The ability to create an account to keep track of any purchases made

A Returning User to the site wants:
1. An easily navigatable website so I can find my created profile
2. The ability to look back on previous orders that were made
3. The ability to save contact/delivery details for an easier checkout in the future
4. The ability to search for a product or category of products if the specific name of a previously found product escapes my mind
5. The ability to sort the products based on certaion criteria. (ie. by price or name)


## Design Choices

The overall feel of the Website should be somber and clean. As a lot of the code for the project was modeled after the Boutique Ado project that was shown in the Code Institute videos, styilistically, not much differs between that site and this funeral site. Obviously elements were altered to make the design fit a funeral website rather than a clothing and housewares shop, but the main style features remained largely the same. 

### Font

The font used on this Website is Lato. Rather than picking a different, more fancy font from Google Fonts, I felt that the built-in font of Lato fit the website's overall aesthetic to the degree that looking elsewhere was not necessary. 


### Colours

The main colours used on the site are:
* 
* 
* 


### Styling




## Wireframe Designs
Provided additional information regarding the wireframes below each picture. Refer to them to explain where a wireframe may differ from the published product or for choices behind the designs.


### Homepage
![Wireframe of the Homepage](static/images/homepagewireframe.jpg "wireframe of the main hopmepage for the site")

This image shows the initial idea for the main page of the website. This is the page that the users would see if they were not logged in or they did not yet have an account.
The homepage would only change slightly if the user did have an account and was logged in- ie. the two card boxes with information and buttons would change accordingly if a user was logged into their account. In addition, the navbar at the top would also display slightly different options depending on whether the user was logged in or not. 



# Features
* 
* 
*  

### The Home Page
* 
* 
* 


# Testing the Site


All HTML pages and CSS files were tested using the HTML and CSS Validator from W3.
* Link to the [HTML Validator](https://validator.w3.org./) used
* Link to the [CSS Validator](https://jigsaw.w3.org/css-validator/) used


## Manual Testing

Using the Chrome Inspect tool, the following aspects of the website were tested:
* All of the contents on the pages of the website collapsed correctly when viewed on a smaller screen.
* The footer remained at the bottom of the pages when viewed on a smaller screen.
* The Navbar collapsed correctly when viewed on a smaller screen, and the correct code was there to enable to collapsed menu to expand when clicked. 
* The text within the boxes were all still correctly centered on smaller screens just as they were on the larger ones. 
* 



## Testing User Stories
### New User:
1. 
2. 

### Returning User
1. 
2. 


## Small Problems (that were fixed)
* 
* The Footer refused to stay at the bottom of the page on pages where there was not a lot of content. This was fixed by Googling, and landing on [this page](https://dev.to/nehalahmadkhan/how-to-make-footer-stick-to-bottom-of-web-page-3i14). As shown on the page, adding `min-height: 100vh`, `display:flex`, `flex-direction:column` and `margin-top:auto` to the `body` and `footer` styles in `style.css` fixed the problem. It was important to retain the original `height: calc(100vh - 164px);`, otherwise the page looked really weird.


# Deployment
The Website was created in Visual Studio Code, version controlled with Git and hosted on Heroku.

Steps to publish website to Heroku:
1. On Heroku, press "Create a New App"
2. On the new page, type in the app name and select the region for the app. Keep in mind that the app name must be completely original. Then press "Create".
3. Once the page has loaded, under the "Deploy" menu, select "Connect to GitHub", and enter the name of the repository to connect it to Heroku. 
4. Once it is connected, either choose "Automatic deploys" or "Manual deploy" and choose the branch that Heroku will deploy from. 
5. Make sure that there is a Procfile in the root of the directory. If there is not, create a new file and name it `Procfile`, making sure that the first letter is capitalised, otherwise Heroku will not register the file correctly. 
6. Within the Procfile, type: `web: python app.py`. This will tell Heroku exactly what the process type is (in this case it's `web`) and what the command is (`python app.py`)
7. Once the Procfile is created and filled in, push the change to the branch on GitHub that was specified as being the branch to deploy from. If automatic deploys were enabled, Heroku will automatically deploy the changes any time alterations are made to the deployed branch. If Manual deploys were used, you will have to manually deploy every time a large change is made. 
8. Another necessary step is to add the information that is in the `env.py` file to the "Config Vars" section in Heroku. This is necessray, because since the `env.py` file is in a `.gitignore`, it is ignored by GitHub, and therefore is not accessible to Heroku.
9. To add the information to the Config Vars, open the "Settings" section on the app page. Once opened, scroll down to the "Config Vars" area and click on "Reveal Config Vars".
10. Here, you will see two text boxes that say "Key" and "Value" respectively. Into the "Key" side, enter `SECRET_KEY`, `IP`, `PORT`, `MONGO_URI` and `MONGO_DBNAME`. On the "Value" side of each pair, enter the value stated in the `env.py` file and press the "add" button to add each pair. 
11. Once all of the steps are complete, Heroku should be able to publish the website. 

Steps to publish website to GitHub Pages:
1. On the main page of the repository, click settings.
2. Go to the GitHub Pages section on the menu bar to the left.
3. In the Source section, click "None" and change the selected branch to "main". 
4. Leave the following option as (root), and click "Save"
5. Once the repository is published, a link to the website will be shown in the GitHub Pages section. 

To Clone this repository using IDE Terminal:
1. Navigate locally to the directory in which you want to save the repository.
2. On the main page of the repository, click the "Code" button, and copy the HTTPS address.
3. In the terminal, run the command: 'git clone' followed by the HTTPS address.
4. The project will now be saved to the desired directory. 

To Clone this repository using Visual Studio Code:
1. Open a new window in VSCode.
2. On the main page of the repository, click the "Code" button, and copy the HTTPS address.
3. Back in VSCode, under "Start" click "clone repository" and paste the link into the textbox that pops up.
4. Navigate into the folder that you want the repository to be saved into, and "Select Repository Location".
5. The repository will now be saved to the selected location.


# Credits

Created by Phoebe Ireland

The content of this website was created by Phoebe Ireland, with the exception of the following:
* [Unsplash](https://unsplash.com/)
  * Used for the images found on the site
* [Bootstrap](https://getbootstrap.com/)
  * Used to create the Navbar and the footer
* [favicon.io](https://favicon.io/)
  * Used to create the favicon
* [jQuery](https://jquery.com/)
  * Uses jQuery for various Bootstrap functions 
* Code Institute's Task Manager Project
  * Used to model most of the code for the site.
* [Emailjs](https://www.emailjs.com/)
  * Used to connect the contact form to an email service. This is the main instance of JavaScript on the website.
* [Balsamiq](https://balsamiq.com/)
  * Used to create the wireframes.
* [Code Institute Boutique Ado Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1)
  * Used to model all of the main shop code for the funeral website.


   All of the content that was taken from other sources was altered to fit the use of this website where necessary.

A special thank you to my mentor for helping me though the project, and pointing out my (numerous) mistakes. 