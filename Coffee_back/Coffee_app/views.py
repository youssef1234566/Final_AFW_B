import json
import hashlib

from django.shortcuts import render
from rest_framework.views import APIView
from Coffee_app.models import *
from rest_framework import status
from rest_framework.response import Response



# Create your views here

class Sign_Up(APIView):
    def post(self , request ,*args , **kwargs):
        try:
            json_obj = json.dumps(request.data)
            data = json.loads(json_obj)

            try:
                exist = User.objects.get(User_Email = data["User_Email"])
                userExists = True
            except Exception:
                userExists = False
                
            if userExists == False:    
                user_name = data["User_Name"]
                user_email = data["User_Email"]
                user_password_unhashed= data["User_Password"]
                user_details = data["User_Details"]
                # details = json.loads(user_details)
                details_dumped = json.dumps(user_details)
                user_orders = 0
                
                md5_hash = hashlib.md5()
                md5_hash.update(user_password_unhashed.encode('utf-8'))
                user_password = md5_hash.hexdigest()
                
                
                user = User(
                    User_Name = user_name,
                    User_Email=user_email,
                    User_Password=user_password,
                    User_Details=details_dumped,
                    User_Orders=user_orders
                )
                
                user.save()
                return Response('User Created', status=status.HTTP_201_CREATED)
            elif userExists == True:
                return Response("This email is already in use.", status=status.HTTP_409_CONFLICT)
        except Exception as e:
            return Response(f'An Error Occured: {e}', status=status.HTTP_400_BAD_REQUEST)
        
        
class Sign_In(APIView):
    def post(self , request ,*args , **kwargs):
        
        try:
        
            json_obj = json.dumps(request.data)
            data = json.loads(json_obj)
            
            user_email = data["User_Email"]
            user_password_entered = data["User_Password"]
            
            md5_hash = hashlib.md5()
            md5_hash.update(user_password_entered.encode('utf-8'))
            user_password_hashed = md5_hash.hexdigest()
            
            
            try:
                user_instance = User.objects.get(User_Email = user_email)
                user_password = user_instance.User_Password
            except Exception as e:
                return Response("Invalid Email", status=status.HTTP_401_UNAUTHORIZED)
            

            
            
            if user_password == user_password_hashed:
                
                user_logIn_status = True
                return Response({"LogIn_Status" : user_logIn_status}, status=status.HTTP_201_CREATED)
            
            else:
                user_logIn_status = False
                return Response({"Log In Status" : user_logIn_status}, status=status.HTTP_401_UNAUTHORIZED)
            
            
        except Exception as e:
            return Response(f'Error in Logging In : {e}', status=status.HTTP_400_BAD_REQUEST)
        
        
class Profile(APIView):
    def post(self,request, *args,**kwargs):
        
        try:
            json_obj = json.dumps(request.data)
            data = json.loads(json_obj)
            
            user_email = data["User_Email"]
            
            user_ins = User.objects.get(User_Email = user_email)
            
            details = json.loads(user_ins.User_Details)
            
            return Response({"User_Email" : user_email, "User_Orders" : user_ins.User_Orders, "User_Details" : details, "User_Name" : user_ins.User_Name}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(f"An Error Occured {e}", status=status.HTTP_400_BAD_REQUEST)
        
        
class Products(APIView):
    def get(self,request, *args,**kwargs):
        products = Product.objects.all().values()
        print(products)
        return Response(products, status=status.HTTP_200_OK)
