from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView
)
from rest_auth.registration.views import RegisterView
from accounts.api.views import (
    UserDetailsView,
    CartView,
    ProductCartView,
    UserFavoriteView,
    UserShoppedView,
    UserAccessedView,
    UserAddressesView
)

""" Main router """
router = routers.SimpleRouter()
router.register("cart", CartView, basename="user_cart")
router.register("favorites", UserFavoriteView, basename="user_favorites")
router.register("shopped", UserShoppedView, basename="user_shopped")
router.register("accessed", UserAccessedView, basename="user_accessed")
router.register("addresses", UserAddressesView, basename="user_addresses")

""" ProductCart router """
product_cart_router = nested_routers.NestedSimpleRouter(router, r'cart', lookup='cart')
product_cart_router.register(r'products', ProductCartView, basename='products')

urlpatterns = [
    url(r"^password/reset/$", PasswordResetView.as_view(), name="password_reset"),
    url(r"^password/reset/confirm/$", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    url(r"^login/$", LoginView.as_view(), name="account_login"),
    url(r"^registration/$", RegisterView.as_view(), name="account_signup"),

    # URLs that require a user to be logged in with a valid session / token.
    url(r"^logout/$", LogoutView.as_view(), name="account_logout"),
    url(r"^user/$", UserDetailsView.as_view(), name="user_details"),
    url(r"^password/change/$", PasswordChangeView.as_view(), name="password_change"),
    url(r"^user/", include(router.urls)),
    url(r"^", include(product_cart_router.urls))
]
