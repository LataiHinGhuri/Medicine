from rest_framework import serializers
from rest_framework.serializers import CharField
from app.models import MedicinePost
from django.contrib.auth import get_user_model

# medicine create edit
class MedicinePostSerializer(serializers.ModelSerializer):
	class Meta:
		model = MedicinePost
		fields =[
			'pk',
			'user',
			'name',
			'description',
			'time',
			'timedif',
		]

#Register Serializer
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
		]
		extra_kwargs ={"password":{"write_only":True}}

	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		user_obj = User(
			username = username,
			email = email
		)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data

# Login Serializer 
class UserLoginSerializer(serializers.ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField()

	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'token',
		]
		extra_kwargs ={"password":{"write_only":True}}

	
