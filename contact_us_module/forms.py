from django import forms
from .models import ContactUsModel


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = "__all__"
        widgets = {
            "name": forms.widgets.TextInput(attrs={
                "id": "name",
                "type":"text",
                "placeholder":"نام"
            }),
            "phone_number": forms.widgets.TextInput(attrs={
                "id": "phone",
                "type": "text",
                "placeholder":"تلفن"

            }),
            "subject": forms.widgets.TextInput(attrs={
                "id": "subject",
                "type": "text",
                "placeholder":"موضوع"

            }),
            "email": forms.widgets.EmailInput(attrs={
                "id": "email",
                "type": "text",
                "placeholder":"ایمیل"

            }),
            "text": forms.widgets.Textarea(attrs={
                "id": "message",
                "placeholder":"متن پیام"
            })
        }

    def is_valid(self):


        super().is_valid()
