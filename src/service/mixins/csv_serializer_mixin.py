class CsvSerializerMixin:
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
    def get_model_value_list(obj: dict, related_model):
        model = [*obj.keys()][0]

        fields = obj[model]

        data = []

        for field in fields:
            data.append(related_model.__dict__[field])
        return data

    def sum_elements(self, lst: list):
        if not lst:
            return []
        else:
            return lst[0] + self.sum_elements(lst[1:])

    def create_data_rows(self, queryset_object, fields):
        data = []

        for model_object in queryset_object:
            data.append(
                self.sum_elements(
                    [
                        self.get_model_value_list(obj=self.get_model_fields(model_object.high_school, fields=fields),
                                                  related_model=model_object.high_school),
                        self.get_model_value_list(obj=self.get_model_fields(model_object.guardian, fields=fields),
                                                  related_model=model_object.guardian),
                        self.get_model_value_list(obj=self.get_model_fields(model_object.first_member, fields=fields),
                                                  related_model=model_object.first_member),
                        self.get_model_value_list(obj=self.get_model_fields(model_object.second_member, fields=fields),
                                                  related_model=model_object.second_member)
                    ]
                )
            )

        return data
