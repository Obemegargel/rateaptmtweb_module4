# Overview

I am tired of not having good, accurate, updated information to go off of when trying to find the best apartment to stay at. I made Rate My Apartment to fix this problem.
Because this site's information is input from locals in the area I can be confident it will stay updated and will be better suited to the market it was made for than a website that tries to read information from other sites many people have already tried this but it is too complicated or too taxing on one indavidual that quickly it seems to become outdated.

to run this site on a local server to host go into the terminal and paste this code:
python app.py
then copy the text:
http://127.0.0.1:5000
and paste it in a search engine.


{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/0RmBHJBX5QI)

# Web Pages
The main Rate My Apartment page has two halfs of the form. You can fill out as much as you want. The first half saves a stay at a previous apartment. The second have saves your most recent purchase of an apartment so people can see how much it costs now rather than in the past. This will be accurate and useful data mostly around the time where people are actively signing leases for apartments in their area.

Page two takes all the inputs of previous anonymous forms and sorts them in a table to compare prices and ratings etc.

There are links to move conveniently between both pages.

# Development Environment
The form is written in html, and is stylized using css.
In a python file I use flask to take the values I request from the form and write those values to a csv file. Then I take that csv file and again using flask I write the csv information to a table on my second page.

{Describe the tools that you used to develop the software}
-Visual Studio Code 2022

{Describe the programming language that you used and any libraries.}
-python 3.11.5 64bit 
-css
-html
-flask (framework) you don't need to download anything
# Useful Websites

{Make a list of websites that you found helpful in this project}
* [ChatGPT](https://chat.openai.com/c/e9ebf047-a510-470d-833b-5193997e7f15)
    Ask ChatGPT things like how to write to a csv file using a html and css form and then post your code as you go, allows Chat GPT to give you ideas on how to fix it and helps you understand how your files can be set up. It is good for learning how to make things and is not just used for getting the answer because sometimes it does not work so you must understand what is going on. Still very useful though.
* [Stack Overflow](https://stackoverflow.com/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1 Add more updated questions
* Item 2 Eventually get it online
* Item 3 perform calculations on data recieved as well as filters