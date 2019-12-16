from django import forms

from apps.plan.models import Plan

class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan

        fields = [
            'plan',
            'curso',
            'tipo',
            'persona',
        ]
        labels ={
            'plan': 'Plan',
            'curso': 'Curso',
            'tipo': 'Tipo de Curso',
            'persona': 'Comprador',

        }
        widgets = {
            'plan': forms.TextInput(attrs={'class':'form-control'}),
            'curso': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),

        }