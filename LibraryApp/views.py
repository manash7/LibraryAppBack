from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


from LibraryApp.models import customusers,Books
from LibraryApp.serializers import BooksSerializers
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
# @csrf_exempt
# def usersApi(request,id=0):
   
#     if request.method=='POST':
#         users_data=JSONParser().parse(request)
#         users_serializers=UsersSerializers(data=users_data)
#         if users_serializers.is_valid() :
#             users_serializers.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)




class LoginUser(APIView):
    def post(self,request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
        # A backend authenticated the credentials
                refresh = RefreshToken.for_user(user)
            else:
                pass
                return Response({
                    "SUCCESS":"True",
                    "DATA":"User Added Successfully",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                },
                    status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error":str(e),
            },
            status=status.HTTP_400_BAD_REQUEST)
        

class RegisterUser(APIView):
    def post(self,request):
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        user = User.objects.create_user(username=email,email=email,password=password)
        user.set_password(password)
        user.save()
        customusers.objects.create(first=first_name,last=last_name,user=user)
        return Response({
                "SUCCESS":"True",
                "DATA":"User Added Successfully"
            },
            status=status.HTTP_200_OK)

class ListBooks(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [BasicAuthentication]
    def get(self, request,pk=None):
        try:      
            if pk:
                queryset=Books.objects.get(id=pk)
                serializer = BooksSerializers(queryset)
            else:    
                queryset = Books.objects.all()
                serializer = BooksSerializers(queryset,many=True)
            return Response({
                "data":serializer.data
            },
            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error":str(e),
            },
            status=status.HTTP_400_BAD_REQUEST)
            

    def post(self, request):
        
        try:
            title = request.data.get('title')
            author= request.data.get('author')
            category = request.data.get('category')
            price = request.data.get('price')
            dic ={"title":title,"author":author,"category":category,"price":price}
            serializer = BooksSerializers(data=dic)
            if serializer.is_valid():
                serializer.save()

            return Response({
                "SUCCESS":True,
                "data":serializer.data,
                "DATA":"Books Added Successfully !!"
            },
            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error':str(e),
            },
            status=status.HTTP_400_BAD_REQUEST)   

    def patch(self, request, format=None):        
        id = request.data.get('id',None)
        title = request.data.get('title',None)
        author= request.data.get('author',None)
        category = request.data.get('category',None)
        price = request.data.get('price',None)
        try:
            if id:
                obj = Books.objects.get(id=id)
            dic ={"title":title,"author":author,"category":category,"price":price}
            serializer = BooksSerializers(obj,data=dic,partial=True)
            if serializer.is_valid():
                serializer.save()

            return Response({
                "SUCCESS":True,
                "data":serializer.data,
                "DATA":"Books Updated Successfully !!"
            },
            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error':str(e),
            },
            status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request,pk=None, format=None):
        id = pk
        try:
            book = Books.objects.get(id=id)
            book.delete()
            return Response({
                "SUCCESS":True,
                "DATA":"Books Deleted Successfully !!"
            },
            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error":str(e)
            },
            status=status.HTTP_400_BAD_REQUEST)











# @csrf_exempt
# def booksApi(request,id=0):
#     if request.method =='GET':
#         books = Books.objects.all()
#         books_serializers=BooksSerializers(books,many=True)
#         return JsonResponse(books_serializers.data,safe=False)
#     elif request.method=='POST':
#         books_data=JSONParser().parse(request)
#         books_serializers=UsersSerializers(data=books_data)
#         if books_serializers.is_valid() :
#             books_serializers.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT' :
#         books_data=JSONParser.parse(request)
#         books=Users.objects.get(id=books_data['book_id'])
#         books_serializers=BooksSerializers(books,data=books_data)
#         if books_serializers.is_valid() :
#             books_serializers.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failde to Update")
#     elif request.method=='DELETE':
#         books=Books.objects.get(id=books_data['book_id'])
#         books.delete() 
#         return JsonResponse("Deleted Successfully",safe=False)           

# def func(request):
#     print(Books.objects.all())
#     return HTTPResponse('success')
