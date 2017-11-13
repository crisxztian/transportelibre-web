from domicilios.models import clientes, domiciliarios, vehiculos
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, FileInput, Select

class domiciliariosForm(ModelForm):
    class Meta:
        model = domiciliarios
        fields = ['id','documento','nombres', 'apellidos', 'email', 'telefono', 'rostro']
        widgets = {
            'id':  NumberInput(attrs={'class':'form-control'}),
            'documento':  TextInput(attrs={'class':'form-control'}),
            'nombres':  TextInput(attrs={'class':'form-control'}),
            'apellidos':  TextInput(attrs={'class':'form-control'}),
            'email':  EmailInput(attrs={'class':'form-control'}),
            'telefono':  NumberInput(attrs={'class':'form-control'}),
            'rostro':  FileInput(attrs={'class':'form-control'}),
        }

class clientesForm(ModelForm):
    class Meta:
        model = clientes
        fields = ['id','documento','nombres', 'apellidos', 'email', 'telefono', 'rostro']
        widgets = {
            'id':  NumberInput(attrs={'class':'form-control'}),
            'documento':  TextInput(attrs={'class':'form-control'}),
            'nombres':  TextInput(attrs={'class':'form-control'}),
            'apellidos':  TextInput(attrs={'class':'form-control'}),
            'email':  EmailInput(attrs={'class':'form-control'}),
            'telefono':  NumberInput(attrs={'class':'form-control'}),
            'direccion': TextInput(attrs={'class':'form-control'}),
        }

class vehiculosForm(ModelForm):
    class Meta:
        model = vehiculos
        fields = ['id', 'tipo', 'placa']
        widgets = {
            'id':  NumberInput(attrs={'class':'form-control'}),
            'tipo':  Select(attrs={'class':'form-control'}),
            'placa':  TextInput(attrs={'class':'form-control'}),
        }
