from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def categories(request):
    """
    returns all the categories in the database
    """
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    """
    renders the home template with all the products available in the databaase
    """
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    """
    renders a page showing all the details for a particular product
    """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})


def category_list(request, category_slug):
    """
    renders a page showing all products belonging to a particular category
    """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
