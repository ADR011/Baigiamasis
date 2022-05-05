from django import forms

# from .models import Person, City

from .models import Order, Modelis


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelis'].queryset = Modelis.objects.none()

        if 'marke' in self.data:
            try:
                marke_id = int(self.data.get('marke'))
                self.fields['modelis'].queryset = Modelis.objects.filter(marke_id=marke_id).order_by('modelis')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            # self.fields['modelis'].queryset = self.instance.country.marke_set.order_by('name')
            self.fields['modelis'].queryset = self.instance.marke.modelis_set.order_by('name')
