import stat
from urllib import response
from urllib.request import Request
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User,Group
from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from quickstart.serializer import *
from rest_framework.decorators import api_view,action
from quickstart.models import Test
from rest_framework import status
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be vivwed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request: HttpRequest, pk):

        user = get_object_or_404(User, id = pk)
        serializer = self.serializer_class(user, context={'request': request})
        
        return Response(serializer.data)
    
    
    def partial_update(self, request, pk=None):
        user = get_object_or_404(User, id = pk)
        
        serializer = self.serializer_class(user,data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            print("hot ",serializer.data)
            
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
    def list(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True,context={'request': request})
        print(serializer.data)
        return Response(serializer.data)

def foo(request: HttpRequest):
    return HttpResponse("foo")
    
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]    

    # __a = 'private'
    # a ='public'
    def create(self,request):
        print('request ',request.data)
        serializer = self.serializer_class(request.data,context={'request':request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.error_messages) 
    #     print(group, _)
    #     serializer = self.serializer_class(group,context={'request':request})
    #     return Response(serializer.data)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]    
    def create(self,request):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        print(request.data) 
        serializer.is_valid(raise_exception=True) 

        self.perform_create(serializer)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def partial_update(self, request, pk=None):
        user = get_object_or_404(User, id = pk)
        
        serializer = self.serializer_class(user,data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            print("hot ",serializer.data)
            
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
    
    def retrieve(self, request: HttpRequest, pk):
        return Response('hello')

    def list(self, request):
        
        print('luh',self.get_queryset())
        queryset = self.filter_queryset(self.get_queryset())
        # users = Test.objects.all()
        # print(query)
        # serializer = self.serializer_class(users, many=True,context={'request': request})
        # print(serializer.data)
        # return Response(serializer.data)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)





# @api_view(['GET',"POST"])
# def test(request):
#     if request.method == 'GET':
#         data = Test.objects.all()
#         serializer = TestSerializer(data,many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == "POST":
#         serializer = TestSerializer(data=request.data)
#         if serializer.is_valid():
#             test = serializer.validated_data
#             print(test)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error_messages)

@api_view(['DELETE','PATCH'])
def delete_test(request,id):
    print(id)
    """ GETTING INSTANCE """
    try:
        data = Test.objects.get(id = id)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if(request.method == 'DELETE'):
            print(data)
            data.delete()
            return Response(status=status.HTTP_200_OK)
    elif(request.method == 'PATCH'):
            print(data)
            serializers = TestSerializer(data,data=request.data)
            if(serializers.is_valid()):
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class Base: 
    _foo = 2
    def __init__(self): 
        self._foo = 222
  
        # Protected member 
        self._a = 2
        

# class TestViewSet(viewsets.ModelViewSet):
#     serializer_class = TestSerializer
#     # queryset = YourModel.objects.all()  

#     @action(detail=False, methods=['POST'])
#     def create_test(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # serializer.save()

#         return Response(serializer.data, status=201)

   
   
   
        
            
     