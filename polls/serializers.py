from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ('question_text', 'id', 'pub_date')


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(
#         many=True, view_name='snippet-detail', read_only=True)

#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'snippets')

# class UserLoginSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username', 'password')
