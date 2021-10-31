from suds.client import Client as SudsClient

from .constants import WSDL_URL
from .service import Service


def web_service_call(method_name):
    def wrapper(self, package, destination_zip_code, service):
        return self.call_web_service(method_name, package, destination_zip_code, service)
    return wrapper


class Client(object):

    def __init__(
        self, origin_zip_code, company_code='', password='', declared_value=0.0, own_hand=False,
        receivement_warning=False
    ):
        self.origin_zip_code = origin_zip_code
        self.company_code = company_code
        self.password = password
        self.declared_value = declared_value
        self.own_hand = own_hand
        self.receivement_warning = receivement_warning

    @property
    def ws_client(self):
        if not hasattr(self, '_ws_client'):
            self._ws_client = SudsClient(WSDL_URL)
        return self._ws_client

    def build_web_service_call_args(self, package, destination_zip_code, service):
        return (
            self.company_code,        # nCdEmpresa
            self.password,            # sDsSenha
            service,                  # nCdServico
            self.origin_zip_code,     # sCepOrigem
            destination_zip_code,     # sCepDestino
            package.weight,           # nVlPeso
            package.format,           # nCdFormato
            package.length,           # nVlComprimento
            package.height,           # nVlAltura
            package.width,            # nVlLargura
            0,                        # nVlDiametro
            self.own_hand,            # sCdMaoPropria
            self.declared_value,      # nVlValorDeclarado
            self.receivement_warning  # sCdAvisoRecebimento
        )

    def call_web_service(self, method_name, package, destination_zip_code, service):
        print("entrei call web service")
        args = self.build_web_service_call_args(package, destination_zip_code, service)
        print(args)
        result = getattr(self.ws_client.service, method_name)(*args)
        print(result)
        return [Service.create_from_suds_object(result.Servicos[0][i]) for i in range(len(result.Servicos[0]))][0]

    # calc_preco_data = web_service_call('CalcPrecoData')

    calc_price_deadline = web_service_call('CalcPrecoPrazo')

    # calc_prazo = web_service_call('CalcPrazo')

    # calc_preco = web_service_call('CalcPreco')

    # calc_prezo_prazo_data = web_service_call('CalcPrezoPrazoData')

    # calc_prazo_data = web_service_call('CalcPrecoData')
