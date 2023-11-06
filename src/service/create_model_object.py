def create_model_object(model, **kwargs):
    return model.objects.create(**kwargs)
