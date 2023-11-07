from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.db.models import Q
from .models import Repository
from django.views import View

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AccountPageView(TemplateView):
    template_name = "account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchRepositoriesView(View):
    def get(self, request):
        query = request.GET.get('q')
        sort_by = request.GET.get('sort_by', 'stars')  # Default sorting by stars

        # Define the sorting field based on user choice
        if sort_by == 'stars':
            sort_field = '-stars'  # Sort by stars in descending order
        elif sort_by == 'forks':
            sort_field = '-forks'  # Sort by forks in descending order
        elif sort_by == 'last_commit':
            sort_field = '-last_commit'  # Sort by last_commit in descending order
        else:
            sort_field = '-stars'  # Default sorting by stars

        if query:
            repositories = Repository.objects.filter(
                Q(name__icontains=query)
                | Q(description__icontains=query)).order_by(sort_field)
        else:
            repositories = Repository.objects.all().order_by(sort_field)

        context = {
            'query': query,
            'sort_by': sort_by,
            'repositories': repositories,
        }

        return render(request, 'search_results.html', context)