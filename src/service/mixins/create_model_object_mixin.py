from service.create_model_object import create_model_object


class CreateModelObjectMixin:
    def create_object(self, model, form_data: dict, files_to_save=None):
        if files_to_save:
            model_object = create_model_object(
                model=model,
                **{files_to_save: self.request.FILES[files_to_save]},
                **form_data
            )
        else:
            model_object = create_model_object(
                model=model,
                **form_data
            )
        return model_object
