
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from django.contrib.auth import authenticate
import random
from rest_framework.authtoken.models import Token

# Create your views here.

class UserViewSet(generics.CreateAPIView, generics.UpdateAPIView):



    def get(self,request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and username:

            user = authenticate(username=username, password=password)
            if user:

                token, created  = Token.objects.get_or_create(user=user)

                return Response({'success': True, 'token':token.key})
            else:
                return Response({'success': False, 'Message': 'Incorrect username or password'})
        else:
            return Response({'success':False, 'Message': 'All fields required'})



    def post(self,request, *args, **kwargs):
        if not User.objects.filter(username= request.data.get('name')):
            user ={}
            user['username'] = request.data.get('name')
            password = request.data.get('password')
            user['email'] = request.data.get('email')
            user['is_active'] = True
            details = {}
            details['address'] = request.data.get('address')
            details['phone'] = request.data.get('phone_number')
            details['company_name'] = request.data.get('company_name')

            device_id = request.data.get('device_id')
            print(device_id)

            otp_obj = [str(random.randint(0, 9)) for i in range(6)]
            details['otp'] = ''.join(otp_obj)

            user_obj = User.objects.create(**user)
            user_obj.set_password(password)
            user_obj.save()
            device_obj = DeviceDetail.objects.create(device_id=device_id,device_token=device_id)
            details['user'] = user_obj
            details['device'] = device_obj
            detail_obj = UserDetail.objects.create(**details)
            detail_obj.save()

            return Response({'success': True,'Message': 'Detail Saved'})
        else:
            return Response({'success': False,'Message': 'Username already exists'})




