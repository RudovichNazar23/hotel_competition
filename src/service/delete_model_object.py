def delete_model_object(model, **kwargs):
    return model.objects.delete(**kwargs)


