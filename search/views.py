from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.models import Page
from blog.models import BlogPage  # ✅ import your BlogPage model

# To enable logging of search queries for use with the "Promoted search results" module # <https://docs.wagtail.org/en/stable/reference/contrib/searchpromotions.html> 
# uncomment the following line and the lines indicated in the search function 
# (after adding wagtail.contrib.search_promotions to INSTALLED_APPS):
# from wagtail.contrib.search_promotions.models import Query


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    if search_query:
        # ✅ Search only within your blog posts
        search_results = BlogPage.objects.live().search(search_query)

        # Optional: enable promoted results logging
        # query = Query.get(search_query)
        # query.add_hit()
    else:
        search_results = BlogPage.objects.none()

    # Pagination (10 results per page)
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )
