from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import SelectedTweet, Setup, TrendingTopics, Location
from tweets.api_twitter.src.initialize_api import InitializeTwitterApi


class SelectedTweetsListView(APIView):
    def __init__(self):
        self.serializer = None

    def get(self, request, format=None):
        queryset = SelectedTweet.objects.all()
        self.serializer = SelectedTweetSerializer(queryset, many=True)
        return Response(self.serializer.data)

    def post(self, data):
        for i in data:
            serializer = SelectedTweetSerializer(data={'text':i})
            if serializer.is_valid():
                serializer.save()

    def delete(self):
        queryset = SelectedTweet.objects.all()
        self.serializer = SelectedTweetSerializer(queryset, many=True)

        for i in self.serializer.data:
            pk = dict(i)
            element = SelectedTweet.objects.get(pk=pk['id'])
            element.delete()


class TrendingTopicsView(APIView):
    def __init__(self, *args, **kwargs):
        self.delete()
        self.post()

    def get(self, request, format=None):
        queryset = TrendingTopics.objects.all()
        serializer = TredingTopicsSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def delete(self):
        queryset = TrendingTopics.objects.all()
        serializer = TredingTopicsSerializer(queryset, many=True)

        for i in serializer.data:
            pk = dict(i)
            element = TrendingTopics.objects.get(pk=pk['id'])
            element.delete()

    def post(self):
        result = InitializeTwitterApi().init_read_trending_topics()
        for i in result:
            serializer = TredingTopicsSerializer(data=i)
            if serializer.is_valid():
                serializer.save()


class SetupView(generics.ListCreateAPIView):
    queryset = Setup.objects.all()
    serializer_class = SetupSerializer
 

class SetupDetail(APIView):
    def get(self, request, pk, format=None):
        setup = Setup.objects.get(pk=1)
        serializer = SetupSerializer(setup)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        #For each configuration update, a twitter API is started.
        
        setup = Setup.objects.get(pk=1)
        serializer = SetupSerializer(setup, data=request.data)
        if serializer.is_valid():
            serializer.save()

        term = serializer.data['term']
        limit = serializer.data['limit']
        init = InitializeTwitterApi()
        init.init_read_api(term, limit)
        
        SelectedTweetsListView().delete()
        SelectedTweetsListView().post(init.result)

        LocationView().delete()
        LocationView().post(init.geo_location)

        return Response(serializer.data)    


class LocationView(APIView):
    def get(self, request, format=None):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)

        for i in serializer.data:
            pk = dict(i)
            element = Location.objects.get(pk=pk['id'])
            element.delete()

    def post(self, datas):
        for i in datas:
            serializer = LocationSerializer(data={'latitude':i[0], 'longitude':i[1]})               
            if serializer.is_valid():
                serializer.save()