import datetime
from django import forms
from .models import GodFather, ASEMUser, Worker, Child, SEX_TYPES, CORRESPONDENCE,Volunteer

class CreateNewGodFather(forms.ModelForm):
    class Meta:
        model = GodFather
        fields = ['dni','name','surname','email','birth_date','sex','city',
                  'address','telephone','postal_code', 'payment_method',
                  'bank_account_number','bank_account_holder','bank_account_reference',
                  'amount','frequency','seniority','notes','status']
        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.date.today}, format='%Y-%m-%d'),
            'seniority': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.date.today}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01"}),
        }

class CreateNewASEMUser(forms.ModelForm):
    class Meta:
        model = ASEMUser
        exclude = ['id']


class CreateNewWorker(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Worker
        exclude = ['id', 'last_login', 'is_active','is_admin','password']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CreateNewWorker, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CreateNewChild(forms.ModelForm):
    sex = forms.ChoiceField(choices=SEX_TYPES, label="Género")
    correspondence = forms.ChoiceField(choices=CORRESPONDENCE, label="Correspondencia")

    class Meta:
        model = Child
        exclude = ['id']
        
class CreateNewVolunteer(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name','surname','email','birth_date','sex','city',
                  'address','telephone','postal_code','photo','job','dedication_time','contract_date']
        widgets = {
            'contract_date': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.date.today}, format='%Y-%m-%d'),
        }