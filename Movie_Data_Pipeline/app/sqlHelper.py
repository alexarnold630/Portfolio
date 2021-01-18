from sqlalchemy import create_engine
import pandas as pd
import numpy as np

class SQLHelper():

    def __init__(self):
        SQL_USERNAME = "postgres"
        SQL_PASSWORD = "password"
        SQL_IP = "35.193.140.4"
        PORT = 5432
        DATABASE = "postgres"
        self.connection_string = f"postgresql+psycopg2://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_IP}:{PORT}/{DATABASE}"
        self.engine = create_engine(self.connection_string)

    def get_top_10_movies(self):
        query = """
                SELECT
	                r.rank,
	                o.title
                FROM
                    movies o
	            JOIN ratings r on o.film_id = r.film_id
                limit 10
                """

        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

    def get_avg_rating_by_genre(self):
        query = """
                select
	                round(avg(r.rating),2) as avg_rating,
	                round(avg(r.num_reviews),2) as avg_num_reviews,
	                e.genre
                from
                    movies o
	                    join ratings r on o.film_id = r.film_id
	                    join film_genres f on o.film_id = f.film_id
	                    join genres e on f.genre_id = e.genre_id
                group by e.genre
                order by
	                avg_rating desc
                """
        
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

    def get_director_rating(self):
        query = """
                select
	                count(o.title),
	                d.director_name,
	                round(avg(r.rating),2) as avg_rating
                from
                    movies o
	                    join ratings r on o.film_id = r.film_id
	                    join film_directors f on o.film_id = f.film_id
	                    join directors d on f.director_id = d.director_id
                group by d.director_name
                order by
	                count desc
                """
        
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

    def get_actor_count(self):
        query = """
                select
	                count(o.title),
	                d.actor_name
                from
                    movies o
	                    join ratings r on o.film_id = r.film_id
	                    join film_actors f on o.film_id = f.film_id
	                    join actors d on f.actor_id = d.actor_id
                group by d.actor_name
                order by
	                count desc
                """

        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

    def get_titles_by_country(self):
        query = """
                select
	                count(i.country),
	                round(avg(r.rating),2) as avg_rating,
	                round(avg(r.num_reviews),2) as avg_num_reviews,
	                country
                from
                    movies o
	            join film_countries f on o.film_id = f.film_id
	            join ratings r on o.film_id = r.film_id
	                oin countries i on f.country_id =i.country_id
                group by i.country
                order by
                    count DESC
                """
        
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

