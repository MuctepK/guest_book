from django import forms


class NoteForm(forms.Form):
    author_name = forms.CharField(max_length=70, label='Имя', required=True)
    author_mail = forms.EmailField(max_length=80, label='Email', required=True)
    text = forms.CharField(max_length=3000, label='Текст', required=True,
                           widget=forms.Textarea(attrs={'rows': 8, 'cols': 15}))


class SearchForm(forms.Form):
    pattern = forms.CharField(max_length=100, required=True, label='',widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'}))