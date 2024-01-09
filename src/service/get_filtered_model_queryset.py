
def get_filtered_model_queryset(model, **kwargs):
    return model.objects.filter(**kwargs)
