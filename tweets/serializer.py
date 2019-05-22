from rest_framework import serializers
from .models import SelectedTweet, Setup, TrendingTopics, Location


class SelectedTweetSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(SelectedTweetSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = SelectedTweet
        fields = ('id', 'text')


class SetupSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(SetupSerializer, self).__init__(many=many, *args, **kwargs)
        
    class Meta:
        model = Setup
        fields = ('id', 'term', 'limit')


class TredingTopicsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(TredingTopicsSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:    
        model = TrendingTopics
        fields = ('id', 'text')

class LocationSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(LocationSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude')