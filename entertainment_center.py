import fresh_tomatoes
###fresh_tomatoes is the html file for the movie trailers website
import media
###launches movie trailers
###Clicking on a trailer poster will open the Youtube trailer on the same page
Toy_Story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.rotoscopers.com/wp-content/uploads/2013/10/Toy-Story-Poster.jpg",
                        "http://www.youtube.com/watch?v=ZZv1vki4ou4")
#print (Toy_Story.storyline)
#Toy_Story.show_trailer ()
###Clicking on a trailer poster will open the Youtube trailer on the same page
Avatar = media.Movie ("Avatar",
                      "A marine on an alient planet",
                      "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print (avatar.storyline)
#Avatar.show_trailer ()
###Clicking on a trailer poster will open the Youtube trailer on the same page
Beauty_and_the_Beast = media.Movie("Beauty and the Beast",
                        "Can She Lift the Curse on His Life?",
                        "http://img3.wikia.nocookie.net/__cb20140922052152/disney/images/a/a7/Beauty_and_the_Beast_VHS_Poster_1992.jpg",
                        "https://www.youtube.com/watch?v=CGQcM8vBZLM")
#print (Beauty_and_the_Beast.storyline)
#Beauty_and_the_Beast.show_trailer ()
###Clicking on a trailer poster will open the Youtube trailer on the same page
Lion_King = media.Movie("Lion King",
                        "Will the King Return to Pride Rock?",
                        "http://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=YkULiFjPjU")
#print (Lion_King.storyline)
#Lion_King.show_trailer ()
###Clicking on a trailer poster will open the Youtube trailer on the same page
UP = media.Movie       ("UP",
                        "Loves goes on a great adventure",
                        "https://morganrlewis.files.wordpress.com/2014/02/up-poster.jpg?w=486",
                        "https://www.youtube.com/watch?v=qas5lWp7R0")
#print (UP.storyline)
#UP.show_trailer ()
###Clicking on a trailer poster will open the Youtube trailer on the same page
Finding_Nemo = media.Movie("Finding_Nemo",
                        "An adventure at sea",
                        "http://i.huffpost.com/gen/636511/thumbs/o-FINDING-NEMO-3D-900.jpg",
                        "https://www.youtube.com/watch?v=gcwv1Gflh4Q")
#print (Finding.Nemo)
#Finding_Nemo.show trailer ()
###Clicking on a trailer poster will open the Youtube trailer on the same page
movies =[Toy_Story,Avatar,Beauty_and_the_Beast,Lion_King,UP,Finding_Nemo]
fresh_tomatoes.open_movies_page (movies)
