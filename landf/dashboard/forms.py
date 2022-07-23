from django import forms
from newsfeeds.models import Feeds

class AddPostForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('L', 'L'),
        ('F', 'F'),
        
    ]
    term = forms.BooleanField(required=True)
    status = forms.ChoiceField(
        required=True,
        choices=STATUS_CHOICES,
    )
    descriptions = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}))


    class Meta:
        model = Feeds
        fields = ('name',  
        'item_name', 
        'item_image', 
        'category', 
        'location',
         'time', 
         'descriptions',
        'status',
         'contact')

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['item_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['item_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['time'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['descriptions'].widget.attrs.update({'class': 'form-control'})