from rest_framework import serializers
from .models import User, Post, Category, Tag
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    token_detail = serializers.SerializerMethodField("get_token_detail")

    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','gender','phone_no','password','token_detail')

    def get_token_detail(self, obj):#obj,self=arguments
        token, created = Token.objects.get_or_create(user=obj) #isme objects ke perameter ko user ke perameter mai change nkr diya
        return token.key
    
class UserdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'email', 'phone_no', 'gender')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)  # Adjust this to include other fields you need

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name',) 
        
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Use the CategorySerializer directly
    tags = TagSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'category', 'tags')

class PostupdateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Post
        fields = ('id', 'title', 'text')



    

# class UserSerializer(serializers.ModelSerializer):
#     # def clean_password2(self):
#     #     password1 = self.cleaned_data.get("password1")
#     #     password2 = self.cleaned_data.get("password2")
#     #     if password1 and password2 and password1 != password2:
#     #         raise serializers.ValidationError("Passwords do not match")
#     #     return password2

#     class Meta:
#         model = User
#     fields = ('username','email','first_name','last_name','password1','password2','image','gender','phone_no')
















