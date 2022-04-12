# SQL Assessment

## Instructions
1. Open this repo in Gitpod by clicking the green Gitpod button.
1. All of the challenges are in `challenges` directory. In each SQL file you will find a comment stating the prompt for that challenge. 
1. You do not need to complete every challenge in order to test a query, but the test will stop at the first query that is incorrect. Look in the debug console for feedback on the queries when they are tested. 
1. To test your queries, you can click on the debug icon and then run the tests by clicking the green play button next to the text "Test Sql Queries". (Unclick the "Uncaught Breakpoints" checkbox so that you don't have to press continue each time the program exits) Running this the first time may open the `test.py` file, which you can close.  
1. When you have gotten as far as you can, commit and push your code in the gitpod terminal to the main branch of your repo so that Github classroom can grade it. 

## The Rules
1. Though this codebase is written in Python, you do not need to write or debug any Python to take this assessment. The only place you should edit or write code is in the `.sql` files in the challenges directory. Start with the query beginning with `01`, and work your way up.
1. *Do not use any column aliases unless you are specifically asked to.* The assessment is looking for very specific data, and you will notice that if your column names differ from the expected ones, the query will not pass. All of the column names are unique in the db, so aliasing them is unnecessary. You may use table aliases if you wish.
1. You may only write one SQL statement terminating in a semicolon per file. It will break the tests if you try to run more than one in a file.
1. If you select duplicate column names (for example, `Musician.MusicianId` and `MusicianInstrument.MusicianId`), you will notice that only one appears in your results. It is one of the limitations of this program, but none of these queries require a column to appear twice.

## ERD
![Musician ERD](/MusicianERD.png?raw=true "Musician Database")
