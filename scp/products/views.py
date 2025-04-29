from django.shortcuts import render
# Create your views here.

def product_view(request):
    return render(
        request = request,
        template_name = 'products.html',
    )


