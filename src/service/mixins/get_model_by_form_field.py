class GetModelByFormFieldMixin:
    @staticmethod
    def _get_form_class_by_field(form_class, field_name: str):
        try:
            return form_class.__dict__["fields"][field_name]
        except Exception as ex:
            return None

    def get_model_by_field(self, form_classes: list, field):
        for form_class in form_classes:
            if self._get_form_class_by_field(form_class=form_class, field_name=field):
                return form_class.model
            else:
                continue
