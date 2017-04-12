# Movie Trailer Website

This Movie Trailer Website consist of server side code to store a list of movies and generate a static web page, allowing visitors to browse the movies and play their trailers.

## Getting Started
Movies are created and stored in the `entertainment_center.py` file which imports from both the `media.py` and `fresh_tomatoes.py` files.  The `media.py` file contains the Movie class used to create new instance of movie objects, as well as the `show_trailer` method used to lauch the trailer of the movie on YouTube.

Movies can be created and stored in `entertainment_center.py` as follows:
```
movie = media.Movie(movie_title, movie_storyline, 
                    poster_image_url, trailer_youtube_url)
```

At the bottom of the `entertainment_center.py` file, all movie instances are stored in a list and passed to the `fresh_tomatoes.open_movies_page` method to create the web page for displaying poster art and trailers for each movie when clicked.

## License
The content of this Movie Trailer Website is licensed under a [Creative Commons Attribution License](https://creativecommons.org/licenses/by/3.0/us/).