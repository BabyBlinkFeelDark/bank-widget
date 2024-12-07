import pytest
from src.decorators import log


def test_log(capsys):
    log()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"