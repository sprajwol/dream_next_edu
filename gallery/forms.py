from django import forms
from django.core.validators import validate_image_file_extension


from gallery.models import Album, Image


class AlbumAdminForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('__all__')

    photos = forms.FileField(widget=forms.ClearableFileInput(
        attrs={"multiple": True}), label=("Add photos"), required=False,)
    # photos = forms.FileField(widget=forms.ClearableFileInput(
    #     attrs={"multiple": True}), label=("Add photos"))

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, show):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            image = Image(
                photo_album=show, image=upload)
            image.save()
