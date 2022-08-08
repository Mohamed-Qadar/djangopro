from django.shortcuts import render, HttpResponse,redirect,reverse
from django.shortcuts import get_object_or_404
from . forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def articles(request):
    keyword =request.GET.get("keyword")
    if keyword:
        articles =Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    articles =Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


@login_required(login_url="user:login")
def dashboard(request):
    articles =Article.objects.filter(author =request.user)
    return render(request,"dashboard.html",{"articles":articles})

@login_required(login_url="user:login")
def addarticle(request):
    form =ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
       #form.save()# hadii aaan saas kaga tagno error aa sobixdo maxaa yeley qoraga maynan shegin qofka uu yahay.
       article =form.save(commit=False)#waxay kamacno tahya adu ha aburin userka.
       article.author =request.user
       article.save()
       messages.success(request,"basar ile keydediniz.")
       return redirect("index")
    return render(request,"addarticle.html",{"form": form})


def detail(request,id):
    article =Article.objects.filter(id =id).first()
    #  article =get_object_or_404(Article,id= id)
    article =get_object_or_404(Article,id= id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url="user:loginUser")
def updataArticle(request,id):
    article =get_object_or_404(Article,id =id)
    form = ArticleForm(request.POST or None,request.FILES or None, instance=article)
    if form.is_valid():
        # form.save()# hadii aaan saas kaga tagno error aa sobixdo maxaa yeley qoraga maynan shegin qofka uu yahay.
        article = form.save(commit=False)  # waxay kamacno tahya adu ha aburin userka.
        article.author = request.user
        article.save()
        messages.success(request, "basar ile guncelllendi.")
        return redirect("index")
    return render(request,"update.html",{"form": form})

@login_required(login_url="user:loginUser")
def deleteArticle(request,id):
    article =get_object_or_404(Article,id =id)

    article.delete()
    messages.success(request,"basari ila silindi")
    #return redirect("website:dashboard/articles")
    return redirect("index")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
        #dashboard/articles/article/
    #return redirect(reverse("website:detail",kwargs={"id":id}))
    return redirect("dashboard/articles/article/", +str(id))