from django import forms

class CartForm(forms.Form):

	QUANTITY_PRODUCT = [(i,str(i)) for i in range(1,21)]

	quantity = forms.TypedChoiceField(choices=QUANTITY_PRODUCT , coerce=int)
	update = forms.BooleanField(required=False , widget=forms.HiddenInput , initial=False)
