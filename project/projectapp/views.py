from projectapp.models import Post
from projectapp.serializers import PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from rest_framework import generics,permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User




class PostList(APIView):
 
    

     def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostLogin(APIView):
     
      # This is login api
      def post(self,request, format=None):
          print("Checkpoint 1")
          serializer = PostSerializer(data=request.data)
          mail = request.Post['mail']
          print("Checkpoint 2 mail",mail)
          password = request.Post['password']
          print("Checkpoint 3 password==",password)

          # Write your code for check email and      passsssssssssword exissssssssssssssssssssssssssssssssssssssssssssssssssssst in db
          user = Post.objects.get(mail='suresh@gmail.com',password='123456')
         
          if user is not None:
              #login(mail, password)
          
              return Response({"sucessfull","true"}, status=status.HTTP_201_CREATED)
          else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
     
      # This is login api
      def post(self,request, format=None):
          print("Checkpoint 1")
          serializer = PostSerializer(data=request.data)
          email = request.data['mail']
          print("Checkpoint 2 l",email)
          passwd = request.data['password']
          print("Checkpoint 3 password==",passwd)

          # Write your code for check email sssst in db
          try:
              user = Post.objects.get(mail=email)
         
              if user is not None:
                  if user.password==passwd:
                      print("Login successfull: ",)

                      #token

                      return Response({"sucess":"true","message":"Loging successfull"}, status=status.HTTP_200_OK)
                  else:
                      return Response({"sucess":"false","message":"Login not successfull"}, status=status.HTTP_400_BAD_REQUEST)

              else:
                  return Response({"sucess":"false","message":"Login not successfull"}, status=status.HTTP_400_BAD_REQUEST)

          except:
              return Response({"sucess":"false","message":"Mail does not exist"}, status=status.HTTP_400_BAD_REQUEST)








          

              
                 
          


