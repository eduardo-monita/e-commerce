import stripe
from stripe.api_resources import customer, customer_balance_transaction

stripe.api_key = "sk_test_51Jzhs2GmSz11SzxVHdg0vXuekpPWUbVMHtpdeGl5vsTABVM30HTywklrsUCuAoXiBhO87FpVD0KZe2HXzJ3sRak900aFtj5IRp"

# customer_create = stripe.Customer.create(
#     description="Test customer",
#     email="eduardo.monita.dias@gmail.com"
# )

# print("customer id:" + str(customer_create.id))

card_token = stripe.Token.create(
    card={
        "number": "5555555555554444",
        "exp_month": 11,
        "exp_year": 2022,
        "cvc": "314",
    },
)

# print("card toekn" + str(card_token.id))

# card = stripe.Customer.create_source(customer_create.id, source=card_token.id)

# print("card" + str(card))

charge = stripe.Charge.create(
    amount=400,
    currency="brl",
    source=card_token.id,
    description="Tetst charge",
)
print("charge" + str(charge))
