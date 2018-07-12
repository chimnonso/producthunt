from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Product, UpVote
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

User = get_user_model()


class ProductList(ListView):
    model = Product
    # context_object_name = 'products'
    # template_name=''

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'domain', 'body', 'image']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.hunter = self.request.user
        return super().form_valid(form)

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['hasvoted'] = UpVote.objects.filter(voted_by=self.request.user, product=self.object.pk) and True or False
        return context


# def ProductDetail(request, product_id):
#     product = get_object_or_404(Product, slug=product_id)
#     has_voted = product.vote.filter(voted_by=request.user) and True or False
#     context = {'product': product, 'has_voted': has_voted}
#     return render(request, 'products/detail.html', context)


# @login_required(login_url='/accounts/login')
def upvote(request):
    if request.user.is_authenticated:
        print("User is None None")
    prod_id = request.GET['product_id']
    new_upvote, created = UpVote.objects.get_or_create(product_id=prod_id, voted_by=request.user)
    countVote = UpVote.objects.filter(product_id=prod_id).count()
    return HttpResponse(countVote)

class UserProducts(DetailView):
    model = User
    template_name = 'products/user_products.html'


def user_products(request, user_id, username):
    user = User.objects.get(pk=user_id)
    return render(request, 'products/user_products.html', {'user': user})
    # pass