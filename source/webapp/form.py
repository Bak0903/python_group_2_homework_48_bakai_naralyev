from django import forms
from webapp.models import Food, OrderFood, Order


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'description', 'photo', 'price')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-sm-10'}),
            'description': forms.Textarea(attrs={'class': 'form-control col-sm-10'}),
            'price': forms.NumberInput(attrs={'class': 'form-control col-sm-10' }),
        }


# class OrderFoodForm(forms.ModelForm):
#     class Meta:
#         model = OrderFood
#         fields = ('food', 'amount')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['contact_name', 'contact_phone', 'delivery_address']


class OrderfoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        exclude = ['order']




