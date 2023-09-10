from rest_framework import serializers
from watchlist_app.models import *


class MovieSerializer(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ['name']

    def get_len_name(self, object):
        length = len(object.name)
        return length
        #field validation 
    def validate_name(self, value):
        if len(value) <2 :
            raise serializers.ValidationError('value is too short')
        return value
    # object validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description shoud not be same")




# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance