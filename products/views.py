from django.http import HttpResponse
from django.template import loader
from .models import Product, Category, Tag

def extract_filters_from_request(request):
    """
    Parse the GET parameters from the request to extract the search query, selected category, and selected tags.
    """
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category')
    tags = request.GET.getlist('tag') # getlist is used to get multiple values for the same key (in this case multiple selected tags)
    all_tag_ids = [tag_id for tag_id in tags]
    
    return search_query, category_id, all_tag_ids

def apply_product_filters(products, search_query, category_id, tag_id):
    """
    Filters the products queryset based on the search query, selected category, and selected tags.
    """
    if search_query:
        # Case-insensitive search in description
        products = products.filter(description__icontains=search_query)

    if category_id:
        products = products.filter(category_id=category_id)

    if tag_id:
        # Use in operator to filter products that have any of the selected tags
        products = products.filter(tags__id__in=tag_id).distinct() # If a product has multiple of the selected tags, we only want to show it once

    return products

def get_all_static_data():
    """
    Retrieve all products, categories, and tags from the database.
    """
    p = Product.objects.filter(active=True) # Only show active products
    c = Category.objects.all()
    t = Tag.objects.all()

    return p, c, t

def product_list(request):
    # Load the template
    template = loader.get_template('products/product_list.html')

    # Extract filters from the request
    product_search_query, selected_category_id, selected_tag_ids = extract_filters_from_request(request)

    # Get all products, categories, and tags
    all_products, all_categories, all_tags = get_all_static_data()

    # Apply filters to the products queryset
    all_products = apply_product_filters(all_products, product_search_query, selected_category_id, selected_tag_ids)

    context = {
        'products': all_products,
        'categories': all_categories,
        'tags': all_tags,
        'selected_tags': selected_tag_ids,
    }

    return HttpResponse(template.render(context, request))