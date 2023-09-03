from django.shortcuts import render
from store.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request):
    products = Product.objects.all().filter(is_special=True).order_by('id')
    product_count = products.count()

    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    product_count = products.count()

    context = {
        'products': paged_products,
        'p_count': product_count,
    }

    return render(request, 'home.html', context)


def about(request):
    bio = {
        'name': 'Saumik Das',
        'status': 'Intermidiate Programmer',
        'skils': 'C/C++, Python, MySQL, Django',
    }
    return render(request, 'about.html', bio)
