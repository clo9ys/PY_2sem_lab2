from src.protocol import TaskSource
from src.file_source import FileTaskSource
from src.generation_source import GenerationTaskSource
from src.api_stub import ApiTaskSource

class FakeSource:
    pass

def test_protocol_detection():
    assert isinstance(FileTaskSource("random.json"), TaskSource)
    assert isinstance(GenerationTaskSource(0), TaskSource)
    assert isinstance(ApiTaskSource(), TaskSource)
    assert not isinstance(FakeSource(), TaskSource)