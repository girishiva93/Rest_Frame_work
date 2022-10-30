from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('watchlist', )

class WatchListSerializer(serializers.ModelSerializer):
    # foreign key ma related_name ma j define gareko xa tei hunu parxa object name
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__" # yesma all fields model ko include gareko xa
        

class StreamPlatformSerializer(serializers.ModelSerializer):
    # model ko related_name ma dako name lai use garne - watchlist
    # one StreamPlatForm has Many Movies or youtube can have many movies
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    # Returning title or movie name only from the watchList
    # watchlist = serializers.StringRelatedField(many=True)
    
    # yesle primary key matra return garxa
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only = True,
    #     view_name = 'movie-details',
    # )
    
    # HyperLinkedIdentityField -> yesle tei link for watchLink foreign key banauxa
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"

# HyperLinkedModelSerializer
# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):

#     watchlist = WatchListSerializer(many=True, read_only=True)

#     class Meta:
#         model = StreamPlatform
#         fields = "__all__"



##################################################
# Learning the Serilizers.models here
#################################################

# serializers.Model type
# class MovieSerializer(serializers.ModelSerializer):

#     ##################
#     # yedi model ma kei kura haru calclulate garnu xa vani hami le following way ma garrxam
#     #################
#     len_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = "__all__" # yesma all fields model ko include gareko xa

#         # chaine kura haru define garnu
#         # paryo vani filed ma model ko field kun
#         #    kun field chaixa tyo kura hahru matra define garnu parxa
#         #############
#         # fields = ['id', 'name', 'description' ]
#         ############
        
#         # yedi hami sanga 20 field xa ra malai 10 wa 18 ko euta field chaidaina
#         # vani we use exclude field
#         ################################
#         # exclude=['active']
#         ################################
        
        
#     ##################
#     # yedi model ma kei kura haru calclulate garnu xa vani hami le following way ma garrxam
#     #################
#     def get_len_name(self, object):
#         length = len(object.name)
#         return length
    
#     #  Field Level validations
#     def validate_name(self, value):
#         if len(value)<2:
#             raise serializers.ValidationError("Name is too Short!")
#         # else:
#         #     return value
#         return value
        
#     #  Object Level validations
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description should not be same")
#         return data

# serializers.Serializer type

# best way to validate Field better than line number 28
# def name_length(value):
#         if len(value)<2:
#             raise serializers.ValidationError("Name is too Short!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     # name = serializers.CharField()
#     name = serializers.CharField(validators = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#        return Movie.objects.create(**validated_data)
   
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Movie` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    #  Field Level validations
    # def validate_name(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too Short!")
    #     # else:
    #     #     return value
    #     return value
        
    #  Object Level validations
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should not be same")
    #     return data