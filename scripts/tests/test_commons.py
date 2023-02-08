import pytest
from modules.commons import finder_files

@pytest.mark.parametrize('path_string, expected', [
    ('D:\\runners_source_files\\notificaciones\\2023\\02\\01', list)
])
def test_finder_files(path_string, expected):
    assert type(finder_files(path_string)) == expected
