from django import forms
from .models import District, Branch, Person

class PersonForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all())
    branch = forms.ModelChoiceField(queryset=Branch.objects.none())
    
    class Meta:
        model = Person
        fields = '__all__'

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('cheque', 'Cheque'),
        ('debit', 'Debit Card'),
        ('credit', 'Credit Card'),
    )

    ACCOUNT_TYPE_CHOICES = (
        ('savings', 'Savings account'),
        ('current', 'Current account'),
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Name'
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        label='Date of Birth'
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Age'
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Gender'
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Phone Number'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Email'
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Address'
    )
    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='District'
    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select dropdown'}),
        label='Payment Method'
    )
    
    account_type = forms.ChoiceField(
        choices=ACCOUNT_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select dropdown'}),
        label='Account Type'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id)
            except (ValueError, TypeError):
                pass
