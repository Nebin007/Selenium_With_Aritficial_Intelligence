# Selenium_With_Aritficial_Intelligence
This project is an implementation of artificial intelligence in selenium Automation. By playing a game against computer.
>Please note inorder to run this script, it require chromedriver, which can be downloaded based on your [chrome version here](https://chromedriver.chromium.org/downloads)
>Also note this program is related to my previous project which is [JavaScriptNumbergame](https://nebin007.github.io/JavascriptNumbergame/). Which is number game with AI minimax algorithm.

## AIM with this project
We know that selenium is used for automated testing. By doing that we can find any flaws in the software we are creating, either web based or OS-based. With this project my main aim was to implement ***Artificial intelligence in automation testing.*** 


**What are the advantages?**.
By Doing this we will be able create a greater automation testing script, which can do anything including something which requires some intelligence. *Currently this project is using Minimax Algorithm to achieve its goals. There are better algorithms out there which helps us to gain more better ways.*


>Use the main.py to run this project. By typing "py/python main.py"

### Code divided by steps
1. This script first loads the site and take a random choice to go with "Artificial Intelligence" or "Yourself".
2. Next the script will scrap all the information regarding the numbers available, the score of the players and send towards the database.
3. The script uses minimax algorithm and chooses the best appropriate value for winning the game, according to the current state.

The main.py contains all the script regarding selenium automation. The gameclass.py contains the class for using minimax algorithm.

Here is the image depitction of the output can be seen in the console.
![image](https://user-images.githubusercontent.com/85371475/163390007-143eb0e6-a2eb-471a-aa0b-8f3b4c7db2eb.png)
