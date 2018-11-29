import json

from django.http import HttpResponse


def index(request, zip_code):
    # todo: zip code to age distribution
    # todo: age distribution to report to specific product
    return HttpResponse(f"specific sport product for {zip_code}")













