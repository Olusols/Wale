from django.shortcuts import render
from .models import Product
from django.views .generic import DeleteView, ListView, UpdateView, DetailView, CreateView
from django.urls import reverse_lazy


def items(request):
    return render(request, 'cart.html')


def productlist(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'product-list.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'post-detail.html'


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'edit-post.html'
    fields = ['title', 'body']


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete-post.html'
    success_url = reverse_lazy('blog:home')
