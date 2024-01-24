class TestMixin:
    @staticmethod
    def get_model_fields(model, fields: list):
        result = {model: []}

        for field in fields:
            try:
                model._meta.get_field(field)
                result[model].append(field)
            except Exception as ex:
                continue
        return result

    @staticmethod
    def get_model_value_list(obj: dict):
        model = [*obj.keys()][0]

        if not obj[model]:
            return []

        model_data = model.objects.values_list(*obj[model])
        return list(model_data)

    def sum_elements(self, lst: list):
        if not lst:
            return ()
        else:
            return lst[0] + self.sum_elements(lst[1:])

    def create_data_rows(self, *args):
        args = list(args)
        filtered_args = [*filter(lambda x: x, args)]

        result = []

        for pare in zip(*filtered_args):
            result.append(self.sum_elements(pare))
        return result

