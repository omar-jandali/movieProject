import webbrowser

#this is the class that will be used to create instances of each
#movie that is going to be created
class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #the init function is the main fuction that is going to be called when
    #the Movie class is called. and all of the variables are going to be
    #assigned with the right information
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #this is the trailer for the selected movie that you get once
    #you click on the poster
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
