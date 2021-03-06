from __future__ import print_function
from tmdb_wrapper import TV
from tmdb_wrapper import Movie
from tmdb_wrapper import People


popular = TV.popular()

print("Popular TV shows")
for number, show in enumerate(popular['results'], start=1):
    print("{}. {} - {}".format(
        number, show['name'], show['popularity']))

popular_movies = Movie.popular()
print(popular_movies)
print("\n\nPopular Movies")
for number, movie in enumerate(popular_movies['results'], start=1):
    print("{}. {} - {}".format(number, movie['title'], movie['popularity']))

person = People.info(123)
print(person)

person_movie_credits = People.movie_credits(123)
print(person_movie_credits)
