from rest_framework import generics, mixins
from django.db.models import Q
from app.models import MedicinePost
from . serializers import MedicinePostSerializer, UserSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class MedicinePostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	pass
	lookup_field = 'pk'
	serializer_class = MedicinePostSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		qs = MedicinePost.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(title_icontains=query)|Q(content_icontains=query)).distinct()
		return qs

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class MedicinePostRudView(generics.RetrieveUpdateDestroyAPIView):
	pass
	lookup_field = 'pk'
	serializer_class = MedicinePostSerializer

	def get_queryset(self):
		return MedicinePost.objects.all()


class CreateUserView(generics.CreateAPIView):
	model = get_user_model()
	permission_classes=(AllowAny,)
	serializer_class = UserSerializer


class LoginUserView(APIView):
	permission_classes = (AllowAny,)
	serializer_class = UserLoginSerializer
	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)