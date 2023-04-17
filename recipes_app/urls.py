from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('subscribe/', views.newsletter_signup, name='newsletter_signup'),
    path('unsubscribe/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),
    path('receptai/', views.RecipeListView.as_view(), name='recipe_list'),
    path('receptai/kategorija/<int:tree_id>/', views.RecipeCategoryListView.as_view(), name='recipe_category_list'),
    path('receptai/subkategorija/<int:id>/', views.RecipeSubCategoryListView.as_view(), name='recipe_subcategory_list'),
    path('receptai/zyma/<int:id>/', views.RecipeTagListView.as_view(), name='recipe_tag_list'),
    path('receptai/<slug:slug>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('naudinga-informacija/griliaus-ruosimas', views.info_grill, name='info_grill'),
    path('naudinga-informacija/pakuociu-etiketes', views.info_labels, name='info_labels'),
    path('naudinga-informacija/mato-vienetai', views.info_measurement, name='info_measurement'),
    path('naudinga-informacija/maisto-temperatura', views.info_temperature, name='info_temperature'),
    path('apie', views.about, name='about'),
    path('search', views.search, name='search'),
    path('atsitiktinis_receptas', views.random_recipe, name='random_recipe'),
]
