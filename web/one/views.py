from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, reverse,redirect
from .models import Categoryposts, Interview
from marketing.models import Signup
from django.db.models import Q
from .forms import CommentForm
from .forms import InterviewForm


def search(request):
    queryset = Categoryposts.objects.filter(blogpost = True)
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(about__icontains=query)
        ).distinct()
        
        context = {
            'queryset': queryset
        }
        return render(request,'search_results.html', context)


def searchInterviews(request):
    queryset = Interview.objects.filter(select = True )
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(company_name__icontains=query)
        ).distinct()
        
        context = {
            'queryset': queryset
        }
        return render(request,'search_interview_results.html', context)

def index(request):


    featured = Categoryposts.objects.filter(homepost = True)
    latest = Categoryposts.objects.order_by('-date')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'cposts': featured,
        'latest': latest
    }
    return render(request,'index.html',context)

def blog(request):
    most_recent = Categoryposts.objects.order_by('-date')[:3]
    posts = Categoryposts.objects.filter(blogpost = True)
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent
    }
    return render(request,'blog.html',context)


def post(request, id):
    most_recent = Categoryposts.objects.order_by('-date')[:3]
    post = get_object_or_404(Categoryposts,id=id)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.instance.post = post
        form.save()
        return redirect(reverse("post-detail",kwargs={
            'id':post.pk
        }))

    context = {
        'most_recent': most_recent,
        'post':post,
        'form':form,
    }
    return render(request,'post.html',context)

def interviews(request,id):
    inter = get_object_or_404(Interview,id=id)
    my_form = InterviewForm(request.POST or None)
    if request.method == "POST":
        if my_form.is_valid():
            my_form.instance.user = request.user
            my_form.instance.post = post
            my_form.save()
            return redirect(reverse("interviews-detail",kwargs={
                'id':inter.pk
            }))
    context ={
        'p':inter,
        'form':my_form
    }
    return render(request,'interview_experience_results.html',context)

def interview_form(request):
    my_form = InterviewForm(request.POST or None)
    if request.method == "POST":
        if my_form.is_valid():
            my_form.save()
            return redirect('/')
    context = {
        'form':my_form
    }
    return render(request,'interview_form.html',context)

def interview_experience(request):
    inter_post  = Interview.objects.order_by('-timestamp')[:]
    
    context = {
        'post':inter_post
    }
    return render(request,'interview_experience.html',context)
