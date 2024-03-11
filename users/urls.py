from django.urls import include, path

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # registration url for new accounts
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), 
]