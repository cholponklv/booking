from django.shortcuts import render
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from .serializers import CreateAdminSerializer, RecoverPasswordSerializer, VerificationCodeSerializer, NewPasswordSerializer
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
import random
from django.conf import settings
from django.core.mail import send_mail
import smtplib
# Create your views here.


class CreateAdminView(APIView):
    @extend_schema(
        description="create_admin",
        request= CreateAdminSerializer,
        responses={200: {"message": "admin is created   "}}
        )
    
    def post(self, request):
        serializer = CreateAdminSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            password_non = serializer.validated_data['password']
            phone_number = serializer.validated_data['phone_number']
            password = make_password(password_non)

            User.objects.create(username = username, name = name, password = password, email = email, phone_number = phone_number, is_staff = True)

            return Response({"message": "admin is created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SendToRecoverPassword(APIView):
    permission_classes = []
    @extend_schema(
        description=" send Recover_token Password",
        request= RecoverPasswordSerializer,
        responses={200: {"message": "code successfully sended."}}
        )

    def post(self, request):
        serializer = RecoverPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']


            
            user = User.objects.get(email = email)
            username = user.username

            verification_code = ''.join([str(random.randint(0, 9)) for i in range(6)])
            user.email_token = verification_code
            user.save()
        
            subject = 'Восстановление пароля'
            message = f'Здравствуйте, {username}!\n\nВаш код для восстановле пароля: {verification_code}\n\nС уважением,\nВаша команда.'
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            
            try:

                send_mail(subject, message, from_email, to_email)
                return Response({'message': 'Код отправлен на указанный адрес.'}, status=status.HTTP_200_OK)
            except smtplib.SMTPException:
                return Response({'message': 'Произошла ошибка при отправке письма.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'message': 'Неверные данные.'}, status=status.HTTP_400_BAD_REQUEST)
        






class VerificationPasswordCodeAPIView(APIView):
    permission_classes = []
    @extend_schema(
        description="Recover Password",
        request= VerificationCodeSerializer,
        responses={200: {"message": "code successfully checked."}}
        )

    def post(self, request):
        serializer = VerificationCodeSerializer(data=request.data)
        if serializer.is_valid():
            verification_code = serializer.validated_data['verification_code']
            user = User.objects.filter(email_token=verification_code).first()
            if user:
                return Response({'message': ' code is valid.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        





class NewPasswordView(APIView):
    permission_classes = []
    @extend_schema(
        description="new Password",
        request= NewPasswordSerializer,
        responses={200: {"message": "password successfully changed."}}
        )
    def post(self, request):
        serializer = NewPasswordSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            confirm_password = serializer.validated_data['confirm_password']
            username = serializer.validated_data['username']

            user = User.objects.get(username=username)

            if password == confirm_password:
                user.password = make_password(password)
                user.save()
                return Response({'message': ' PASSWORD is changed.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'mistake.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    

