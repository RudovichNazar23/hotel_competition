class GetFormDataMixin:
    def get_form_data(self, form_fields, keys_to_delete=None):
        form_data = {}
        for field in form_fields:
            form_data[field] = self.request.POST.get(field)

        if keys_to_delete and type(keys_to_delete) == list:
            for key in keys_to_delete:
                form_data.pop(key)
        return form_data
    
    def check_form_data(self, form_data: dict):
        for key in form_data:
            if not form_data[key]:
                return False
        return True
