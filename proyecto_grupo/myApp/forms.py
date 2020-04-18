from django import forms

class empleadoForm(forms.Form):
        dni = forms.CharField(label="DNI", max_length=9)
        nombre = forms.CharField(label="Nombre", max_length=100)
        apellidos = forms.CharField(label="Apellidos", max_length=100)
        email = forms.EmailField(label="Email", max_length=50)
        telefono = forms.IntegerField(label="Telefono")
        estado = forms.CharField(label="Estado", max_length=50)
