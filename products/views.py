from django.http import HttpResponse
from django.template import loader
from .models import Product, Category, Tag

def extract_filters_from_request(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category')
    tags = request.GET.getlist('tag')
    all_tag_ids = [tag_id for tag_id in tags]
    
    return search_query, category_id, all_tag_ids

def apply_product_filters(products, search_query, category_id, tag_id):
    if search_query:
        # Case-insensitive search in description
        products = products.filter(description__icontains=search_query)

    if category_id:
        products = products.filter(category_id=category_id)

    if tag_id:
        # Use in operator to filter products that have any of the selected tags
        products = products.filter(tags__id__in=tag_id)

    return products

def get_all_static_data():

    p = Product.objects.all()
    c = Category.objects.all()
    t = Tag.objects.all()

    return p, c, t

def product_list(request):
    template = loader.get_template('products/product_list.html')

    product_search_query, selected_category_id, selected_tag_ids = extract_filters_from_request(request)

    all_products, all_categories, all_tags = get_all_static_data()

    all_products = apply_product_filters(all_products, product_search_query, selected_category_id, selected_tag_ids)

    context = {
        'products': all_products,
        'categories': all_categories,
        'tags': all_tags,
    }

    return HttpResponse(template.render(context, request))