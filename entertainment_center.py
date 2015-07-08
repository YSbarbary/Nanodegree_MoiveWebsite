import fresh_tomatoes
# fresh_tomatoes is the html file for the movie trailers website
import media
# movies instances
Toy_Story = media.Movie("Toy Story 3",
                        "A story of a boy and his toys that come to life",
                        "Lee Unkrich",
                        " John Lasseter (story), Andrew Stanton (story)"
                        "Tom Hanks, Tim Allen, Joan Cusack"
                        "8.4"
                        "http://ia.media-imdb.com/images
                         /M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

Avatar = media.Movie("Avatar",
                     "A marine on an alient planet",
                     "http://goo.gl/cbYLTi",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

Beauty_and_the_Beast = media.Movie("Beauty and the Beast",
                                   "Can She Lift the Curse on His Life?",
                                   "Masakazu Higuchi, Chinami Namba"
                                   "Jacob Grimm"
                                   "Susan Silo"
                                   "5.7"
                                   "http://goo.gl/NMkjAi",
                                   "https://www.youtube.com/watch?v=X6bnGiW4PNg")

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
                           " Andrew Stanton, Lee Unkrich",
                           " Andrew Stanton (original story by), Andrew Stanton (screenplay)",
                           " Albert Brooks, Ellen DeGeneres, Alexander Gould"
                           "8.2"
                           "http://goo.gl/EBzM09",
                           "https://www.youtube.com/watch?v=gcwv1Gflh4Q")
# movies Array
movies = [Toy_Story, Avatar, Beauty_and_the_Beast, Lion_King, UP, Finding_Nemo]

fresh_tomatoes.open_movies_page(movies)
