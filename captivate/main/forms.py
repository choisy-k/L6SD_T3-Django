from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="New List", max_length=300)
    check = forms.BooleanField(label="Completed?", required=False)