from abc import ABC, abstractmethod
from core.application_data import ApplicationData


class BaseCommand(ABC):
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    @abstractmethod
    def execute(self):
        pass

