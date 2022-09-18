import psycopg2
import pandas as pd
import numpy

def get_connection():
    try:
        return psycopg2.connect(
            database="imdb",
            user="postgres",
            password="password",
            host="127.0.0.1",
            port=5432,
        )
    except:
        return False
  
conn = get_connection()
  
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")

#data=pd.read_csv(r'C:\Users\patry\OneDrive\Documents\GitHub\imdb\data\title_principals.tsv',sep='\t')

#print(data)

  
conn = get_connection()
curr = conn.cursor()

# Retrieve the top 20 movies with a minimum of 50 votes with the ranking determined by:
#(numVotes/averageNumberOfVotes) * averageRating

def top_20_movies():

    sql='''SELECT number_votes, primary_title, average_rating
    FROM titles_basics
    INNER JOIN ratings
    ON titles_basics.t_const = ratings.t_const
    where number_votes>50 and title_type='movie' 
    group by number_votes, average_rating, primary_title, titles_basics.t_const
    order by (number_votes/avg(number_votes)*average_rating) desc limit 20'''
    curr.execute(sql)
    rows=curr.fetchall()
    for row in rows:
        print(row)

# Original titles of the 20 movies

def original_title():
    sql='''SELECT top20.primary_title, original_title
    FROM top20
    INNER JOIN titles_basics
    ON titles_basics.primary_title = top20.primary_title
    group by top20.primary_title, original_title'''

    curr.execute(sql)
    rows=curr.fetchall()
    for row in rows:
        print(row)

# People credited within the top 20 movies

def people_credited():
    sql='''SELECT primary_title, primary_name
    FROM top20
    inner JOIN titles_principals
    ON titles_principals.t_const = top20.t_const
    inner join names_basics
    on titles_principals.n_const = names_basics.n_const
    group by top20.primary_title, top20.t_const, primary_name'''

    curr.execute(sql)
    rows=curr.fetchall()
    for row in rows:
        print(row)
    

    

if __name__ == '__main__':
    top_20_movies()

if __name__ == '__main__':
    original_title()

if __name__ == '__main__':
    people_credited()





