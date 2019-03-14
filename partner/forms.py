from django.forms import TextInput, Textarea, ModelForm, ChoiceField
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField
from .models import Partner, Menu, CATEGORIES


class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = (
            "image_thumbnail",
            "category",
            "name",
            "contact",
            "address",
            "description",
            "category",
        )
        image_thumbnail = ProcessedImageField(
            spec_id="myapp:partner:image_thumbnail",
            processors=[Thumbnail(120, 120)],
            format='JPEG',
            options={'qulity': 60}
        )
        category = ChoiceField(choices=CATEGORIES)
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
