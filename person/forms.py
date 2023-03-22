from django import forms
from .models import GodFather, ASEMUser, Worker, Child, SEX_TYPES, CORRESPONDENCE, Volunteer


class CreateNewGodFather(forms.ModelForm):
    class Meta:
        model = GodFather
        exclude = ['id']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'seniority': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'step': "0.01"}),
            'sex': forms.Select(attrs={'step': "0.01"}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewGodFather, self).__init__(*args, **kwargs)
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select border-class'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input border-class'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control border-class'})


class CreateNewASEMUser(forms.ModelForm):
    class Meta:
        model = ASEMUser
        exclude = ['id']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewASEMUser, self).__init__(*args, **kwargs)
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select border-class'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input border-class'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control border-class'})


class CreateNewWorker(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Worker
        exclude = ['id', 'last_login', 'is_active', 'is_admin', 'password']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewWorker, self).__init__(*args, **kwargs)
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select border-class'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input border-class'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control border-class'})

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
    correspondence = forms.ChoiceField(
        choices=CORRESPONDENCE, label="Correspondencia")

    class Meta:
        model = Child
        exclude = ['id']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'termination_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'sponsorship_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewChild, self).__init__(*args, **kwargs)
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select border-class'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input border-class'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control border-class'})


class CreateNewVolunteer(forms.ModelForm):
    class Meta:
        model = Volunteer
        exclude = ['id']
        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'contract_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'contract_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'dedication_time': forms.NumberInput(attrs={'step': "0.01"}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewVolunteer, self).__init__(*args, **kwargs)
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select border-class'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input border-class'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control border-class'})
