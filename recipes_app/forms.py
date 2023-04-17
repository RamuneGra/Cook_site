from django import forms
from .models import Comment, NewsletterUser, Category, Ingredient


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_at']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Vardas'}),
            'email': forms.EmailInput(attrs={'placeholder': 'El. paštas'}),
            'message': forms.Textarea(attrs={'placeholder': 'Komentaras'})
        }


class NewsletterUserSignupForm(forms.ModelForm):

    class Meta:
        model = NewsletterUser
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email


class RecipeFilterForm(forms.Form):
    category_name = forms.ModelChoiceField(
        queryset=Category.objects.filter(level=1),
        empty_label='-- All --',
        required=False,
        label='Kategorija',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    ingredient_name = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        required=False,
        label='Produktai',
        help_text='Siūlome pasirinkite ne daugiau 5 produktų. Keliems produktams pasirinkti naudokite ctrl arba shift',
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
