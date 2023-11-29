class GetFormDataOrNoneMixin:
    def get_form_data_or_none(self, request_keys: list, form_keys: list):

        form_data = {}

        test = dict(zip(request_keys, form_keys))

        for key in test:
            form_data[test[key]] = self.request.POST.get(key)
        return self._check_form_data_is_none(form_data)

    @staticmethod
    def _check_form_data_is_none(form_data: dict):
        return None if not any(form_data.values()) else form_data
