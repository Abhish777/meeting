from django import forms

class meetingform(forms.Form):
    meetingid=forms.IntegerField(
        label="Enter Meeting Hall Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Hall Number'

            }
        )
    )
    meetingroom= forms.CharField(
        label="Enter Meeting Hall Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Hall Name'

            }
        )
    )
    meetingdescription = forms.CharField(
        label="Enter Meeting Hall Description",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Hall Name'

            }
        )
    )



class staffform(forms.Form):
    staffid=forms.IntegerField(
        label="Enter Staff ID Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Staff ID Number'

            }
        )
    )
    staffname= forms.CharField(
        label="Enter Meeting Hall Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Staff Name'

            }
        )
    )
    staffmail=forms.EmailField(
        label="Enter Meeting Description",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Staff Description'

            }
        )
    )


class bookingform(forms.Form):
    meetingid=forms.IntegerField(
        label="Enter Meeting Hall Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Hall Number'

            }
        )
    )
    staffid = forms.IntegerField(
        label="Enter Meeting Hall Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Hall Number'

            }
        )
    )
    bookingstartdate= forms.DateField(
        label="Enter Meeting Start Date",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Hall Name'

            }
        )
    )
    bookingenddate=forms.DateField(
        label="Enter Meeting End Date",
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'Booking End Date'

            }
        )
    )