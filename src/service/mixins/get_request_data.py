class RequestObjectDataMixin:
    def get_form_request_keys(self):
        return [*filter(lambda x: x, [*self.request.POST.keys()][1:])]

    def get_form_request_values(self):
        return [*filter(lambda x: x, [*self.request.POST.values()][1:])]
