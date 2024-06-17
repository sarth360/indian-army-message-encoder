from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Message')
    day_type = forms.ChoiceField(choices=[('odd', 'Odd'), ('even', 'Even')], label='Day Type')
