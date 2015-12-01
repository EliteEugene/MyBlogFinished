from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя пользователя")
    email = forms.EmailField(max_length=100, label="E-mail")
    message = forms.CharField(widget=forms.Textarea(), max_length=1000, label="Сообщение")