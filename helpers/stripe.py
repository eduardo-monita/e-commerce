import stripe
from django.conf import settings
from rest_framework.exceptions import ValidationError

###
# API KEY
###
stripe.api_key = settings.STRIPE_SECRET_KEY


###
#
###
class Stripe(object):

    def gen_card_token(self, number, exp_month, exp_year, cvc):
        card_token = stripe.Token.create(
            card={
                "number": number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc,
            },
        )
        return card_token.id

    def create_charge(self, token, price, description):
        charge = stripe.Charge.create(
            amount=int(price*100),
            currency="brl",
            source=token,
            description=description,
        )
        return charge
