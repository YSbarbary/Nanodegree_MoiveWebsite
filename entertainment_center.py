import fresh_tomatoes
# fresh_tomatoes is the html file for the movie trailers website
import media
# movies instances
Toy_Story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://goo.gl/Vid4Zn",
                        "http://www.youtube.com/watch?v=ZZv1vki4ou4")

Avatar = media.Movie("Avatar",
                     "A marine on an alient planet",
                     "http://goo.gl/cbYLTi",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

Beauty_and_the_Beast = media.Movie("Beauty and the Beast",
                                   "Can She Lift the Curse on His Life?",
                                   "http://goo.gl/NMkjAi",
                                   "https://goo.gl/C37UKF")

Lion_King = media.Movie("Lion King",
                        "Will the King Return to Pride Rock?",
                        "http://goo.gl/RVJscY",
                        "https://www.youtube.com/watch?v=YkULiFjPjU")

UP = media.Movie("UP",
                 "Loves goes on a great adventure",
                 "https://goo.gl/UoH0DM",
                 "https://www.youtube.com/watch?v=qas5lWp7R0")

Finding_Nemo = media.Movie("Finding_Nemo",
                           "An adventure at sea",
                           "http://goo.gl/EBzM09",
                           "https://www.youtube.com/watch?v=gcwv1Gflh4Q")
# movies Array
movies = [Toy_Story, Avatar, Beauty_and_the_Beast, Lion_King, UP, Finding_Nemo]

fresh_tomatoes.open_movies_page(movies)
