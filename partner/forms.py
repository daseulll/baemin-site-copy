from django.forms import TextInput, Textarea, ModelForm
from imagekit.forms import ProcessedImageField
from imagekit.processors import Thumbnail
from .models import Partner, Menu

# class User(forms.Form):
#     class Meta:


class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = (
            "image_thumbnail",
            "name",
            "contact",
            "address",
            "description",
        )
        image_thumbnail = ProcessedImageField(
            spec_id="myapp:partner:image_thumbnail",
            processors=[Thumbnail(120,120)],
            format='JPEG',
            options={'qulity': 60}
        )
        widgets = {
            "name" : TextInput(attrs={"class":"form-control"}),
            "contact" : TextInput(attrs={"class":"form-control"}),
            "address" : TextInput(attrs={"class":"form-control"}),
            "description" : Textarea(attrs={"class":"form-control"}),
        }

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = (
            "image",
            "name",
            "price",
        )
        widgets = {
            # "image" : TextInput(attrs={"class":"form-control"}),
            "name" : TextInput(attrs={"class":"form-control"}),
            "price" : TextInput(attrs={"class":"form-control"}),
        }
