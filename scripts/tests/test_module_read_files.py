import pytest
from modules.module_read_files import read_files_excel

@pytest.mark.parametrize('path_file, expected', [
    ('D:\\runners_source_files\\notificaciones\\2023\\02\\01\\Fisico 01.02.2023.xls', int)
])
def test_read_files_excel(path_file, expected):
    assert len(read_files_excel(path_file)) == expected

    
