from django.test import TestCase
from django.test import Client
# Create your tests here.

class ViewsTestCase(TestCase):
    client = Client()

    example_movie_id = 414906
    example_movie_name = "Django"

    def test_getMovieImages(self):
        response = self.client.get(
            '/movies/' + str(self.example_movie_id) + "/images")
        self.assertEqual(response.status_code, 200)

    def test_getMovieCrew(self):
        response = self.client.get(
            '/movies/' + str(self.example_movie_id) + "/credits")
        self.assertEqual(response.status_code, 200)

    def test_getSimilarMovies(self):
        response = self.client.get(
            '/movies/' + str(self.example_movie_id) + "/similar")
        self.assertEqual(response.status_code, 200)

    def test_getTrendingMovies(self):
        response = self.client.get(
            '/movies/trending'
        )
        self.assertEqual(response.status_code, 200)

    def test_getMoviesByName(self):
        response = self.client.get(
            '/search/movie/page/1/name/' + str(self.example_movie_id))
        self.assertEqual(response.status_code, 200)