from django import forms


class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()


class CursoBuscarFormulario(forms.Form):
    curso = forms.CharField()


class ProfesorFormulario(forms.Form)