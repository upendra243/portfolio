from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from home.models import MySkills
from api.serializers import MySkillSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


from rest_framework import status

# Create your views here.


def skill_list(request):
    """
    List all skills and create new skills.
    """

    if request.method == 'GET':
        skills = MySkills.objects.all()
        serializer = MySkillSerializer(skills, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # steps
        data = JSONParser().parse(request)
        serializer = MySkillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



def skill_detail(request, pk):
    """
    Retrive, update or delete a skill
    """

    try:
        skill = MySkills.objects.get(pk=pk)
    except MySkills.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MySkillSerializer(skill)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MySkillSerializer(skill, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        skill.delete()
        return HttpResponse(status=204)






from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def skill_list_v2(request):
    """
    List all skills, or create a new skill.
    """
    if request.method == 'GET':
        snippets = MySkills.objects.all()
        serializer = MySkillSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MySkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def skill_details_v2(request, pk):
    """
    Retrieve, update or delete a skill.
    """
    try:
        skill = MySkills.objects.get(pk=pk)
    except MySkills.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MySkillSerializer(skill)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MySkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class SkillList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        skill = MySkills.objects.all()
        serializer = MySkillSerializer(skill, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MySkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return MySkills.objects.get(pk=pk)
        except MySkills.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MySkillSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MySkillSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




from rest_framework import mixins
from rest_framework import generics


class SkillListMixing(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):


    queryset = MySkills.objects.all()
    serializer_class = MySkillSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class SkillDetailMixing(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = MySkills.objects.all()
    serializer_class = MySkillSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



from rest_framework import generics

class SkillListGeneric(generics.ListCreateAPIView):
    queryset = MySkills.objects.all()
    serializer_class = MySkillSerializer

class SkillDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = MySkills.objects.all()
    serializer_class = MySkillSerializer


from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    apis = {
        'skills': reverse('skill-list-v2', request=request, format=format),
        'users': reverse('user-list', request=request, format=format)
    }
    return Response(apis)

























