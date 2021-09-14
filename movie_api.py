from movie_model import MovieModel
import requests

def callMovieApi(page=1):
    uri = f"https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20"
    response = requests.get(uri)

    responseDict = response.json()
    movies = responseDict["data"]["movies"]
    print(movies)
    return convert_model(movies)

def convert_model(movies):
    list = []

    for movie in movies:
        movie_model = MovieModel(movie["title"], movie["rating"], movie["small_cover_image"], movie["summary"] )
        list.append(movie_model)

    print(list)
    return list