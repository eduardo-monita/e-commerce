from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.api.serializers import UserDetailSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = None

    def get_object(self):
        return self.request.user
