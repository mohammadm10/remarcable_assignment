from django.http import HttpResponse
from django.template import loader
from .models import Product, Category, Tag

def extract_filters_from_request(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')

    return search_query, category_id, tag_id

def product_list(request):
    template = loader.get_template('products/product_list.html')

    product_search_query, selected_category_id, selected_tag_id = extract_filters_from_request(request)

    print(f"Search Query: {product_search_query}, Category ID: {selected_category_id}, Tag ID: {selected_tag_id}")

    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    all_tags = Tag.objects.all()

    context = {
        'products': all_products,
        'categories': all_categories,
        'tags': all_tags,
    }

    return HttpResponse(template.render(context, request))