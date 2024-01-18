
def get_model_object(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except Exception as ex:
        return None
