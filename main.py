import json
from src import FileTaskSource, GenerationTaskSource, ApiTaskSource
from src.models import ValidationError
from src.protocol import TaskSource
from src.logger import make_logger

logger = make_logger()

def process_task(source) -> None:
    """Проверяет источник, получает задачи и печатает их. Если источник не подходит, выбрасывает ошибку"""
    if not isinstance(source, TaskSource):
        raise TypeError(f"Объект не реализует единый контракт - отсутствует метод get_tasks()")

    tasks = source.get_tasks()
    for task in tasks:
        logger.info(f'{task.id}: {task.title} [приоритет: {task.priority}]')
        print(f'Выполнение задачи {task.id}: {task.title} [приоритет: {task.priority}]')

if __name__ == "__main__":
    tasks = [
        FileTaskSource("tasks.json"),
        GenerationTaskSource(5),
        ApiTaskSource(),
    ]
    try:
        for source in tasks:
            process_task(source)
    except FileNotFoundError as err:
        logger.error(err)
        print(err)
    except json.JSONDecodeError as err:
        logger.error(err)
        print(err)
    except TypeError as err:
        logger.error(err)
        print(err)
    except ValidationError as err:
        logger.error(err)
        print(err)
    except Exception as err:
        logger.error(err)
        print(err)