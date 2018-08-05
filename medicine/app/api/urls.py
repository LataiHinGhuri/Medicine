from django.conf.urls import url

from . views import MedicinePostRudView, MedicinePostAPIView, CreateUserView, LoginUserView
app_name='app'

urlpatterns=[
	# Medicine list and Create new medicine url = localhost:8000/api/app
	url(r'^app/$',MedicinePostAPIView.as_view(), name='post-create'),

	# Register new user  url = localhost:8000/api/register
	url(r'^register/$',CreateUserView.as_view(), name='register'),
	
	# Login Test user  url = localhost:8000/api/login
	url(r'^login/$',LoginUserView.as_view(), name='login'),
	
	# Medicine Post Edit and Delete using post id url = localhost:8000/api/app/id 
	url(r'^app/(?P<pk>\d+)/$',MedicinePostRudView.as_view(), name='post-rud'),
]