from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response


class CommonViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_action_class = {}

    def get_serializer_class(self):
        if self.action == "list":
            return self.serializer_action_class['list']
        elif self.action == "retrieve":
            return self.serializer_action_class['retrieve']

    def list(self, request):
        serializer_class = self.get_serializer_class()
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"response": serializer.data}, HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        queryset = get_object_or_404(self.get_queryset(), pk=kwargs.get("pk"))
        serializer = self.get_serializer(queryset)
        return Response({"response": serializer.data}, HTTP_200_OK)
