from django import forms

class DocumentForm(forms.Form):
  title = forms.CharField(max_length=100) 
  docfile = forms.FileField(
    label='Select a file'
  )
