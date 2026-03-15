from src.models import Task
from src.logger import make_logger

logger = make_logger()

class GenerationTaskSource:
    """Создает задачи программно с помощью цикла"""
    def __init__(self, count: int):
        self.count = count

    def get_tasks(self) -> list[Task]:
        tasks = [Task(id=str(i), title=f"task №{i}", priority=(i%10 + 1)) for i in range(1, self.count+1)]
        logger.info(f"Сгенерировано {len(tasks)} задач")
        return tasks