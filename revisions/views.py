from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from revisions.models import Revision
from revisions.serializers import RevisionSerializer, UserSerializer


class RevisionViewSet(viewsets.ModelViewSet):
    queryset = Revision.objects.all()
    serializer_class = RevisionSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
