import csv, pandas as pd
import pytest
from src.pars import pars_csv,pars_xlsx


@pytest.fixture
def create_test_csv(tmp_path):
    file_path = tmp_path / "test.csv"
    test_data = [
        ["id", "status", "timestamp", "value"],
        ["650703", "EXECUTED", "2023-09-05T11:30:32Z", "16210"],
        ["16210", "EXECUTED", "2023-09-05T11:30:32Z", "16210"],
        ["650703", "EXECUTED", "2023-09-05T11:30:32Z", "650703"]
    ]
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(test_data)
    return file_path, test_data[1:]

def test_pars_csv_success(create_test_csv):
    file_path, expected_data = create_test_csv
    result = pars_csv(file_path)
    assert result == [
        dict(zip(["id", "status", "timestamp", "value"], row))
        for row in expected_data
    ]

def test_pars_csv_empty_file(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.touch()
    with pytest.raises(ValueError, match="Файл пустой или не содержит данных"):
        pars_csv(empty_file)

def test_pars_csv_file_not_found():
    with pytest.raises(FileNotFoundError, match="Файл non_existent_file.csv не найден"):
        pars_csv("non_existent_file.csv")


@pytest.fixture
def create_test_xlsx(tmp_path):
    file_path = tmp_path / "test.xlsx"
    test_data = pd.DataFrame({
        "heaader1": ["650703", "EXECUTED", "2023-09-05T11:30:32Z", "16210"],
        "heaader2": ["16210", "EXECUTED", "2023-09-05T11:30:32Z", "16210"],
        "heaader3": ["650703", "EXECUTED", "2023-09-05T11:30:32Z", "650703"],
    })
    test_data.to_excel(file_path, index=False)
    return file_path, test_data.to_dict(orient="records")

def test_pars_xlsx_success(create_test_xlsx):
    file_path, expected_data = create_test_xlsx
    result = pars_xlsx(file_path)
    assert result == expected_data

def test_pars_xlsx_file_not_found():
    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        pars_xlsx("non_existent_file.xlsx")

def test_pars_xlsx_invalid_file_format(tmp_path):
    invalid_file = tmp_path / "test.txt"
    invalid_file.write_text("Некорректный файл")
    with pytest.raises(Exception):
        pars_xlsx(invalid_file)

def test_pars_xlsx_empty_file(tmp_path):
    empty_file = tmp_path / "empty.xlsx"
    pd.DataFrame().to_excel(empty_file, index=False)
    with pytest.raises(ValueError, match="Файл пустой"):
        pars_xlsx(empty_file)