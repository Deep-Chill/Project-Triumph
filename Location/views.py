from django.shortcuts import render
from .models import Country, Region

def Country_page(request, country_id):
    user = request.user
    country = Country.objects.get(id=country_id)
    context = {'country': country, 'region': country.region_set.all()}
    return render(request, 'Location/Country_page.html', context)

def region_page(request, region_code):
    user = request.user
    region = Region.objects.get(code=region_code)
    context = {'region': region, 'country': region.country}
    return render(request, 'Location/region_page.html', context)


# user = request.user
# region = Region.objects.get(id=region_id)
# context = {'region': region, 'country': region.country, 'region_code': region.code}
# return render(request, 'Location/region_page.html', context)