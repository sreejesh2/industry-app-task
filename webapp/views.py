from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import logout as signout
from decouple import config
from django.http import HttpResponseRedirect
import json
# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        auth0_user = user.social_auth.get(provider='auth0')

        user_data = {
            'user_id': auth0_user.uid,
            'pro_pic': auth0_user.extra_data['picture']
        }
        context = {
            'user_data': json.dumps(user_data, indent=4),
            'auth0_user': auth0_user
        }
        return render(request, 'profile.html', context)

def logout(request,*args, **kwargs):
    signout(request)
    domain=config('APP_DOMAIN')
    client_id=config('APP_CLIENT_ID')
    return_to='http://localhost:8000'
    return HttpResponseRedirect(f"http://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")