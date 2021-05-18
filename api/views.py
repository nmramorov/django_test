from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.serializers import UserSerializer, FriendshipSerializer
from api.models import User, Friendship


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=404)


@csrf_exempt
def receive(request, user_id):
    try:
        user_to_get = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user_to_get)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=404)


@csrf_exempt
def list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=404)


@csrf_exempt
def create_friendship(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FriendshipSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=404)


@csrf_exempt
def delete_friendship(request):
    try:
        data = JSONParser().parse(request)
        initiator_id = data['initiator_id']
        target_id = data['target_id']
        friendship_to_get = Friendship.objects.get(first_user=initiator_id, second_user=target_id)
    except Friendship.DoesNotExist:
        return HttpResponse(status=404)
    except KeyError:
        return HttpResponse(status=404)
    if request.method == 'DELETE':
        friendship_to_get.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)





