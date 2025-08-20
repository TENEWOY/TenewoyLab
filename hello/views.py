from django.shortcuts import render, get_object_or_404
from .models import Post
from django.conf import settings
from .models import Visit
def home(request):
    return render(request, 'hello/home.html')

def about(request):
    return render(request, 'hello/about.html')

def it2025(request):
    return render(request, 'hello/it2025.html')

def contacts(request):
    return render(request, 'hello/contacts.html')

def worker(request):
    return render(request, 'hello/worker.html')

def courses(request):
    return render(request, 'hello/courses.html')

def news(request):
    return render(request, 'hello/news.html')

# список всех статей
def posts_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'hello/posts_list.html', {'posts': posts})

# детальный просмотр статьи
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'hello/post_detail.html', {'post': post})

def money(request):
    context = {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,  # Для Stripe
        'yoomoney_wallet': settings.STRIPE_SECRET_KEY
    }
    return render(request, 'hello/money.html', context)

def stats(request):
    visits = Visit.objects.all().order_by('-timestamp')[:50]  # последние 50 посещений
    total_visits = Visit.objects.count()
    return render(request, "hello/stats.html", {
        "visits": visits,
        "total": total_visits
    })