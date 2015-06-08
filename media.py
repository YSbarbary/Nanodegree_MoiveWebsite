import webbrowser
class Movie ():
   
###This class provides the format for our movie trailers website. 
###Each movie will feature a title, poster image, Youtube trailer, and storyline. 
    def __init__(self, movie_title, movie_storyline, poster_image,
              trailer_youtube):
                 #the structure of each movie entry
        self.title = movie_title
        #includes the movie title 
        self.storyline = movie_storyline
        #includes a basic story summary
        self.poster_image_url = poster_image
        #includes a movie poster from Wikipedia
        self.trailer_youtube_url = trailer_youtube
        #launches the youtube trailer in the same browser window
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
###Clicking on a movie poster will open a Youtbe trailer on the same page
