from typing import Protocol, runtime_checkable
from src.models import Task

@runtime_checkable
class TaskSource(Protocol):
    """Протокол (контракт) источника задач. Любой источник должен иметь метод get_tasks, возвращающий список Task"""
    def get_tasks(self) -> list[Task]:
        """Возвращает список задач"""
        ...
