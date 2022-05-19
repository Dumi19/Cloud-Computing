from django.urls import path
from . import views

urlpatterns = [   
    # Movies ================================================================================================
    # /movies/{movie_id}/
    path('movies/<int:movie_id>/', views.MovieById.as_view(), name='Movie by ID'),
    # /movies/{movie_id}/images
    path('movies/<int:movie_id>/images', views.MovieImg.as_view(), name='Get movie mages by movie ID'),
    # /movies/{movie_id}/credits
    path('movies/<int:movie_id>/credits', views.MovieCrew.as_view(), name='Get movie crew'),
    # /movies/{movie_id}/similar
    path('movies/<int:movie_id>/similar', views.MovieSimilar.as_view(), name='Get similar movies'),
    # /movies/trending
    path('movies/trending', views.TrendingMovies.as_view(), name='Get trending movies'),
    # /search/movie/page/{page_number}/name/{movie_name}
    path('search/movie/page/<int:page_number>/name/<str:movie_name>', views.MovieByName.as_view(), name='Find movie by name')
]