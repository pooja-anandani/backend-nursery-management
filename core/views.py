from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from .models import User
from rest_framework import status
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from backend import custom_status_codes, responses
from .serializers import UserSignUpSerializer, UserSerializer, UserSignInSerializer


# USER SIGN UP
class UserSignup(APIView):
    def post(self, requests):
        requests.data['email'] = requests.data['email'].lower()
        serializer = UserSignUpSerializer(data=requests.data)
        if not serializer.is_valid():
            return Response(responses.generate_failure_response(custom_status_codes.USERS_SIGN_UP_FAILURE,
                                                                payload=serializer.errors),
                            status=status.HTTP_400_BAD_REQUEST)
        # Check if email address already exists
        if User.objects.filter(email=requests.data['email']).exists():
            return Response(
                responses.generate_failure_response(
                    custom_status_codes.USER_ACCOUNT_ALREADY_EXISTS,
                    payload=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=requests.data['username'], email=requests.data['email'],
                                        password=requests.data['password'], last_login=timezone.now())

        my_group = Group.objects.get(name=requests.data['group'])
        my_group.user_set.add(user)
        token = Token.objects.get(user_id=user.id)

        user_serializer = UserSerializer(user)

        return Response(responses.generate_success_response(custom_status_codes.USERS_SIGN_UP_SUCCESS,
                                                            payload={'user': user_serializer.data, 'token': token.key}),
                        status=status.HTTP_200_OK)


# USER LOGIN
class UserSignIn(APIView):
    def post(self, requests):

        requests.data['email'] = requests.data['email'].lower()

        serializer = UserSignInSerializer(data=requests.data)
        if not serializer.is_valid():
            return Response(
                responses.generate_failure_response(
                    custom_status_codes.USERS_SIGN_IN_FAILURE,
                    payload=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=requests.data['email'])

            if user.is_deleted:
                user.is_deleted = False
                user.save()
            user = authenticate(
                email=requests.data['email'], password=requests.data['password'])

            if user is not None:
                login(requests, user)
                token = Token.objects.get_or_create(user_id=user.id)
                user_serializer = UserSerializer(user)
                return Response(responses.generate_success_response(custom_status_codes.USERS_SIGN_IN_SUCCESS,
                                                                    payload={'user': user_serializer.data,
                                                                             'token': token[0].key}),
                                status=status.HTTP_200_OK)
            else:
                return Response(
                    responses.generate_failure_response(
                        custom_status_codes.USERS_SIGN_IN_FAILURE, payload={}),
                    status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response(
                responses.generate_failure_response(custom_status_codes.USERS_SIGN_IN_FAILURE,
                                                    payload={}), status=status.HTTP_400_BAD_REQUEST)
