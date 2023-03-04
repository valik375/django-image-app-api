from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


def validate_image_size(image):
    validate_image(image, 5242)


def validate_image(image, limit_kb):
    file_size = image.size
    if file_size > limit_kb * 1024:
        raise ValidationError(_("Max size of file is {} KB").format(limit_kb))
