import webbrowser  #here will import webbrowser that help us to open youtube url
class Movie(): # here we add class Movie and inside this class we will use function called  __init__ that is take place in the memory for arguments.
	""" this use for play the trailer for movies""" #> this for __doc__
	def __init__(self,Movie_title,movie_storyline,poster_image,trailer_youtube): #first we write self to rever the instance attrbute  (movie title ,movie_storyline,poster_imge,trailer_youtube)
		self.title= Movie_title # here we define varaible called self.title that take instance(self).and called aruments movie title for this instance(such as: self>toy_story.title)
		self.storyline= movie_storyline #here we define varaible called self.storyline it will give us the movie _storyline for self 
		self.poster_image_url= poster_image #here we define varaible called self.storyline it will give us the poster_image for self 
		self.trailer_youtube_url= trailer_youtube #here we define varaible called self.storyline it will give us the trailer_youtube for self 

	def show_trailer(self): # here we define function called show_trailer for play the youtube url its will take instace as self (show_trailer(toy_story)
		webbrowser.open(self.trailer_youtube_url) # here we use webbrowser.open to open youtube trailer for movie 