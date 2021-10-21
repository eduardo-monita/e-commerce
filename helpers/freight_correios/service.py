from .utils import comma_separated_to_float, s_n_to_bool


class Service(object):

    code = None
    price = None
    delivery_deadline = None
    own_hand_value = None
    receivement_warning_value = None
    declared_value = None
    home_delivery = None
    delivery_saturday = None
    erro = None
    msg_erro = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if not hasattr(self.__class__, k):
                raise TypeError

            setattr(self, k, v)

    @classmethod
    def create_from_suds_object(cls, suds_object):
        return cls(
            code=str(suds_object.Codigo),
            price=comma_separated_to_float(suds_object.Valor),
            delivery_deadline=int(suds_object.PrazoEntrega),
            own_hand_value=comma_separated_to_float(suds_object.ValorMaoPropria),
            receivement_warning_value=comma_separated_to_float(suds_object.ValorAvisoRecebimento),
            declared_value=comma_separated_to_float(suds_object.ValorValorDeclarado),
            home_delivery=s_n_to_bool(suds_object.EntregaDomiciliar),
            delivery_saturday=s_n_to_bool(suds_object.EntregaSabado),
            erro=int(suds_object.Erro),
            msg_erro=suds_object.MsgErro
        )
