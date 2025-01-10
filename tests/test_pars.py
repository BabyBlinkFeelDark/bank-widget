import csv
import pytest
from src.pars import pars_csv

@pytest.fixture
def create_test_csv(tmp_path):
    file_path = tmp_path / "test.csv"
    test_data = [
        ["650703","EXECUTED","2023-09-05T11:30:32Z","16210"],
        ["16210","EXECUTED","2023-09-05T11:30:32Z","16210"],
        ["650703","EXECUTED","2023-09-05T11:30:32Z","650703"]
    ]
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(test_data)
    return file_path, test_data

def test_pars_csv_success(create_test_csv):
    file_path, expected_data = create_test_csv
    result = pars_csv(file_path)
    assert result == expected_data

def test_pars_csv_empty_file(tmp_path):
    empty_file = tmp_path / "heh.csv"
    empty_file.touch()  # Создаем пустой файл
    result = pars_csv(empty_file)
    assert result == []

def test_pars_csv_invalid_path():
    with pytest.raises(FileNotFoundError):
        pars_csv("alahamora.csv")