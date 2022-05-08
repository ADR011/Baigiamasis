# from django import forms

# # from .models import Person, City

# from .models import Order, Modelis


# class PersonCreationForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['modelis'].queryset = Modelis.objects.none()

#         if 'marke' in self.data:
#             try:
#                 marke_id = int(self.data.get('marke'))
#                 self.fields['modelis'].queryset = Modelis.objects.filter(marke_id=marke_id).order_by('modelis')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['modelis'].queryset = self.instance.marke.modelis_set.order_by('name')


from django import forms

# from .models import Person, City

from .models import Klientas, Modelis, Metai, Spalva


class PersonForm(forms.ModelForm):
    class Meta:
        model = Klientas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelis'].queryset = Modelis.objects.none()
        self.fields['metai'].queryset = Metai.objects.none()
        self.fields['spalva'].queryset = Spalva.objects.none()

        

        if 'marke' in self.data:
            try:
                marke_id = int(self.data.get('marke'))
                # modelis_id = int(self.data.get('modelis'))
                # self.fields['modelis'].queryset = Modelis.objects.filter(marke_id=marke_id).order_by('modelis')
                # self.fields['metai'].queryset = Metai.objects.filter(modelis_id=modelis_id).order_by('metai')
                # self.fields['spalva'].queryset = Spalva.objects.filter(modelis_id=modelis_id).order_by('spalva')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            # self.fields['modelis'].queryset = self.instance.country.marke_set.order_by('name')
            self.fields['modelis'].queryset = self.instance.marke.modelis_set.order_by('modelis')
            # self.fields['metai'].queryset = self.instance.modelis.metai_set.order_by('metai')
            # self.fields['spalva'].queryset = self.instance.modelis.spalva_set.order_by('spalva')

