from django.contrib.auth.models import User
from rest_framework import serializers

from revisions.models import Revision


class RevisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Revision
        fields = ['id', 'shop', 'rev_date', 'schema', 'status']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
