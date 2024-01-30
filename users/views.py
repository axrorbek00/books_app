from django.shortcuts import render
from .models import UserModel
from .serializers import UserRegisterSerializer, UserProfileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class ProfileView(APIView):
    # serializer_class = UserProfileSerializer
    # queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        qs = UserModel.objects.all().get(username=request.user)
        serializer = UserProfileSerializer(qs)
        return Response({
            'profile': serializer.data,
            'order_history': 'order history data'
        })

    def patch(self, request):
        serializer = UserProfileSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
