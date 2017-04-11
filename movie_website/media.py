import webbrowser

class Movie():
    
    def __init__(self, title, story, poster, trailer):
        '''This is the __init__ function
        
        Attributes:
            title(str): The title of the movie instance
            title(movie_story): The story summary of the movie instance
            title(poster_image_url): The website poster link of the movie instance
            title(trailer_youtube_url): The youtube promotion trailer of the movie instance
        
        '''
        self.title = title
        self.movie_story = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        
    def show_trailer(self):
        '''
        This function allow us to open the link we provided in the webbrower
        
        '''
        
        
        webbrowser.open(self.movie_trailer)
    