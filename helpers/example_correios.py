from freight_correios.client import Client
from freight_correios.package import Package
from freight_correios.constants import PACKAGE_OR_BOX, PAC

package = Package(format=PACKAGE_OR_BOX)

package.add_item(
    weight=1,
    height=12.0,
    width=32.0,
    length=32.0
)

client = Client(origin_zip_code='14026-596')

servicos = client.calc_price_deadline(package, '14840-000', PAC)
print(servicos[0])
print(servicos[0].code)
print(servicos[0].price)
print(servicos[0].delivery_deadline)
