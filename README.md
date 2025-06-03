# Hypertropy: A health and fitness Web application
### Video Demo:  https://youtu.be/wZ8N6YYVk2c
### Description:
This is my final project for CS50X: Introduction to Computer Science. My web app enables users to get customized health advice and evaluation, meal planning tips and exercise tips.

### Languages
This project is coded with Python, HTML, CSS, JavaScript, SQL.

### Directories and files
These are some important directories and files in my project:

    1. app.py: this file is the main area of back-end programming for my project.
    2. templates: this directory is where I stored all of my HTML files, creating my web app DUI.
    3. python.db: this file is where I stored all of my users' information dynamically.
    4. helpers.py: a file with many useful libraries and frameworks I used
    5. static: a directory where I stored my background images and css file.

### Functions in app.py
These are some important functions in my app.py:

    1. login()
    2. register()
    3. logout()
    4. bmi()
    5. intro()
    6. meal()
    7. fitness()

#### login()
This is where I let users log into my Web app when they already have an account. This function is directly linked to the ***login.html*** file in the ***templates*** directory.

#### register()
My ***register*** function serve its purpose as letting the user register an account and then saving the account to ***project.db*** to let the user login again. This register is linked to the ***register.html*** in the ***templates*** directory.

#### logout()
The ***logout*** function is where users can log out of their account. By doing this, the web page will return to its ***intro.html*** page.

#### bmi()
This function is used to calculate the user's BMI and in turn ouput the user's health status. When the method is ***GET***, the function will return the ***bmi.html*** page. When the method is ***POST***, the function will return the ***bmi_calculated.page***

#### intro()
This function serves as a welcome to guest and users alike with ***intro.html***. If the user is signed in, then the function will return ***homescreen.html*** where the user will get all of his/her health evaluation.

#### meal()
This fuction will calculate the user's recommended calorie intake based on his/her health evaluation and give meal planning tips to the user. This function is linked to the ***meal.html*** file.

### fitness()
This function will give out some excercise and workout tips to the user. This function is linked to the ***fitness.html*** file.

### project.db
This is my database which contains of one table called ***users***. This table have the columns:
1. id
2. username
3. hash
4. height
5. weight
6. bmi
7. status
8. age

### Conclusion:
This is my final project for CS50X! It was very difficult to come up with an adequate project idea as CS50 taught me a lot of topics ranging from C to SQL. However, in my opinion, a project that sums up the whole course would be one consisting of the most topics and languages the course taught me. So the idea bears fruit. And after about 2 weeks of nonstop coding, the project is finally finished. Such a great journey!
