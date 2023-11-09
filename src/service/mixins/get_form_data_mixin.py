class GetFormDataMixin:
    def get_form_data(self, form_fields):
        form_data = {}
        for field in form_fields:
            form_data[field] = self.request.POST.get(field)
        return form_data
    
    def check_form_data(self, form_data: dict):
        for key in form_data:
            if not form_data[key]:
                return False
        return True
