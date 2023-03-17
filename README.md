# CodeClause-March-PYTHON-DEVELOPMENT
This repository is to share my workings as a Python Developer Intern at CodeClause.
## I am Adarsh pursuing engineering CSE at Ramaiah University of Applied Science
# Task1_URL shortener
## IDE used: Pycharm
Description: In this code we have installed and imported an library function called pyshortners. This code defines a function called shorten_url() that takes a URL as input, creates a pyshorteners object, and uses the TinyURL provider to shorten the URL. The function returns the shortened URL.The code then prompts the user to enter a URL, calls the shorten_url() function to shorten the URL, and prints the shortened URL to the console.

URL: https://github.com/adarshc70/CodeClause-March-PYTHON-DEVELOPMENTE/blob/main/Task1-URL%20Shortener.py
Our main goal is to make large url as a short.
# Task2_Alarm Clock with GUI
Description: In this code we creates a simple alarm clock with a graphical user interface using the tkinter library in Python.The datetime, time, and winsound libraries are imported for the purpose of getting the current time, setting the alarm, and playing a sound respectively.

The alarm function takes the set alarm time as a parameter and runs an infinite loop that checks the current time every second. If the current time matches the set alarm time, the function plays a sound to wake up the user and then breaks out of the loop. If the current time is greater than the set alarm time, the function prints a message to stop the alarm and then breaks out of the loop.

The actual_time function takes input from the user in the form of the day, month, year, hour, minute, and second of the alarm time and calls the alarm function with the set alarm time.

The main part of the code creates a window using tkinter. It also creates six StringVar() variables to store the values of day, month, year, hour, minute, and second entered by the user, and six Entry widgets to accept the user input. Finally, it creates a button widget that calls the actual_time function when clicked.

When the user enters the required time and clicks the Set Alarm button, the actual_time function is called and the alarm is set. When the current time matches the set alarm time, the alarm function is called and the sound plays until the user stops the program.

The output of the program will be a GUI window with six input fields and a button to set the alarm. Once the user enters the required time and clicks the button, the alarm will be set and will play the sound at the set time.


