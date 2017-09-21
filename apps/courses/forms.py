from django import forms
import re, md5

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d') #searches for a upper case followed by a number and the |(or operator) looks for a number then a upper case
# NAME_REGEX = re.compile(r'\W.*[A-Za-z]|[A-Za-z]\.*\W|\d.*[A-Za-z]|[A-Za-z].*\d')

class NewClass(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    desc = forms.CharField(label='Description', widget=forms.Textarea)
    def clean(self):
        cleaned_data = super(NewClass, self).clean()
        name = cleaned_data.get("name")
        desc = cleaned_data.get("desc")
        if len(name) < 5:
            msg = "Course name is too short!"
            self.add_error('name', msg)
        if len(desc) < 15:
            msg = "Description must be longer than 15 characters!"
            self.add_error('desc', msg)