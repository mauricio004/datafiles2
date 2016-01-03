__author__ = 'MFlores1'

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


movies = [toy_story]


print media.Movie.__doc__
print media.Movie.__module__
print media.Movie.__name__
