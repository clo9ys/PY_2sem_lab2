import pytest
from src.models import Task, ValidationError, TaskStatus

@pytest.fixture
def task():
    return Task(id="1", title="something1", priority=1)

def test_priority_set(task):
    task.priority = 3
    assert task.priority == 3
    task.priority = 7
    assert task.priority == 7

@pytest.mark.parametrize("wrong_priority", [0, 11, "str", None])
def test_priority_validation_error(task, wrong_priority):
    with pytest.raises(ValidationError, match="Приоритет должен быть целым числом от 1 до 10"):
        task.priority = wrong_priority

def test_short_title(task):
    with pytest.raises(ValidationError, match="Слишком короткое описание задачи"):
        task.title = "123"

def test_set_status_wrong_status_error(task):
    with pytest.raises(ValidationError, match="Неизвестный статус задачи"):
        task.set_status("done")

def test_set_status_new_to_done(task):
    task.set_status(TaskStatus.NEW)
    with pytest.raises(ValidationError, match="Нельзя сменить статус"):
        task.set_status(TaskStatus.DONE)