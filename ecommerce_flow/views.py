"""EcommerceFlow Views"""

# Django
from django.views.generic import TemplateView

# Models
from products.models import Category


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context