from helpers.freight_correios.client import Client
from helpers.freight_correios.package import Package
from helpers.freight_correios.constants import SEDEX_10, USABLE_SERVICES
from about_us.models import Company


def calculate_feight(product, destination_zip_code):
    package = Package(format=product.package.format)
    package.add_item(
        weight=product.package.weight,
        height=product.package.height,
        width=product.package.width,
        length=product.package.length
    )

    if Company.objects.first():
        client = Client(origin_zip_code=Company.objects.first().origin_zip_code)
        freights = []
        msg_erro = []
        for service in USABLE_SERVICES:
            if not (service[0] == SEDEX_10 and package.weight > 10):
                response_service = client.calc_price_deadline(package, destination_zip_code, service[0])
                if not response_service.price == 0:
                    freights.append({
                        "service": service[1],
                        "price": response_service.price,
                        "delivery_deadline": response_service.delivery_deadline
                    })
                elif response_service.msg_erro is not None:
                    msg_erro.append({
                        "service": service[1],
                        "error": response_service.msg_erro
                    })
        if not freights == []:
            return freights
        elif not msg_erro == []:
            return msg_erro
    return None
