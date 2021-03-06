from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Categoty
from django.views.generic import ListView,DetailView

# Create your views here.


class PostList(ListView):
    queryset = Post.objects.published()
    paginate_by = 2

class PostDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post.objects.published(),slug=slug)

def postdetail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month, publish__day=day, slug=post)
    return render(request, 'blog/post_detail.html', {"post": post})


def category(request, slug,page=1):
    category = get_object_or_404(Categoty, slug=slug, status=True)
    post_list = category.posts.published()
    paginator = Paginator(post_list, 3)
    post = paginator.get_page(page)
    return render(request, "blog/category.html", {"category": category,'post':post})
