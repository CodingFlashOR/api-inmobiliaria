from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from apps.users.infrastructure.db import UserRepository
from .base import BaseUserSerializer
from apps.users.models import UserRoles
from apps.utils import ERROR_MESSAGES, ErrorMessagesSerializer


class SearcherUserProfileDataSerializer(ErrorMessagesSerializer):
    """
    Defines the fields that are required for the searcher user profile.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user_repository = UserRepository
        self.profile = None

    address = serializers.CharField(
        required=True,
        max_length=90,
        error_messages={
            "max_length": ERROR_MESSAGES["max_length"].format(
                max_length="{max_length}"
            ),
        },
    )
    phone_number = PhoneNumberField(
        required=True,
        max_length=25,
        error_messages={
            "invalid": ERROR_MESSAGES["invalid"],
            "max_length": ERROR_MESSAGES["max_length"].format(
                max_length="{max_length}"
            ),
        },
    )

    def validate_address(self, value: str) -> str:
        if not self.profile:
            self.profile = self._user_repository.get_profile_data(
                role=UserRoles.SEARCHER.value,
                address=value,
            )
        if self.profile.filter(address=value).exists():
            raise serializers.ValidationError(
                code="invalid_data",
                detail=ERROR_MESSAGES["address_in_use"],
            )

        return value

    def validate_phone_number(self, value: str) -> str:
        if not self.profile:
            self.profile = self._user_repository.get_profile_data(
                role=UserRoles.SEARCHER.value,
                phone_number=value,
            )
        if self.profile.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                code="invalid_data",
                detail=ERROR_MESSAGES["phone_in_use"],
            )

        return value


class SearcherUserSerializer(BaseUserSerializer):
    """
    Defines the fields that are required for the searcher user.
    """

    profile_data = SearcherUserProfileDataSerializer()
