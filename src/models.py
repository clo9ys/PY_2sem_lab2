from typing import Any
from enum import Enum
from src.logger import make_logger
from datetime import datetime

logger = make_logger()


class ValidationError(Exception):
    """Ошибка валидации данных или нарушения инвариантов"""
    pass


class TaskStatus(Enum):
    """Хранит статус задачи"""
    NEW = "new"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class PriorityDescriptor:
    """Data дескриптор для валидации приоритета"""
    def __set_name__(self, owner, name: str) -> None:
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner) -> Any:
        if instance is None: return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value) -> None:
        if not isinstance(value, int) or not (1 <= value <= 10):
            logger.error("Недопустимое значение нового приоритета")
            raise ValidationError("Приоритет должен быть целым числом от 1 до 10")

        setattr(instance, self.private_name, value)


class TaskLink:
    """Non-data дескриптор для генерации ссылки на задачу"""
    def __get__(self, instance, owner) -> Any:
        if instance is None:
            return self
        return f"http://some_link/for-task/{instance.id}"


class Task:
    """Модель задачи с использованием дескрипторов, инвариантов и инкапсуляции"""
    priority = PriorityDescriptor()
    link = TaskLink()

    def __init__(self, id: str, title: str, priority: int, status: TaskStatus = TaskStatus.NEW,):
        self.id = id
        self.title = title
        self.priority = priority
        self._status = status
        self._created_at = datetime.now()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, name) -> None:
        """Метод смены названия задачи"""
        if not name or len(name) < 4:
            logger.error(f"Слишком короткое название задачи: {name}")
            raise ValidationError("Слишком короткое название задачи")

        self._title = name

    @property
    def status(self) -> TaskStatus:
        return self._status

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def set_status(self, new_status: TaskStatus) -> None:
        """Метод смены статуса с проверкой инвариантов"""
        if new_status == TaskStatus.DONE and not self._title:
            logger.error(f"Завершение задачи без описания")
            raise ValidationError("Нельзя завершить задачу без описания")

        if not isinstance(new_status, TaskStatus):
            logger.error(f"Неизвестный статус задачи")
            raise ValidationError("Неизвестный статус задачи")

        if new_status == TaskStatus.DONE and self._status == TaskStatus.NEW:
            logger.error(f"Смена статуса новой задачи сразу на завершенный")
            raise ValidationError("Нельзя сменить статус новой задачи сразу на завершенный")

        self._status = new_status

    def __repr__(self) -> str:
        return f"Task(id={self.id}, priority={self.priority}, status={self._status.value}, created_at={self.created_at})"

    def __str__(self) -> str:
        return f"Задача №{self.id}: {self._title} [приоритет: {self.priority}]"