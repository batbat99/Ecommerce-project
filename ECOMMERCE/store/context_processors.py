from .models import Category


def categories(request):
    """
    returns all the categories in the database
    """
    return {
        'categories': Category.objects.all()
    }
