import fresh_tomatoes #here we import fresh_tomatoes file for use webpage style and use some function inside this file 
import media #here we import media python file for using the movie class and the functions inside this file (__init__,show_trailer)

#now will define 6 variable (this variables are my fevorate movies ) inside this variables we will use media file and Movie class and give this arguments 4 things (title,storyline,poster image,youtube trailer)

toy_story= media.Movie("Toy story","A story of a boy and his toys that come to life","https://i.ebayimg.com/images/g/xxUAAOSwPcVVoDr9/s-l300.jpg","https://youtu.be/KYz2wyBy3kc")
# here will go inside file called media inside this file we will us Movie class inside this class we will find function called __init__ that is take toy_story as self and give the title and other arguments 
#self.ttle >>toy_story.title


avatar= media.Movie("Avatar","A marine on an alien planet","http://www.thinkhero.com/wp-content/uploads/2010/08/Avatar-rerelease-movie-poster-limited-1.jpg","https://youtu.be/d1_JBMrrYw8")


troy= media.Movie("troy","A 2004 American film adapted from the epic of Homer Iliad, which tells the story of the Trojan siege,","https://i1.wp.com/thesefantasticworlds.com/wp-content/uploads/2014/03/troy-brad-pitt-movie-poster.jpg?fit=1024768&ssl=1","https://youtu.be/QpikTTSOHXc")


brave_heart=media.Movie("braveheart","Is an American film released in 1995, portraying the epic of William Wallace, who led the resistance against the British occupiers of Scotland during Scotland's wars of independence","https://upload.wikimedia.org/wikipedia/ar/b/bf/THE_Braveheart.jpg","https://youtu.be/wj0I8xVTV18")

room=media.Movie("room","Is a drama film produced in Canada and released in 2015. Starring Barry Larsson, Jacob Trimblay, Joanne Allen and William Messi","http://cima4u.tv/old/th_imgs/1450456083994155.gif","https://youtu.be/E_Ci-pAL4eE")


the_theory_of_everything= media.Movie("the theory of everything","The theory of everything is a biographical and romantic British film 2014 directed by James Marsh and written by Anthony McCartney, inspired by travel notes to infinity.","http://ghscientific.com/wp-content/uploads/2017/02/the-theory-of-everything-1920.jpg","https://youtu.be/Salz7uGp72c")


movies =[toy_story,avatar,troy,brave_heart,room,the_theory_of_everything] #here we will add list and add our fevorate movies inside it 

fresh_tomatoes.open_movies_page(movies) #here will we use the function open_movies_page that is inside fresh_tomatoes file