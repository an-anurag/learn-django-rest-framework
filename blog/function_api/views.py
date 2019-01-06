from ..models import Post
from django.http import JsonResponse
from .serializers import PostSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def post_api_view(request):
    if request.method == 'GET':
        posts = Post.published.all()
        serializer = PostSerializer(instance=posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        parser = JSONParser()
        data = parser.parse(request)
        # use many = true only when you are posting multiple object
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def post_api_view_detail(request, id):
    try:
        instance = Post.objects.get(id=id)
    except instance.DoesNotExist as e:
        return JsonResponse({'error': 'Given post object not found'}, status=404)

    if request.method == 'GET':
        serializer = PostSerializer(instance=instance)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        parser = JSONParser()
        data = parser.parse(request)
        # use many = true only when you are posting multiple object
        serializer = PostSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        instance.delete()
        return JsonResponse({'data': 'post deleted successfully'}, status=204)
