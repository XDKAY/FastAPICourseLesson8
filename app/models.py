__all__ = ("FeedackRequestScheme", "FeedackResponseScheme", )


from typing import Annotated, Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator
)


class Contact(BaseModel):
    email: EmailStr
    phone: Annotated[Optional[str], Field(min_length=7, max_length=15)] = None

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:
        if value.startswith("+"):
            value = value.replace("+", "")

        if not value.isdigit():
            raise ValueError("Номер телефона должен содержать только цифры")

        return value


class FeedackRequestScheme(BaseModel):
    username: Annotated[str, Field(min_length=2, max_length=50)]
    message: Annotated[str, Field(min_length=10, max_length=500)]
    contact: Contact

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        for word in (
            "редиска", "редиске", "редиску", "редиской", "редиски",
            "бяка", "бякой", "бяку", "бяке", "бяки",
            "козявка", "козявкой", "козявке", "козявку", "козявки"
        ):
            if word in value:
                raise ValueError("Использование недопустимых слов")

        return value


class FeedbackResponseScheme(BaseModel):
    message: str
