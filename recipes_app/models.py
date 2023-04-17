from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField


class Category(MPTTModel):
    name = models.CharField(verbose_name='Pavadinimas', max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategorija'
        verbose_name_plural = 'Kategorijos'


class Ingredient(models.Model):
    name = models.CharField(verbose_name='Produktas', max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ingredientas'
        verbose_name_plural = 'Ingredientai'
        ordering = ['name']


class MeasurementUnit(models.Model):
    name = models.CharField(verbose_name='Pavadinimas', max_length=20)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mato vienetas'
        verbose_name_plural = 'Mato vienetai'
        ordering = ['name']


class Tag(models.Model):
    name = models.CharField(verbose_name='Pavadinimas', max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Žyma'
        verbose_name_plural = 'Žymos'
        ordering = ['name']


class Recipe(models.Model):
    create_at = models.DateTimeField(verbose_name='Sukūrimo data', auto_now_add=True)
    author = models.ForeignKey(
        to=User,
        verbose_name='Autorius',
        max_length=50,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recipes"
    )
    title = models.CharField(verbose_name='Pavadinimas', max_length=100)
    image = models.ImageField(verbose_name='Nuotrauka', upload_to='images/', null=True)
    description = HTMLField(verbose_name='Aprašymas', null=True, blank=True)
    serves = models.PositiveIntegerField(verbose_name='Porcijos', default=0)
    cook_time = models.PositiveIntegerField(verbose_name='Gaminimo laikas', default=0)
    directions = HTMLField(verbose_name='Gaminimo eiga')
    notes = HTMLField(verbose_name='Pastabos', null=True, blank=True)
    category = models.ForeignKey(
        Category,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(
        to='Tag',
        related_name='recipe')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def display_tag(self):
        return ', '.join(tags.name for tags in self.tags.all()[:3])

    display_tag.short_description = 'Žymos'

    def get_comments(self):
        return self.comment.all()

    class Meta:
        verbose_name = 'Receptas'
        verbose_name_plural = 'Receptai'
        ordering = ['-create_at']


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(
        to='Recipe',
        verbose_name='Receptas',
        on_delete=models.CASCADE,
        related_name='recipe_ingredient'
    )
    ingredient = models.ForeignKey(
        to='Ingredient',
        verbose_name='Ingredientas',
        on_delete=models.SET_NULL,
        null=True
    )
    quantity = models.FloatField(verbose_name='Kiekis', default=0)
    measurement_unit = models.ForeignKey(
        to='MeasurementUnit',
        verbose_name='Mato vienetas',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f'{self.recipe} | {self.ingredient} ({self.quantity})'

    class Meta:
        verbose_name = 'Recepto ingredientas'
        verbose_name_plural = 'Recepto ingredientai'


class Comment(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, default='Anonimas')
    email = models.CharField(verbose_name='El. paštas', max_length=100, null=True, blank=True)
    message = models.TextField(verbose_name='Tekstas', max_length=500)
    create_at = models.DateTimeField(verbose_name='Sukūrimo data', default=timezone.now)
    recipe = models.ForeignKey(
        to='Recipe',
        on_delete=models.CASCADE,
        related_name='comment',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Komentaras'
        verbose_name_plural = 'Komentarai'
        ordering = ['-create_at']


class Info(models.Model):
    notes = HTMLField(verbose_name='Aprašymas')

    class Meta:
        verbose_name = 'Informacija'
        verbose_name_plural = 'Informacija'


class NewsletterUser(models.Model):
    email = models.EmailField(verbose_name='El. paštas', max_length=100)
    date_added = models.DateTimeField(verbose_name='Pridėjimo data', auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Naujienlaiškio gavėjas'
        verbose_name_plural = 'Naujienlaiškio gavėjai'
        ordering = ['email']


class Newsletter(models.Model):
    EMAIL_STATUS_CHOICE = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    subject = models.CharField(verbose_name='Tema', max_length=255)
    body = models.TextField(verbose_name='Tekstas')
    email = models.ManyToManyField(NewsletterUser)
    status = models.CharField(verbose_name='Statusas', max_length=10, choices=EMAIL_STATUS_CHOICE)
    created = models.DateTimeField(verbose_name='Sukūrimo data', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Atnaujinimo data', auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Naujienlaiškis'
        verbose_name_plural = 'Naujienlaiškai'
        ordering = ['-created']
