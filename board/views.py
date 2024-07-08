from django.shortcuts import render
from rest_framework.views import APIView

from .models import Board, Comment
from .serializers import BoardSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class BoardList(APIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)