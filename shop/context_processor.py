from .models import Category


def categories(self):
    categories = Category.objects.all()

    return dict(categories=categories)
