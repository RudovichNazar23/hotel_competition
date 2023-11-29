from ..create_model_object import create_model_object


class CreateObjectOrGetNoneMixin:
    def create_object_or_get_none(self, form_data, form_class, files_upload: bool, file_key: str, form_file_field_key: str):
        if form_data:
            form_object = form_class(form_data, self.request.FILES) if files_upload is True else form_class(form_data)
            if form_object.is_valid():
                model_object = create_model_object(model=form_object.model, **form_data, **{form_file_field_key: self.request.FILES.get(file_key)})
                return model_object
        else:
            return None
