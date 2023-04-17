from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, reverse
from django.template.loader import get_template
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import NewsletterUserSignupForm, CommentForm, RecipeFilterForm
from .models import Recipe, Category, Tag, Info, NewsletterUser
import random
import requests


class HomeView(ListView):
    model = Recipe
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get('https://zenquotes.io/api/random')
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            context['quote'] = quote
            context['author'] = author
        context['uzkandziai_count'] = Recipe.objects.filter(category__tree_id='1').count()
        context['sriubos_count'] = Recipe.objects.filter(category__tree_id='2').count()
        context['karstieji_count'] = Recipe.objects.filter(category__tree_id='3').count()
        context['gerimai_count'] = Recipe.objects.filter(category__tree_id='4').count()
        context['desertai_count'] = Recipe.objects.filter(category__tree_id='5').count()
        return context


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    ordering = '-create_at'
    paginate_by = 5

    def get_queryset(self):
        return Recipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_count_by_category = Recipe.objects.values(
            'category__id', 'category__name', 'category__tree_id').annotate(recipe_count=Count('category__id'))
        context['recipe_count_by_category'] = recipe_count_by_category
        context['uzkandziai_count'] = Recipe.objects.filter(category__tree_id='1').count()
        context['sriubos_count'] = Recipe.objects.filter(category__tree_id='2').count()
        context['karstieji_count'] = Recipe.objects.filter(category__tree_id='3').count()
        context['gerimai_count'] = Recipe.objects.filter(category__tree_id='4').count()
        context['desertai_count'] = Recipe.objects.filter(category__tree_id='5').count()
        return context


class RecipeCategoryListView(ListView):
    model = Recipe
    template_name = 'recipe_category_list.html'
    ordering = '-create_at'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_count_by_category = Recipe.objects.values(
            'category__id', 'category__name', 'category__tree_id').annotate(recipe_count=Count('category__id'))
        context['recipe_count_by_category'] = recipe_count_by_category
        context['category'] = Category.objects.filter(tree_id=self.kwargs['tree_id'])
        context['uzkandziai_count'] = Recipe.objects.filter(category__tree_id='1').count()
        context['sriubos_count'] = Recipe.objects.filter(category__tree_id='2').count()
        context['karstieji_count'] = Recipe.objects.filter(category__tree_id='3').count()
        context['gerimai_count'] = Recipe.objects.filter(category__tree_id='4').count()
        context['desertai_count'] = Recipe.objects.filter(category__tree_id='5').count()
        return context

    def get_queryset(self):
        tree_id = self.kwargs['tree_id']
        queryset = Recipe.objects.filter(category__tree_id=tree_id)
        return queryset


class RecipeSubCategoryListView(ListView):
    model = Recipe
    template_name = 'recipe_subcategory_list.html'
    ordering = '-create_at'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_count_by_category = Recipe.objects.values(
            'category__id', 'category__name', 'category__tree_id').annotate(recipe_count=Count('category__id'))
        context['recipe_count_by_category'] = recipe_count_by_category
        context['category'] = Category.objects.filter(id=self.kwargs['id'])
        context['uzkandziai_count'] = Recipe.objects.filter(category__tree_id='1').count()
        context['sriubos_count'] = Recipe.objects.filter(category__tree_id='2').count()
        context['karstieji_count'] = Recipe.objects.filter(category__tree_id='3').count()
        context['gerimai_count'] = Recipe.objects.filter(category__tree_id='4').count()
        context['desertai_count'] = Recipe.objects.filter(category__tree_id='5').count()
        return context

    def get_queryset(self):
        queryset_id = self.kwargs['id']
        queryset = Recipe.objects.filter(category__id=queryset_id)
        return queryset


class RecipeTagListView(ListView):
    model = Recipe
    template_name = 'recipe_tag_list.html'
    ordering = '-create_at'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_count_by_category = Recipe.objects.values(
            'category__id', 'category__name', 'category__tree_id').annotate(recipe_count=Count('category__id'))
        context['recipe_count_by_category'] = recipe_count_by_category
        context['tag'] = Tag.objects.filter(id=self.kwargs['id'])
        context['uzkandziai_count'] = Recipe.objects.filter(category__tree_id='1').count()
        context['sriubos_count'] = Recipe.objects.filter(category__tree_id='2').count()
        context['karstieji_count'] = Recipe.objects.filter(category__tree_id='3').count()
        context['gerimai_count'] = Recipe.objects.filter(category__tree_id='4').count()
        context['desertai_count'] = Recipe.objects.filter(category__tree_id='5').count()
        return context

    def get_queryset(self):
        queryset_id = self.kwargs['id']
        queryset = Recipe.objects.filter(tags__id=queryset_id)
        return queryset


