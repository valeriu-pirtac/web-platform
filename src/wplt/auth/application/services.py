from abc import abstractmethod
from typing import Protocol

from wplt.auth.domain.models import BaseUser


class AuthService(Protocol):
    @abstractmethod
    def is_authenticated(self, user: BaseUser) -> bool:
        pass
