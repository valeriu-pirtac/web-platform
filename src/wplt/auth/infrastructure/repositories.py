from abc import abstractmethod
from typing import Protocol, Tuple

from pydantic import UUID5

from wplt.auth.domain.models import BaseUser


class UserRepository(Protocol):
    @abstractmethod
    def find_users(self) -> Tuple[BaseUser, ...]:
        pass

    @abstractmethod
    def find_user(self, user_id: UUID5) -> BaseUser:
        pass

    @abstractmethod
    def save(self, user: BaseUser) -> None:
        pass

    @abstractmethod
    def delete(self, user_id: UUID5) -> None:
        pass
