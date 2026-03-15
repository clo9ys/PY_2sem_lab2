from src.models import Task
from dataclasses import dataclass
from random import randint
from src.logger import make_logger

logger = make_logger()

@dataclass
class ApiTask:
    """Данные задачи из API-заглушки. Содержит id и все возможные поля"""
    id: str
    type: str


class ApiTaskSource:
    """Имитирует внешний API. Возвращает задачи, как будто они пришли по сети"""
    def __init__(self, endpoint: str="http://api-stub/tasks"):
        self.endpoint = endpoint

    def get_tasks(self) -> list[Task]:
        api_tasks = [
            ApiTask(id="report67", type="report",),
            ApiTask(id="backup_52", type="backup",),
            ApiTask(id="msg13", type="send_message",),
        ]

        logger.info(f"Данные из API прочитаны, получено {len(api_tasks)} задач")
        return [Task(id=item.id, title=item.type, priority=randint(1, 10)) for item in api_tasks]