class RecipeDetailView(FormMixin, DetailView):
    model = Recipe
    context_object_name = "recipe"
    template_name = 'recipe_detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_count_by_category = Recipe.objects.values(
            'category__id', 'category__name', 'category__tree_id').annotate(recipe_count=Count('category__id'))
        context['recipe_count_by_category'] = recipe_count_by_category
        context['uzkandziai_count'] = Recipe.objects.filter(category__tree_id='1').count()
        context['sriubos_count'] = Recipe.objects.filter(category__tree_id='2').count()
        context['karstieji_count'] = Recipe.objects.filter(category__tree_id='3').count()
        context['gerimai_count'] = Recipe.objects.filter(category__tree_id='4').count()
        context['desertai_count'] = Recipe.objects.filter(category__tree_id='5').count()
        recipe = self.get_object()
        previous_recipe = Recipe.objects.filter(id__lt=recipe.id).order_by('-id').first()
        next_recipe = Recipe.objects.filter(id__gt=recipe.id).order_by('id').first()
        context['previous_recipe'] = previous_recipe
        context['next_recipe'] = next_recipe
        return context

    def get_queryset(self):
        return Recipe.objects.all()

    def get_success_url(self):
        return reverse("recipe_detail", kwargs={'slug': self.object.slug})

    def post(self):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.recipe = self.object
        form.save()
        return super().form_valid(form)


def about(request):
    info = get_object_or_404(Info, id=1)
    context = {'info': info}
    return render(request, 'info/about.html', context)


def info_grill(request):
    infos = Info.objects.filter(id__in=[4, 5, 6, 7])
    context = {'infos': infos}
    return render(request, 'info/grill.html', context)


def info_labels(request):
    info = get_object_or_404(Info, id=3)
    context = {'info': info}
    return render(request, 'info/labels.html', context)


def info_measurement(request):
    info = get_object_or_404(Info, id=2)
    context = {'info': info}
    return render(request, 'info/measurement.html', context)


def info_temperature(request):
    info = get_object_or_404(Info, id=8)
    context = {'info': info}
    return render(request, 'info/temperature.html', context)


def search(request):
    query = request.GET.get('query')
    search_results = Recipe.objects.filter(Q(title__icontains=query)
                                           | Q(category__name__icontains=query)
                                           | Q(recipe_ingredient__ingredient__name__icontains=query)
                                           | Q(tags__name__icontains=query)).distinct()
    paginator = Paginator(search_results, 8)
    page = request.GET.get('page')
    recipes = paginator.get_page(page)
    return render(request, 'search.html', {'recipes': recipes, 'query': query})


def newsletter_signup(request):
    form = NewsletterUserSignupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Klaida. Jūsų nurodytu el. paštu jau yra užprenumeruoti naujienlaiškiai',
                             'alert alert-warning alert-dismissible')
        else:
            instance.save()
            messages.success(request, 'Jūs sėkmingai užsiprenumeravote naujienlaiškius',
                             'alert alert-success alert-dismissible alert-dismissible')
            subject = 'Receptubankas prenumerata'
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR / 'recipes_app/templates/news/sign_up_email.txt', 'r', encoding='utf-8') as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject,
                body=signup_message,
                from_email=from_email,
                to=to_email
            )
            html_template = get_template('news/sign_up_email.html').render()
            message.attach_alternative(html_template, 'text/html')
            message.send()

    context = {
        'form': form,
    }
    return render(request, 'news/subscribe.html', context)


def newsletter_unsubscribe(request):
    form = NewsletterUserSignupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Jūsų el.paštas ištrintas',
                             'alert alert-success alert-dismissible')
            subject = 'Jūsų prenumerata receptubankas nutraukta'
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR / 'recipes_app/templates/news/unsubscribe_email.txt',
                      'r', encoding='utf-8') as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject,
                body=signup_message,
                from_email=from_email,
                to=to_email
            )
            html_template = get_template('news/unsubscribe_email.html').render()
            message.attach_alternative(html_template, 'text/html')
            message.send()
        else:
            messages.warning(request, 'Nurodyto el. pašto nėra mūsų duomenų bazėje',
                             'alert alert-warning alert-dismissible')

    context = {
        'form': form,
    }
    return render(request, 'news/unsubscribe.html', context)


def random_recipe(request):
    filtered_recipes = Recipe.objects.all()
    random_recipe = None

    if request.method == 'POST':
        form = RecipeFilterForm(request.POST)
        random_recipe = None
        if form.is_valid() or not form.has_changed():
            category_name = form.cleaned_data.get('category_name')
            ingredient_name = form.cleaned_data.get('ingredient_name')

            if category_name:
                if ingredient_name:
                    filtered_recipes = filtered_recipes.filter(category__name=category_name.name)
                    for ingredient in ingredient_name:
                        filtered_recipes = filtered_recipes.filter(recipe_ingredient__ingredient__name=ingredient)
                else:
                    filtered_recipes = filtered_recipes.filter(category__name=category_name.name)
            else:
                for ingredient in ingredient_name:
                    filtered_recipes = filtered_recipes.filter(recipe_ingredient__ingredient__name=ingredient)

            if filtered_recipes.exists():
                random_recipe = random.choice(filtered_recipes)
            else:
                random_recipe = None
    else:
        form = RecipeFilterForm()

    context = {
        'form': form,
        'random_recipe': random_recipe,
    }

    return render(request, 'random_recipe.html', context)
