# SQL Assessment

## Instructions
1. Open this repo in Gitpod by clicking the green gitpod button
1. The tests to check your answers for the assessment will run one time when it opens, you'll see that the first query is still failing
1. All of the challenges to complete are in the challenges directory. Write the SQL query that gets the data requested in the comment prompt in each file. 
1. To test your queries, you can click on the debug icon and then run the tests by clicking the green play button next to the text "Test Sql Queries". (Unclick the "Uncaught Breakpoints" checkbox so that you don't have to press continue each time the program exits) Running this the first time may open the `test.py` file (which it is running). If you close it after running it, it should not open again the next time you run the tests. 
1. You will see feedback for every correct query until the first query the test encounters that either errors or has the wrong data. Look in the debug console for either a "Correct!" message, a SQL error, or your actual results and the expected results if they differ. 
1. Once all of your queries are correct, or as many of them are correct as you can get, commit and push your code to the main branch of your repo so that Github classroom can grade it. 

## The Rules
1. Though this codebase is written in Python, you do not need to write or debug any Python to take this assessment. The only place you should edit or write code is in the `.sql` files in the challenges directory.
1. Do not use any *column aliases* unless you are specifically asked to. the assessment is looking for very specific data, and you will notice that if your column names differ from the expected ones, the query will not pass. All of the column names are unique in the db, so aliasing them is unnecessary. You may use table aliases if you wish.
1. You may only write one SQL command per file. It will break the program if you try to run more than one in a file.
1. If you select duplicate column names, you will noticed that only one appears in your results. it's one of the limitations of this program, but it won't affect the actual data you are getting back. 