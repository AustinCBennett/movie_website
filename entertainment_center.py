import fresh_tomatoes
import media

#This file provides the information for each movie.

#These functions create an instance of the class Movie, and assigns an instance referance to a variable. 
the_dark_knight = media.Movie("The Dark Knight",
                              "The worlds greatest detective faces his greatest enemy",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

return_of_the_jedi = media.Movie("Return of the Jedi",
                                 "Return to a galaxy... Far, far away",
                                 "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                                 "https://www.youtube.com/watch?v=XgB4gaY2dWE")

inception = media.Movie("Inception",
                        "No dream is safe",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

godzilla = media.Movie("Godzilla",
                       "The king is back",
                       "https://upload.wikimedia.org/wikipedia/en/1/10/Godzilla_%282014%29_poster.jpg",
                       "https://www.youtube.com/watch?v=vIu85WQTPRc")

winter_soldier = media.Movie("Captain America: The Winter Soldier",
                             "In heroes we trust",
                             "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",
                             "https://www.youtube.com/watch?v=tbayiPxkUMM")

back_to_the_future = media.Movie("Back to the Future",
                            "Marty McFly just broke the time barrier. He's only got one week to get it fixed.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                            "https://www.youtube.com/watch?v=qvsgGtivCgs")

#creates a list of Movie instance referances
movies = [the_dark_knight, return_of_the_jedi, inception, godzilla, winter_soldier, back_to_the_future]

#opens the movies page in the browser
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__name__)
print(media.Movie.__module__)
