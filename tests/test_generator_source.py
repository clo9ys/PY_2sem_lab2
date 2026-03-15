from src.generation_source import GenerationTaskSource

def test_generator_tasks():
    source = GenerationTaskSource(5)
    tasks = source.get_tasks()
    assert len(tasks) == 5
    for i, task in enumerate(tasks, start=1):
        assert task.id == str(i) and task.title == f"task №{i}" and task.priority == (i % 10 + 1)