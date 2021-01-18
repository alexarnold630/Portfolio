table languages
{
language_id INT PK
language VARCHAR(100)
last_updated timestamp
}
table countries
{
country_id INT PK
country VARCHAR(100)
last_updated timestamp
}
table movies
{
film_id INT PK
title VARCHAR(100)
writer VARCHAR(20)
awards VARCHAR(20)
year DATE
plot VARCHAR(20)
poster VARCHAR(20)
last_updated timestamp
}
table genres
{
genre_id INT PK
genre VARCHAR(100)
last_updated timestamp
}
table actors
{
actor_id INT PK
actor_name VARCHAR(100)
last_updated timestamp
}
table film_actors
{
film_actor_id INT PK
film_id INT
actor_id INT
last_updated timestamp
}
ref{
  film_actors.film_id > movies.film_id
}
ref{
  film_actors.actor_id > actors.actor_id
}
table film_genres
{
film_genre_id INT PK
film_id INT
genre_id INT
last_updated timestamp
}
ref{
  film_genres.film_id > movies.film_id
}
ref{
  film_genres.genre_id > genres.genre_id
}
table ratings 
{
rating_id INT PK
film_id INT
num_reviews INT
rating INT
rank INT
last_updated timestamp
}
ref{
  ratings.film_id > movies.film_id
}
table directors
{
director_id INT PK
director_name VARCHAR(100)
last_updated timestamp
}
table film_directors
{
film_director_id INT PK
film_id INT
director_id INT
last_updated timestamp
}
ref{
  film_directors.film_id > movies.film_id
}
ref{
  film_directors.director_id > directors.director_id
}
table film_languages
{
film_language_id INT PK
film_id INT
language_id INT
last_updated timestamp
}
ref{
  film_languages.film_id > movies.film_id
}
ref{
  film_languages.language_id > languages.language_id
}
table film_countries
{
  film_country_id INT PK
  film_id INT
  country_id INT
  last_updated timestamp
}
ref{
  film_countries.film_id > movies.film_id
}
ref{
  film_countries.country_id > countries.country_id
}