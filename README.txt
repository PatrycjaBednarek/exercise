I have used Postgres 14.1 to create a database and store the data.
I have also included tables.txt file with the DDL statements



Problem Statement

Your task is to:

Create a database and tables to store IMDB data (recommendation is to use SQL-Lite or Postgres).
You will need to extract the file using 7zip or winzip. The TSV files can be opened with a normal text editor like Notepad++ for viewing
Create a python program that can connect to your database to answer the following questions
 

Q1. Retrieve the top 20 movies with a minimum of 50 votes with the ranking determined by:

(numVotes/averageNumberOfVotes) * averageRating

 

Q2. For these 20 movies, list the persons who are most often credited and list the different titles of the 20 movies.

 