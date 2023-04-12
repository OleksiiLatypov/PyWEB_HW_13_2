from django.forms import ModelForm, CharField, TextInput, IntegerField, DateField, DateInput, ModelMultipleChoiceField, \
    Textarea, SelectDateWidget

from django.forms import ModelForm, CharField, TextInput, ModelChoiceField

from .models import Tag, Author, Quote

YEARS = [x for x in range(1940, 2021)]


class TagForm(ModelForm):
    tag = CharField(min_length=3, max_length=250, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['tag']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=5, max_length=150, widget=TextInput())
    born_date = DateField(required=True, widget=SelectDateWidget(years=YEARS))
    born_location = CharField(required=True, widget=TextInput())
    description = CharField(min_length=5, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    quote = CharField(max_length=500, required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
