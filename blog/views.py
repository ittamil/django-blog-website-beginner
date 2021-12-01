from django import template
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from blog.models import Blogpost,Comment,Video
from blog.forms import UserRegisterForm,UserPostForm,CommentForm
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.template import loader
# Create your views here.
def home(request):
    blogposts = Blogpost.objects.all()
    context = {
        'blogposts':blogposts
    }
    return render(request,'home.html',context)

def postdetails(request,slug):
    postdetail = get_object_or_404(Blogpost,slug=slug)
    comment = postdetail.comments.all()
    if request.method == "POST":
        print(request.POST)
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            com = Comment.objects.create(post=postdetail,name=request.POST['name'],content=request.POST['content'],email=request.POST['email'])
            com.save()
    
    else:
        commentform = CommentForm()
    context = {
        'postdetail':postdetail,
        'comments':comment,
        'commentform':commentform
    }
    return render(request,'postdetails.html',context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = UserRegisterForm()

    context = {
        'form':form
    }
    return render(request,'register.html',context)

def profile(request):

    if request.method == "POST":
        form = UserPostForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST)

            form.save(commit=True)
            return HttpResponseRedirect('/')

    else:
        form = UserPostForm()
    context = {
        'userform':UserPostForm
    }
    return render(request,'profile.html',context)

# def logout_view(request):

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        print(name,email,body)
       
        context = {
            "name":name,
            "email":email,
            "body":body
        }
        template = loader.render_to_string("mail.html",context)
        send_mail(
           'ITTamil - Chat',
            template,
            email,
           ['harisuku00@gmail.com'],
           fail_silently=False,
        )
    return render(request,'contact.html')

def index(request):
    form = UserPostForm()
    form1 = Video.objects.all()
    return render(request,'index.html',{'form':form,'form1':form1})