from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .get_model_object import get_model_object


def get_model_object_by_uidb(model, uidb64):
    pk = urlsafe_base64_decode(force_str(uidb64))
    model_object = get_model_object(model=model, pk=pk)

    return model_object
