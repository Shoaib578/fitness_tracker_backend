from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import ast

import json

from apis.models import User,FitnessSession
from django.contrib.auth.hashers import make_password, check_password
from apis.serializers import UserSerializer,FitnessSessionSerializer



# Sessions Related Views Start

@api_view(['POST'])
def insert_session(request):

    body = request.body.decode('utf-8')

    # Loading the string as a JSON object
    json_obj = ast.literal_eval(body)

    # Accessing JSON object keys and values
    session_type = json_obj['session_type']
    session_length = json_obj['session_length']
    strength = json_obj['stregth']
    created_by = json_obj['created_by']
    

    new_session = FitnessSession(workout_length= session_length,workout_type=session_type,strength=strength,created_by=created_by)
    new_session.save()
   
   
    response = {
        'status': 'inserted',
        'is_inserted':True,
    }
    
    return Response(response)


@api_view(['GET'])
def get_sessions(request):
    created_by = request.GET['created_by']
    print(created_by)
    all_sessions = FitnessSession.objects.all().filter(created_by=created_by)
   
    serializer = FitnessSessionSerializer(all_sessions,many=True)

    response = {
        "data":serializer.data
    }
    
    return Response(response)



@api_view(['GET'])
def get_session_by_id(request):
    id = request.GET['id']
    session = FitnessSession.objects.get(id=id)
    serializer = FitnessSessionSerializer(session,many=False)
    response = {
        "data":serializer.data
    }
    
    return Response(response)





@api_view(['DELETE'])
def delete_session_by_id(request):
    id = request.GET['id']
    session = FitnessSession.objects.get(id=id)
    session.delete()
    response = {
        "status":"deleted",
        "is_deleted":True
    }
    
    return Response(response)


@api_view(['POST'])
def update_session(request):

    body = request.body.decode('utf-8')

    # Loading the string as a JSON object
    json_obj = ast.literal_eval(body)

    # Accessing JSON object keys and values
    session_type = json_obj['session_type']
    session_length = json_obj['session_length']
    strength = json_obj['strength']
   
    id =  json_obj['id']
    session = FitnessSession.objects.get(id=id)
    session.workout_type = session_type
    session.workout_length = session_length
    session.strength = strength
    session.save()
   
   
    response = {
        'status': 'updated',
        'is_updated':True,
    }
    return Response(response)


# Sessions Related Views End



#User Related Views Start
@api_view(['POST'])
def signup_user(request):

    body = request.body.decode('utf-8')

    # Loading the string as a JSON object
    json_obj = ast.literal_eval(body)

    # Accessing JSON object keys and values
    email = json_obj['email']
    password = json_obj['password']
    username = json_obj['username']
    
    response = {}
    
    user = User.objects.filter(email=email).first()
    if user:
        response = {
            'status': 'email already registered',
            'is_registered':False,
        }
    else:
        response = {
            'status': 'registered successfully',
            'is_registered':True,
        }

        new_user = User(user_name=username, email=email, password=make_password(password))
        new_user.save()
   
   
    
    
    return Response(response)




@api_view(['POST'])
def signin_user(request):
    body = request.body.decode('utf-8')
    
    # Loading the string as a JSON object
    json_obj = ast.literal_eval(body)
    
    # Accessing JSON object keys and values
    email = json_obj['email']
    password = json_obj['password']
    response = {}
    user = User.objects.filter(email=email).first()
    if user and check_password(password, user.password):
        serializer = UserSerializer(user,many=False)
        response = {
            'is_logged_in':True,
            'user':serializer.data,
            'status':"logged in successfully"
        }
    else:
        response = {
            'is_logged_in':False,
            'status':"Invalid email or password"
        }
    
    return Response(response)


@api_view(['GET'])
def get_user_by_id(request):
    id = request.GET['id']
    user = User.objects.get(id=id)
    serializer = UserSerializer(user,many=False)
    response = {
        "data":serializer.data
    }
    
    return Response(response)

@api_view(['POST'])
def update_user(request):

    body = request.body.decode('utf-8')

    # Loading the string as a JSON object
    json_obj = ast.literal_eval(body)

    # Accessing JSON object keys and values
    email = json_obj['email']
    password = json_obj['password']
    username = json_obj['username']
    print(username)
    id = json_obj['id']

    
    response = {}
    
    user = User.objects.get(id=id)
    check_email = User.objects.filter(email=email).first()
    if user.email == email:
        response = {
                'status': 'updated successfully',
                'is_updated':True,
        }
        user.user_name = username
        user.email = email
        user.password = make_password(password)
        user.save()
    else:
        if check_email:
            response = {
               'status': 'email already registered',
                'is_updated':False,
            }
        else:
            response = {
              'status': 'updated successfully',
              'is_updated':True,
            }
            user.user_name = username
            user.email = email
            user.password = make_password(password)
            user.save()



    return Response(response)
#User Related Views End
