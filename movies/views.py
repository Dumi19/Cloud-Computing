from django.conf import settings
from django.template import loader
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

import requests
import json

API_KEY = "7618a9d10c1f79db29ec1cac107ac3bc"
API_URL = "https://api.themoviedb.org/3/"



class RegisterUser(APIView):
    permission_classes = [AllowAny]
    # Register the user

    def put(self, request):
        json_data = json.loads(request.body)
        try:
            username = json_data['username']
            email = json_data['email']
            password = json_data['password']
            if User.objects.filter(username=username).exists():
                existing_user = User.objects.filter(username=username)
                return HttpResponse("User with username " + str(existing_user) + " already exists", status=403)
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                return HttpResponse(json.dumps({"success": True}), status=201)
        except KeyError:
            return HttpResponse("JSON format is incorrect. Please use {username:'value', email:'value', password:'value'}", status=400)

class TrendingMovies(APIView):
    
    def get(self, request):
        parameters = {'api_key': API_KEY}
        api_path = "trending/movie/week"
        request = API_URL + api_path
        request_answer = requests.get(url=request, params=parameters)
        if(request_answer.ok):
            return HttpResponse(request_answer, status=status.HTTP_200_OK)
        else:
            return HttpResponse(request_answer, status=404)


class MovieById(APIView):
    
    def get(self, request, movie_id):
        request_answer = getMovieById(movie_id)
        if(request_answer.ok):
            return HttpResponse(request_answer)
        else:
            return HttpResponse(request_answer, status=404)


class MovieCrew(APIView):
    
    def get(self, request, movie_id):
        parameters = {'api_key': API_KEY}
        api_path = "movie/" + str(movie_id) + "/credits"
        request = API_URL + api_path
        request_answer = requests.get(url=request, params=parameters)
        if(request_answer.ok):
            return HttpResponse(request_answer)
        else:
            return HttpResponse(request_answer, status=404)


class MovieByName(APIView):
    
    def get(self, request, page_number, movie_name):
        parameters = {"api_key": API_KEY,
                      "page": page_number, "query": movie_name}
        request = API_URL + "search/movie"
        request_answer = requests.get(request, params=parameters)
        if(request_answer.ok):
            return HttpResponse(request_answer)
        else:
            return HttpResponse(request_answer, status=404)


class MovieImg(APIView):
    
    def get(self, request, movie_id):
        parameters = {"api_key": API_KEY}
        request = API_URL + "movie/" + str(movie_id) + "/images"
        request_answer = requests.get(request, params=parameters)
        if(request_answer.ok):
            return HttpResponse(request_answer)
        else:
            return HttpResponse(request_answer, status=404)


class MovieSimilar(APIView):
    
    def get(self, request, movie_id):
        parameters = {"api_key": API_KEY}
        request = API_URL + "movie/" + str(movie_id) + "/similar"
        request_answer = requests.get(request, params=parameters)
        if(request_answer.ok):
            return HttpResponse(request_answer)
        else:
            return HttpResponse(request_answer, status=404)

def getMovieById(movie_id):
    parameters = {'api_key': API_KEY}
    api_path = "movie/" + str(movie_id)
    newRequest = API_URL + api_path
    request_answer = requests.get(url=newRequest, params=parameters)
    return request_answer

class MovieReviews(APIView):
     def get(self, request, movie_id):
        parameters = {"api_key": API_KEY}
        request = API_URL + "movie/" + str(movie_id) + "/reviews"
        request_answer = requests.get(request, params=parameters)
        if(request_answer.ok):
            return HttpResponse(request_answer)
        else:
            return HttpResponse(request_answer, status=404)
