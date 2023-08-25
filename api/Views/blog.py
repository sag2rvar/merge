from rest_framework.generics import ListAPIView , RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from blog.serializers import PostSerializer, PostupdateSerializer   
from blog.models import Post ,Category, Tag
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class UserPostsView(APIView):
	
	permission_classes = [IsAuthenticated]

	def get(self, request):
		res = {}
		user_posts = Post.objects.filter(author=request.user)
		print(user_posts, '3333333333333333333333333')
			
		serializer = PostSerializer(user_posts, many=True, read_only=True, context={"request": request})
		print(serializer,'111111111111111111111111111111')
		if serializer:

			res['status'] = True
			res['message'] = "post-view"
			res['data'] = serializer.data
			return Response(res, status=status.HTTP_200_OK)
		else :
			res['status'] = False
			res['message'] = "No posts found for the user"
			res['data'] = []
			return Response(res, status=status.HTTP_404_NOT_FOUND)


class UserPostscreate(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request):
		res = {}

		title = request.data.get("title", None)
		text = request.data.get("text", None)
		category_name = request.data.get("category", None)
		print(category_name,'1111111111111')
		tag_names = request.data.get("tags", [])
		print(tag_names,'2222222222222222')

		if title is None:
			res['status'] = False
			res['message'] = "title is required"
			res['data'] = []
			return Response(res, status=status.HTTP_400_BAD_REQUEST)
		if text is None:
			res['status'] = False
			res['message'] = "text is required"
			res['data'] = []
			return Response(res, status=status.HTTP_400_BAD_REQUEST)
		if category_name is None:
			res['status'] = False
			res['message'] = "category_name is required"
			res['data'] = []
			return Response(res, status=status.HTTP_400_BAD_REQUEST)
		if not tag_names:
			res['status'] = False

			res['message'] = "tags is required"
			res['data'] = []
			return Response(res, status=status.HTTP_400_BAD_REQUEST)

		try:
			category = Category.objects.get(name=category_name)
			print(category,'333333333333')
		except Category.DoesNotExist:
			res['status'] = False
			res['message'] = "Invalid category name"
			res['data'] = []
			return Response(res, status=status.HTTP_400_BAD_REQUEST)
		
		tagsss = []
		print(tagsss,'$$$$$$$$$$$$')
		for tag_name in tag_names.split(','):
			print(tag_name,'ooooooooooo')
			try:
				tag = Tag.objects.get(name=tag_name.strip()) #string indentation ko clear kr deta hai
				print(tag,'ooooooooooo')
				tagsss.append(tag)
			except Tag.DoesNotExist:
				res['status'] = False
				res['message'] = f"Invalid tag name: {tag_name}"
				res['data'] = []
				return Response(res, status=status.HTTP_400_BAD_REQUEST)


		data = Post.objects.create(title=title, text=text, category=category, author=request.user)
		data.tags.set(tagsss)

		serializer = PostSerializer(data, context={"request": request})

		if serializer:
			res['status'] = True
			res['message'] = "Post successfully created"
			res['data'] = serializer.data
			return Response(res, status=status.HTTP_201_CREATED)
		else:
			res['status'] = False
			res['message'] = "Something went wrong"
			res['data'] = []
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPostedit(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request, id=None):
		res = {}
		title = request.data.get("title", None)
		text = request.data.get("text", None)
		category = request.data.get("category", None)
		tags = request.data.get("tags", None)
		postid = request.data.get("id",None)


		# post = Post.objects.get(author=request.user.id).last()
		post = Post.objects.filter(id = postid).last()
		# print(post, "55555555555555555555555555555555555555555555555")

		if post is None:
			res['status'] = False
			res['message'] = "Authenticate Post detail not found!!"
			res['data'] = []
			return Response(res,  status=status.HTTP_404_NOT_FOUND)

		if category:
			res['status'] = False
			res['message'] = "Category is not changeable"
			res['data'] = []
			return Response(res, status=status.HTTP_400_BAD_REQUEST)

		if tags:
			res['status'] = False
			res['message'] = "Tags is not changeable"
			res['data'] = []
			return Response(res, status=status.HTTP_400_BAD_REQUEST)

		# data = request.data   

		# try:
		# 	data._mutable =True
		
		# except:
		# 	pass

		# data['category'] = post.category

		# data['tags'] = post.tags

		# # if title is None:
		# # 	data['title'] = post.title

		# if title is None:
		# 	data['title'] = post.title
		# if text is None:
		# 	data['city'] = post.text

		# print(data,"kkkkkkkkkkkkkkkkkkkkk")

		serializer = PostupdateSerializer(data=request.data, instance = post, context={'request': request}) 
		print(serializer, '787887788888888888888888')
		
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			res['status'] = True
			res['message'] = 'Post detail Update successfully'
			res['data'] = serializer.data
			return Response(res, status=status.HTTP_200_OK)

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer

class PostDeleteView(DestroyAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = PostSerializer
	# queryset = Post.objects.all()
	# def post(self, request, id=None):
	# 	res = {}
	# 	# postid = request.data.get("id",None)

	# 	# post = Post.objects.filter(id = postid).last()
	# 	if post is None:
	# 		res['status'] = False
	# 		res['message'] = "Authenticate Post detail not found!!"
	# 		res['data'] = []
	# 		return Response(res,  status=status.HTTP_404_NOT_FOUND)
	# 	else:
	# 		res['status'] = True
	# 		res['message'] = "Postdeleted"
	# 		res['data'] = request.data
	# 		return Response(res,  status=status.HTTP_404_NOT_FOUND)

		

		
		
	







		
