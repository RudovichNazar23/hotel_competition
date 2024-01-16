
def get_model_object(model, **kwargs):
    return model.objects.get(**kwargs)
