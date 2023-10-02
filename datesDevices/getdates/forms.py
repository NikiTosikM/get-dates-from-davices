from django.forms import ModelForm
from .models import SystemParamets
from django import forms


class FormSystemParamets(ModelForm):

    def __init__ (self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'id':
                field.widget.attrs.update({'class': 'input_field'})

    class Meta:
        model = SystemParamets

        fields = ['number_plot','number_equipment', 'number_node', 'name', 'date_of_repair', 'replaced_parts', 'next_replacement_date']

        labels = {
            'number_plot': 'Номер участка',
            'number_equipment': 'Номер оборудования', 
            'number_node': 'Номер узла',
            'name': 'Наименование',
            'date_of_repair': 'Дата ремонта',
            'replaced_parts': 'Замененные детали',
            'next_replacement_date': 'Дата следующей замены'
        }