
def get_model_fields(model, context_name=None):
    fields = filter(lambda x: x.verbose_name != "ID", [field for field in model._meta.fields])

    model_fields = {}

    if context_name:
        model_fields[context_name] = fields
    else:
        model_fields[model.__name__.lower() + "_fields"] = fields

    return model_fields
