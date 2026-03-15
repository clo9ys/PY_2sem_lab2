import json
from src.models import Task, ValidationError
from src.logger import make_logger

logger = make_logger()

class FileTaskSource:
    """Читает задачи из JSON-файла и превращает их в объекты Task"""

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_tasks(self) -> list[Task]:
        try:
            with open(self.filepath, 'r', encoding="utf-8") as f:
                data = json.load(f) # список словарей с задачами

            tasks = [Task(id=item["id"], title=item["title"], priority=item["priority"]) for item in data]
            logger.info(f"Файл {self.filepath} успешно прочитан, загружено {len(tasks)} задач")
            return tasks

        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.filepath} не найден")
        except json.JSONDecodeError:
            raise ValidationError(f"Файл {self.filepath} содержит некорректный JSON")
