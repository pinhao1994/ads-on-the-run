import json

from django.http import HttpResponse


def index(request, zip_code):
    """ ``GET http://<domain>/sports/<zip_code>``

    :param request: HTTP GET Request
    :type request: requests
    :param zip_code: zip code in NYC
    :type zip_code: str

    :return: list of sports products
    :rtype: list[str]
    """
    # todo: zip code to age distribution
    # todo: age distribution to report to specific product
    return HttpResponse(f"specific sport product for {zip_code}")













