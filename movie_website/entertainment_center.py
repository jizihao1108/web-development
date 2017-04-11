import media
import fresh_tomatoes as ft


# Create instance of Kimi no Na wa Movie
    
Kimi = media.Movie('Kimi no Na wa', 
              'A high school girl exchange her body with a boy',
              'https://myanimelist.cdn-dena.com/images/anime/9/7' \
              '7484l.jpg',
              'https://www.youtube.com/watch?v=k4xGqY5IDBE')

# Create instance of Suzumiya Haruhi no Shoushitsu Movie

Suzu = media.Movie('Suzumiya Haruhi no Shoushitsu', 
                 'Kyon heads over to school and the SOS club acitivites', 
                 'https://images-na.ssl-images-amazon.com/images/I/7' \
                 '18%2Bm4A5PBL._SY445_.jpg', 
                 'https://www.youtube.com/watch?v=eHKyNQopYXo')

# Create instance of Steins;Gate Movie

Stein = media.Movie('Steins;Gate Movie',
                  'Kurisu Makise returns to Akihabara and reunites ' \
                  'with Rintarou Okabe',
                  'https://image.tmdb.org/t/p/original/lOTyDiEkjwgQT' \
                  'NvhAC8WxtNCZh5.jpg',
                  'https://www.youtube.com/watch?v=rDsCNz3pWUg')
    
# Generate the list of movies
    
movie_list = [Kimi, Suzu, Stein]

# Set up the website 

ft.open_movies_page(movie_list)


        