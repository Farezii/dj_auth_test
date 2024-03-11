from django.urls import include, path

from users.views import GoogleLogin

urlpatterns = [
    # for allauth, need to check if its needed for api
    path('accounts/', include('allauth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # registration url for new accounts
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]

urlpatterns += [
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
]
# Obtain token via the following link
# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=<CALLBACK_URL_YOU_SET_ON_GOOGLE>&prompt=consent&response_type=code&client_id=<YOUR CLIENT ID>&scope=openid%20email%20profile&access_type=offline
