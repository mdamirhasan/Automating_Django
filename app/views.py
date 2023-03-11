from django.shortcuts import render

from .models import Contact

# Create your views here.
def contact_list_view(request):
    contact = Contact.objects.filter()
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "contact_list.html",{"contact":contact})