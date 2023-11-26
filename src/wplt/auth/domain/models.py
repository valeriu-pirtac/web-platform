from enum import Enum
from typing import List

from pydantic import BaseModel, EmailStr, Field, SecretStr, StrictBool, StrictStr


class UserRole(str, Enum):
    GUEST = "guest"
    ADMIN = "admin"


class BaseUser(BaseModel):
    email: EmailStr = Field(title="User email address")
    password: SecretStr | str = Field(title="User secret password")


class UserData(BaseUser):
    first_name: StrictStr | str = Field(title="Frst name", max_length=20)
    last_name: StrictStr | str = Field(title="Last name", max_length=20)
    user_role: List[UserRole] = Field(default=[UserRole.GUEST], title="User role")


class UserEntity(UserData):
    one_time_code: str = Field(title="One time registration code")
    account_enabled: StrictBool = Field(default=False, title="Is account enabled")
    password_expired: StrictBool = Field(default=False, title="Is password expired")
