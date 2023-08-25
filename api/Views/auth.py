# Api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.settings import api_settings
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate
from blog.serializers import UserSerializer, UserdetailsSerializer
from blog.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.generics import UpdateAPIView

class LoginView(APIView):
    permission_classes = [AllowAny] #attribute class, ye endpoint kisi bhi user ko allow karega, chaahe woh authenticated ho ya nahi.
    def post(self, request): #Yahan se hum username aur password ko request data se extract karte hain.
        res = {}
        username = request.data.get("username", None)
        # print(username,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        password = request.data.get("password", None)
        # print(password,"2222222222222222222222222222222222")
        if username is None:
            res['status'] = False
            res['message'] = "username is required"
            res['data'] = []
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        if password is None:
            res['status'] = False
            res['message'] = "password is required"
            res['data'] = []
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        # print(user,'uuuuuuuuuuuuuuuuuuuuuuu')

        if user is None:
            res['status'] = False
            res['message'] = "Invalid username & password is required"
            res['data'] = []
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(user, read_only=True, context={"request":request} )
        # print(serializer,'ppppppppppppppppppppppp')
        
        if serializer:
            res['status'] = True
            res['message'] = "Login successfull"
            res['data'] = serializer.data
            return Response(res, status=status.HTTP_200_OK)
        else:
            res['status'] = False
            res['message'] = "somthing went wrong"
            res['data'] = []
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        res = {}
        username = request.data.get("username", None)
        # print(username,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        email = request.data.get("email", None)
        # print(email,'9999999999999999999999999999999999999999999999')
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("first_name", None)
        password = request.data.get("password", None)
        # password2 = request.data.get("confirm_password", None)
        phone_no = request.data.get("phone_no", None)
        # print(password,'ttttttttttttttttttttttttttttttttttttttttttt')
        if username is None:
            res['status'] = False
            res['message'] = "username is required"
            res['data'] = []
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        if email is None:
            res['status'] = False
            res['message'] = "email is required"
            res['data'] = []
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        if first_name is None:
            res['status'] = False
            res['message'] = "first_name is required"
            res['data'] = []
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        if last_name is None:
            res['status'] = False
            res['message'] = "first_name is required"
            res['data'] = []
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        if phone_no is None:
            res['status'] = False
            res['message'] = "phone_no is required"
            res['data'] = []
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        if password is None:
            res['status'] = False
            res['message'] = "password is required"
            res['data'] = []
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        # if password2 is None:
        #     res['status'] = False
        #     res['message'] = "pusernameassword2 is required"
        #     res['data'] = []
        #     return Response(res, status=status.HTTP_400_BAD_REQUEST)
        # if password1 and password2 and password1 != password2:
        #     res['status'] = False
        #     res['message'] = "password is incorrect"
        #     res['data'] = []
        #     return Response(res, status=status.HTTP_400_BAD_REQUEST) 
        # 
        encrypted_password = make_password(password)   
        serializer = UserSerializer(data=request.data, context={"request":request})
        print(serializer,'qqqqqqqqqqqqqqqqqqqqq')
        if serializer.is_valid():
            serializer.save(password=encrypted_password)
            # res_data = serializer.data
            # print(res_data,'rrrrrrrrrrrrrrr')
            # user= User.objects.filter(id=res_data["id"]).last()
            # if password:
            #     user.set_password(password)

        #     return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            res['status'] = True
            res['message'] = "User registered successfully"
            res['data'] = serializer.data
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            res['status'] = False
            res['message'] = "somthing went wrong"
            res['data'] = []
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserProfileView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        res = {}
        # try:
        user = User.objects.filter(id=request.user.id).last()
        print(user,'tttttttttttttttttttttttttttttttttttttttttttt')
        if user is None:
            res['status'] = False
            res['message'] = "Authentication detail not found!!"
            res['data'] = []
            return Response(res,  status=status.HTTP_404_NOT_FOUND)
        serializer = UserdetailsSerializer(user, read_only=True, context={"request":request} )
        print(serializer,'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        if serializer:
            res['status'] = True
            res['message'] = "User-Profile"
            res['data'] = serializer.data
            return Response(res, status=status.HTTP_200_OK)
        else:
            res['status'] = False
            res['message'] = "User is not login"
            res['data'] = []
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProfileEditView(UpdateAPIView):#pre-built view for updating a model
    serializer_class = UserdetailsSerializer# deserializer

    def get_object(self):
        return self.request.user    