from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Autor, Editora, Livro, Publica


def validate_not_whitespace(value):
	"""Validador que rejeita valores vazios ou compostos apenas por espaços."""
	if value is None or not str(value).strip():
		raise ValidationError(_("This field cannot be blank or contain only whitespace."), code="blank")


class AutorForm(forms.ModelForm):
	class Meta:
		model = Autor
		fields = ['nome']
		widgets = {
			'nome': forms.TextInput(attrs={'placeholder': 'Nome do autor', 'class': 'input-text'}),
		}

	def clean_nome(self):
		nome = self.cleaned_data.get('nome')
		validate_not_whitespace(nome)
		return nome.strip()


class EditoraForm(forms.ModelForm):
	class Meta:
		model = Editora
		fields = ['nome']
		widgets = {
			'nome': forms.TextInput(attrs={'placeholder': 'Nome da editora', 'class': 'input-text'}),
		}

	def clean_nome(self):
		nome = self.cleaned_data.get('nome')
		validate_not_whitespace(nome)
		return nome.strip()


class LivroForm(forms.ModelForm):
	class Meta:
		model = Livro
		fields = ['ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora']
		widgets = {
			'ISBN': forms.TextInput(attrs={'placeholder': 'ISBN', 'class': 'input-text'}),
			'titulo': forms.TextInput(attrs={'placeholder': 'Título', 'class': 'input-text'}),
			'publicacao': forms.DateInput(attrs={'type': 'date', 'class': 'input-text'}),
			'preco': forms.NumberInput(attrs={'step': '0.01', 'class': 'input-text'}),
			'estoque': forms.NumberInput(attrs={'class': 'input-text'}),
			'editora': forms.Select(attrs={'class': 'input-text'}),
		}

	def clean_ISBN(self):
		isbn = self.cleaned_data.get('ISBN')
		if isbn is None:
			raise ValidationError(_('ISBN is required.'), code='required')
		isbn_str = str(isbn).strip()
		# Accept ISBN-10 or ISBN-13 digits (basic check)
		digits = ''.join(ch for ch in isbn_str if ch.isdigit())
		if len(digits) not in (10, 13):
			raise ValidationError(_('Enter a valid ISBN with 10 or 13 digits.'), code='invalid')
		return isbn_str

	def clean_titulo(self):
		titulo = self.cleaned_data.get('titulo')
		validate_not_whitespace(titulo)
		return titulo.strip()


class PublicaForm(forms.ModelForm):
	class Meta:
		model = Publica
		fields = ['livro', 'autor']
		widgets = {
			'livro': forms.Select(attrs={'class': 'input-text'}),
			'autor': forms.Select(attrs={'class': 'input-text'}),
		}

