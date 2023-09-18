from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from .utils import *
from Profile.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .serializers import *
from home.models import *
from Profile.models import *
# Create your views here.

"""
Creating Custom Permissions [ inheriting from BasePermission and overriting permissions ].
This activeUser Permission can be used with the Decorator: @permission_classes.
This class checks whether the logged in user account is active or suspended ( Inactive ).
And will revoke access to url's if the user in question is Inactive.
"""
class activeUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.account_status == "Active":
            return True
        return False
"""
To access private information on the server such as the some profile's private data, that account needs to
have the supreme permission turned on.
"""
class supremeUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_supreme == True:
            return True
        return False


"""
Login Route that handles both GET & POST requests [ rather basic login system ] with character.
However a new JWT Authentication System has been added instead of this one.
JWT system will provide access token to logged in users once access and refresh tokens are expired,
Users need to use this LoginRoute to login and get themselves new access tokens.
"""
@api_view(['GET','POST'])
def LoginRoute(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            usr = CustomUser.objects.filter(username=username)
            if usr.exists():
                user = authenticate(username=username, password=password)
                if CustomUser.objects.get(username=username).account_status == "Active":
                    pass
                else:
                    return Response({"status": "Account Disabled"})
                if user is None:
                    return Response({"status": "invalid username or password"})
                else:
                    login(user=user, request=request)
                    return Response({"status": "logged in."})
            else:
                return Response({"status":"invalid username"})
        elif request.method == 'GET':
            return Response({"status": "Forbidden"})
        else:
            return Response({"status": "Invalid method"})

    except Exception as e:
        print(e)
        return Response({"status": "Something went wrong."})

"""
Registration Route that handles both GET & POST requests [ auto encrypts the passwords ].
Also checks if the given username already exists or not.
"""
@api_view(['GET','POST'])
def RegisterRoute(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']
            full_name = request.data['full_name']
            user_image = request.data['user_image']

            if CustomUser.objects.filter(username=username).exists():
                return Response({"status": f"User with username - {username} already exists"})

            user = CustomUser.objects.create(
                username = username,
                email = email,
                full_name = full_name,
                user_image = user_image
            )
            user.set_password(password)
            user.is_email_verified=False
            user.is_phone_verified=False
            user.account_status="Inactive"
            user.save()
            email_subject = "Action Required: Activate your Account"
            msg = render_to_string('activation.html',{
                'user':user,
                'domain':"127.0.0.1:8000",
                'uid':urlsafe_base64_encode(force_bytes(user.id)),
                'token': generate_token.make_token(user=user)
                })
            sendMail(msg=str(msg), reciever=email, subject=email_subject, username=username)
            return Response({
                "status": "Account Inactive",
                "warning": "Complete the registration via the link sent to your Email"
                })
        
        elif request.method == 'GET':
            return Response({"status": "Forbidden"})
        else:
            return Response({"status": "Invalid Method"})

    except Exception as e:
        print(e)
        return Response({"status": "Something went wrong."})

@api_view(['GET'])
def ActivateAccount(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = CustomUser.objects.get(id=uid)
    except Exception as e:
        user=None
    if user is None:
        return Response({"status": "User Does not Exist"})
    if user is not None and generate_token.check_token(user, token=token):
        user.is_email_verified=True
        user.account_status="Active"
        user.save()
        return Response({"status": "Email Verified"})
    return Response({"status": "Something went wrong."})

@api_view(['GET'])
def apiBase(request):
    return Response("Hemlo Niggas.")

@api_view(['GET'])
def apiHome(request):
    try:
        if request.method == 'GET':
            home_data = HomeModel.objects.all().select_related()
            homeSerialzer = HomePageSerializer(home_data, many=True)
            return Response(homeSerialzer.data)
        elif request.method == 'POST':
            return Response({"status": "Forbidden"})
        else:
            return Response({"status": "Invalid Method"})
    except Exception as e:
        print(e)
        return Response({"status": "Something went wrong."})

@api_view(['GET','POST','DELETE'])
def apiSingleCourse(request, course_id):
    try:
        if request.method == 'GET':
            single_course_data = Courses.objects.get(id=course_id)
            Single_Course_Serialzer = SingleCourseSeriealizer(single_course_data)
            return Response(Single_Course_Serialzer.data)
        elif request.method == 'POST':
            return Response({"status": "Forbidden"})
        elif request.method == 'DELETE':
            usr = request.user
            if usr.id != None:
                Courses.objects.get(id=course_id).delete()
                print(usr)
            else:
                return Response({"status": "Forbidden"})  
            return Response({"status": "Deleted"})
        else:
            return Response({"status": "Invalid Method"})
    except Exception as e:
        print(e)
        return Response({"status": "Something went wrong."})

@api_view(['GET'])
def apiBlogs(request):
    try:
        if request.method == 'GET':
            blogs_data = Blog.objects.all()
            blogsSerialzer = BlogsSerializer(blogs_data, many=True)
            return Response(blogsSerialzer.data)
        elif request.method == 'POST':
            return Response({"status": "Forbidden"})
        else:
            return Response({"status": "Invalid Method"})
    except Exception as e:
        print(e)
        return Response({"status": "Something went wrong."})

@api_view(['GET'])
def apiCourses(request):
    try:
        if request.method == 'GET':
            courses_data = Courses.objects.all()
            coursesSerialzer = ShowcaseCourses(courses_data, many=True)
            return Response(coursesSerialzer.data)
        elif request.method == 'POST':
            return Response({"status": "Forbidden"})
        else:
            return Response({"status": "Invalid Method"})
    except Exception as e:
        print(e)
        return Response({"status": "Something went wrong."})

@api_view(['GET','POST','DELETE'])
def apiSingleBlog(request, blog_id):
    try:
        if request.method == 'GET':
            single_blog_data = Blog.objects.get(id=blog_id)
            Single_Blog_Serialzer = SingleBlogSerializer(single_blog_data)
            return Response(Single_Blog_Serialzer.data)
        elif request.method == 'POST':
            return Response({"status": "Forbidden"})
        elif request.method == 'DELETE':
            usr = request.user
            if usr.id != None:
                Blog.objects.get(id=blog_id).delete()
                print(usr)
            else:
                return Response({"status": "Forbidden"})
            return Response({"status": "Deleted"})
        else:
            return Response({"status": "Invalid Method"})
    except Exception as e:
        print(e)
        return Response({"status": "Something went wrong."})