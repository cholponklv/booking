from rest_framework import serializers



class CreateAdminSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length = 100)
    



class RecoverPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()





class VerificationCodeSerializer(serializers.Serializer):
    verification_code = serializers.CharField(max_length=6, min_length=6, required=True)



class NewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 255)
    confirm_password = serializers.CharField(max_length = 255)
    username = serializers.CharField(max_length = 255)
