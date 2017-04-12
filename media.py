import webbrowser


class Movie():
    """Data structure for storing favorite movies objects

    Attributes:
        title (str): Title of the movie
        storyline (str): The plot of the movie
        poster_image_url (str): The web URL of the poster image for the movie
        trailer_youtube_url (str): The full YouTube URL of the trailer for the movie
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Return an instance of the Movie class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open browser instance to load YouTube trailer of movie"""
        webbrowser.open(self.trailer_youtube_url)
