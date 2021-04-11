import requests


def get_api(endpoint):
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYjdlZTA5NTU2NTk0M2Y3NzI5N2VhZTEzODRkMTQ0OCIsInN1YiI6IjYwNTM1NWI4YTFkMzMyMDA3NWU1MTQyZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lL00YloqDKd8p0iPC_ejm8RH9zJrduBVhbOEsGf7xKg"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_list_movies(list_movies):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_movies}"
    response = get_api(endpoint)
    return response


def get_details(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = get_api(endpoint)
    return response


def get_credits(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = get_api(endpoint)
    return response


def search_movies(search_query):
    base_url = "https://api.themoviedb.org/3/"
    endpoint = f"{base_url}search/movie/?query={search_query}"
    response = get_api(endpoint)
    return response


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_movies="popular"):
    data = get_list_movies(list_movies)
    return data['results'][:how_many]
