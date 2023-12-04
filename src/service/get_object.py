
def get_model_object(model, **kwargs):
    try:
        return model.object.get(**kwargs)
    except Exception as ex:
        print(ex)
        return None
