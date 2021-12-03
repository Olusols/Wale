from django.shortcuts import render
from .models import Post, Categories, Review, Newsletter
from Items.models import Product
from django.http import HttpResponseRedirect
from django.views .generic import DeleteView, ListView, UpdateView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q


def index(request):
    if request.method == 'POST':
        newsletter = request.POST.get('newsletter')
        form = Newsletter(email=newsletter)
        form.save()
        return HttpResponseRedirect('home')
    post = Post.objects.all()[:6]
    category = Categories.objects.all()[:6]
    product = Product.objects.all()[:10]
    review = Review.objects.all()[:5]
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Product.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        data = Product.objects.filter(multiple_q)
    else:
        data = Product.objects.all()
    context = {
        'post': post,
        'category': category,
        'product': product,
        'review': review,
        'data': data,
    }
    return render(request, 'home.html', context)


'''
class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
    	context = super(SearchProductView, self).get_context_data(*args, **kwargs)
    	query = self.request.GET.get('q')
    	context['query'] = query

    	return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        # print(query)
        if query is not None:
        	return Product.objects.search(query)
        return Product.objects.featured()


'''


def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')

        return HttpResponseRedirect('home')

    return render(request, 'search.html')


def blog(request):
    post = Post.objects.all()
    return render(request, 'blog.html')


class PostDetail(DetailView):
    model = Post
    template_name = 'post-detail.html'


class UpdateView(UpdateView):
    model = Post
    template_name = 'edit-post.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('blog:home')


class CategoryList(ListView):
    model = Categories
    template_name = 'category-list.html'


class CategoryDetail(DetailView):
    model = Categories
    template_name = 'category-detail.html'


def about(request):
    return render(request, 'about.html')
