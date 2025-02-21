from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview, Wishlist, DiscountCode

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['review_text', 'rating']

    review_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review here...'}))
    rating = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)], widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['products']

    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)

# For future use
class DiscountCodeForm(forms.Form):
    code = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter discount code'}))

    def clean_code(self):
        code = self.cleaned_data['code']
        try:
            discount_code = DiscountCode.objects.get(code=code, active=True)
        except DiscountCode.DoesNotExist:
            raise forms.ValidationError("Invalid or inactive discount code.")
        return code
