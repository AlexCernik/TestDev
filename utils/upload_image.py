def upload_image(instance, filename):
    try:
        instance._meta.model.objects.get(id=instance.id).image.delete(save=False)
        return f'images/{filename}'
    except:
        return f'images/{filename}'