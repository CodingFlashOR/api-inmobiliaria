from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)
from apps.users.domain.constants import SearcherUser
from apps.utils import ERROR_MESSAGES


CreateSearcherUserSchema = extend_schema(
    operation_id="create_searcher_user",
    tags=["Users"],
    responses={
        201: OpenApiResponse(
            description="**(CREATED)** User created correctly."
        ),
        400: OpenApiResponse(
            description="**(BAD_REQUEST)** The request data is invalid, error messages are returned for each field that did not pass validations.",
            response={
                "properties": {
                    "code": {"type": "string"},
                    "detail": {"type": "object"},
                }
            },
            examples=[
                OpenApiExample(
                    name="invalid_data",
                    summary="Invalid data",
                    description="These are the possible error messages for each field.",
                    value={
                        "code": "invalid_request_data",
                        "detail": {
                            "full_name": [
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                                ERROR_MESSAGES["invalid"],
                                ERROR_MESSAGES["max_length"].format(
                                    max_length=SearcherUser.FULL_NAME_MAX_LENGTH.value,
                                ),
                                ERROR_MESSAGES["name_in_use"],
                            ],
                            "email": [
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                                ERROR_MESSAGES["invalid"],
                                ERROR_MESSAGES["max_length"].format(
                                    max_length=SearcherUser.EMAIL_MAX_LENGTH.value,
                                ),
                                ERROR_MESSAGES["email_in_use"],
                            ],
                            "password": [
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                                ERROR_MESSAGES["invalid"],
                                ERROR_MESSAGES["max_length"].format(
                                    max_length=SearcherUser.PASSWORD_MAX_LENGTH.value,
                                ),
                                ERROR_MESSAGES["min_length"].format(
                                    min_length=SearcherUser.PASSWORD_MIN_LENGTH.value,
                                ),
                            ],
                            "confirm_password": [
                                "Este campo es requerido.",
                                "Este campo no puede estar en blanco.",
                                "Este campo no puede ser nulo.",
                                ERROR_MESSAGES["password_no_upper_lower"],
                                ERROR_MESSAGES["password_common"],
                                ERROR_MESSAGES["password_mismatch"],
                            ],
                            "profile_data": {
                                "address": [
                                    "Este campo es requerido.",
                                    "Este campo no puede estar en blanco.",
                                    "Este campo no puede ser nulo.",
                                    ERROR_MESSAGES["invalid"],
                                    ERROR_MESSAGES["max_length"].format(
                                        max_length=SearcherUser.ADDRESS_MAX_LENGTH.value,
                                    ),
                                    ERROR_MESSAGES["address_in_use"],
                                ],
                                "phone_number": [
                                    "Este campo es requerido.",
                                    "Este campo no puede estar en blanco.",
                                    "Este campo no puede ser nulo.",
                                    ERROR_MESSAGES["invalid"],
                                    ERROR_MESSAGES["max_length"].format(
                                        max_length=SearcherUser.PHONE_NUMBER_MAX_LENGTH.value,
                                    ),
                                    ERROR_MESSAGES["phone_in_use"],
                                ],
                            },
                        },
                    },
                ),
            ],
        ),
        500: OpenApiResponse(
            description="**(INTERNAL_SERVER_ERROR)** An unexpected error occurred.",
            response={
                "properties": {
                    "detail": {
                        "type": "string",
                    },
                    "code": {
                        "type": "string",
                    },
                }
            },
            examples=[
                OpenApiExample(
                    name="database_connection_error",
                    summary="Database connection error",
                    value={
                        "code": "database_connection_error",
                        "detail": "Unable to establish a connection with the database. Please try again later.",
                    },
                ),
            ],
        ),
    },
)
