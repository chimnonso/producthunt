from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from .forms import UserCreateForm
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


# Create your views here.

class SignupView(CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/join.html'
    success_url = reverse_lazy('accounts:login')

# class UserPageDetail(DetailView):
#     model = User
#     template_name='accounts/userpage.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Product.objects.filter(hunter=self.object.pk)
#         print(context.get('user').my_products.all(),7890)
#         print(context)
#         return context