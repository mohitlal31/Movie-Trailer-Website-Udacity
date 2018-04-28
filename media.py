import tmdbsimple as tmdb

tmdb.API_KEY = '2c1dbbabadb66b91ce5cd0d6ab18a66d'
poster_image_size = "w300"
youtube_base_url = "https://www.youtube.com/watch?v="


class Movies:
    def __init__(self,
                 title=None,
                 trailer_youtube_url=None,
                 poster_image_url=None):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    # Using a unique TMDB movie index, populate a movies object with title,
    # image URL and YouTube trailer URL
    def populate_movies_info(self, movie_index):
        movie = tmdb.Movies(movie_index)
        movie.info()
        title = movie.title
        # use the first poster in the list of posters returned
        poster_image_file_path = movie.images()["posters"][0]["file_path"]
        base_url = tmdb.Configuration().info()["images"]["base_url"]
        poster_image_url = base_url + poster_image_size + poster_image_file_path  # NOQA
        # use the first link in the list of trailer links returned
        youtube_video_key = movie.videos()["results"][0]["key"]
        trailer_youtube_url = youtube_base_url + youtube_video_key
        return Movies(title, trailer_youtube_url, poster_image_url)

    # returns a unique TMDB movie index from a movie name query 
    def get_tmdb_movie_index(self, movie_name):
        search = tmdb.Search()
        search.movie(query=movie_name)
        return search.results[0]['id']
