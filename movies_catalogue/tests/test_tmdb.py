import tmdb_client
from unittest.mock import Mock
import pytest


def mocks(mock_value):
    requests_mock = Mock()

    response = requests_mock.return_value

    response.json.return_value = mock_value

    return requests_mock


def test_get_single_movie(monkeypatch):
    mock_movie = ['Movie 1']

    requests_mock = mocks(mock_movie)
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie = tmdb_client.get_details(movie_id=399566)

    assert movie == mock_movie


def test_get_movie_images(monkeypatch):
    mock_image = 'https://image.tmdb.org/t/p/w780/inJjDhCjfhh3RtrJWBmmDqeuSYC.jpg'

    requests_mock = mocks(mock_image)

    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    image = tmdb_client.get_poster_url(poster_api_path="inJjDhCjfhh3RtrJWBmmDqeuSYC.jpg", size="w780")

    assert image == mock_image


def test_get_single_movie_cast(monkeypatch):
    mock_cast = {"actor": "actor"}

    requests_mock = mocks(mock_cast)

    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    cast = tmdb_client.get_credits(movie_id=399566)

    assert cast == mock_cast
