prototype
=========

This prototype will focus on creating a web application that communicates with REST services ( backend application ) and displays the information on the frontend application.

Features this application should have
  - Integration with google maps using Google Maps SDK.
  - Filter information by category.
  - CRUD operations ( create, read, update, delete ) places.
  - Use Google Maps SDK to draw points, lines and polygons on Google Map Tiles, this draws should be saved on a MongoDB collection, and fetched/displayed when you click on place to see details.
  - Inputs the places should have [ name - required, description - optional, LatLng (coordinates) - required, photos - required ]

Technologies
=========
- You will need to run a HTTP Reverse Proxy server called NGINX ( not the usual apache )
- You will code your webservices with python and django framework ( do it the restfull way ) 
- You will use git as a concurrent version control and to deploy your apps
- You will use Twitter Bootstrap to ease the development of the frontend design ( HTML5, CSS, JS ) 
- You will use Backbone to implement a MV* approach to frontend development. ( client side logic )
- You will create the schema and use MySQL to save info from places [ name, description, latlng and photos ], 1-N relation on photos
- You will use MongoDB to save points, lines and polygons.

Recommended Tools
=========
- Use pip/easy_install package manager to install python packages
- SequelPro to manage your mysql db
- iTerm2 ( a better terminal )
- ghi to work with github issues on terminal
- vagrant to create your VM instance instead of working on your local machine
- Chrome Developer Tools to frontend debug

Requirements
=========
- Implement Test Driven Development
- Atleast backend code should be tested ( UnitTest ), there are libraries that easy this

Issues
=========
All issues should go to this GitHub repository Issues. 


Recommended Documentation
=========
[andre mete aqui isto sf q n tenho tempo]

Deadlines
=========
- Yesterday - Start exploring the technologies and methodologies 
- February 12 - You should have a grasp knowledge of all the development stack, start developing the prototype
- February 24 - Deliver the prototype

This will be some hard days, but are of utmost importance to integrate you in the team.

