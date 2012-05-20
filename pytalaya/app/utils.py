
def get_or_none(model, **kargs):
    '''Get model instance (model.objects.get) or return None if no matching.'''
    try:
        return model.objects.get(**kargs)
    except model.DoesNotExist:
        return None
