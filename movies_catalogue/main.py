from flask import Flask, render_template, request, url_for

import tmdb_client
import requests


def default_list(list_of_movies):
    movie_category = ['popular','upcoming','now_playing','top_rated']
    if list_of_movies in movie_category:
        None
    else:
        list_of_movies = 'popular'

    return list_of_movies

def select_list(selected_list):
    default_class = "btn btn-outline-info"
    buttons = [default_class,default_class,default_class,default_class]
    if selected_list == 'popular':
        buttons[0] = "btn btn-primary"
    elif selected_list == 'upcoming':
        buttons[1] = "btn btn-primary"
    elif selected_list == 'now_playing':
        buttons[2] = "btn btn-primary"
    elif selected_list == 'top_rated':
        buttons[3] = "btn btn-primary"
    return buttons

app = Flask(__name__)


@app.route('/')
def homepage():
    selected_list = default_list(request.args.get('list_movies',"popular"))
    movies = tmdb_client.get_movies(how_many=5,list_movies=selected_list)
    buttons = select_list(selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, buttons=buttons)


@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    movie = tmdb_client.get_details(movie_id)
    actors = tmdb_client.get_credits(movie_id)["cast"][:4]
    return render_template("details.html", movie=movie, actors=actors)


@app.route('/search')
def search():
    search_query = request.args.get("query", "")
    if search_query:
        movies = tmdb_client.search_movies(search_query=search_query)["results"][:4]
    else:
        movies = []
    return render_template("search.html", movies=movies, search_query=search_query)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.context_processor
def genre():
    def genre_list(genres):
        types = ""
        for i in genres:
            types +=f"{i['name']}, "
        return types
    return {"genre_list": genre_list}

if __name__ == "__main__":
    app.run(debug=True)
