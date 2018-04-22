import fresh_tomatoes
import media

matrix_movie_index = media.Movies().get_tmdb_movie_index("The Matrix")
matrix = media.Movies().populate_movies_info(matrix_movie_index)

la_confidential_movie_index = media.Movies().get_tmdb_movie_index("LA Confidential")
la_confidential = media.Movies().populate_movies_info(la_confidential_movie_index)

dark_knight_rises_movie_index = media.Movies().get_tmdb_movie_index("The Dark Knight Rises")
dark_knight_rises = media.Movies().populate_movies_info(dark_knight_rises_movie_index)

intouchables_redemption_movie_index = media.Movies().get_tmdb_movie_index("The Intouchables")
intouchables = media.Movies().populate_movies_info(intouchables_redemption_movie_index)

inside_out_movie_index = media.Movies().get_tmdb_movie_index("Inside Out")
inside_out = media.Movies().populate_movies_info(inside_out_movie_index)

shawshank_redemption_movie_index = media.Movies().get_tmdb_movie_index("Shawshank Redemption")
shawshank_redemption = media.Movies().populate_movies_info(shawshank_redemption_movie_index)

movies = [matrix, la_confidential, dark_knight_rises, intouchables, inside_out, shawshank_redemption]
fresh_tomatoes.open_movies_page(movies)
