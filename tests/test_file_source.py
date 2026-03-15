import json, pytest
from src.file_source import FileTaskSource
from src.models import ValidationError


def test_file_source_read_json(fs):
    file_path = "/data/tasks.json"
    fs.create_file(file_path, contents=json.dumps([
        {"id": "1", "title": "something1", "priority": 1},
        {"id": "2", "title": "something2", "priority": 2}
    ]))

    source = FileTaskSource(file_path)
    tasks = source.get_tasks()
    assert len(tasks) == 2
    assert tasks[0].id == "1" and tasks[1].id == "2"
    assert  tasks[0].title == "something1" and tasks[1].title == "something2"
    assert tasks[0].priority == 1 and tasks[1].priority == 2


def test_file_not_found_error():
    source = FileTaskSource("random/path")
    with pytest.raises(FileNotFoundError, match="не найден"):
        source.get_tasks()


def test_file_source_invalid_json(fs):
    file_path = "/data/invalid.json"
    fs.create_file(file_path, contents="this is not json")

    source = FileTaskSource(file_path)
    with pytest.raises(ValidationError, match="некорректный JSON"):
        source.get_tasks()