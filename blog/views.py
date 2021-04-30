from django.shortcuts import render
from .models import BlogPost
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def blog(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST' and request.FILES:
        blog_title = request.POST.get('title')
        blog_description = request.POST.get('description')
        blog_category = request.POST.get('category')
        blog_body = request.POST.get('body')
        blog_image = request.FILES.get('image')

        blog_post = BlogPost(title=blog_title, description=blog_description, category=blog_category,
                             body=blog_body, image=blog_image, author=request.user)
        blog_post.save()
       

        return render(request, 'blog_success.html')
    else:
        return render(request, 'create_blog.html')

@login_required(login_url='login')
def blog_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        sql_query = f"SELECT * FROM blog_blogpost WHERE category='{search_query}'"
        objects = BlogPost.objects.raw(sql_query)
        context = {
            'posts': objects,
        }
        print(objects)

    else:
        objects = BlogPost.objects.raw("SELECT * FROM blog_blogpost")
        context = {
            'posts': objects,
        }
        print(objects)

    return render(request, 'blog_view.html', context)
