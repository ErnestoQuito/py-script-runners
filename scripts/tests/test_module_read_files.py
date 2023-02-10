import pytest
from modules.module_read_files import read_files_excel
from modules.module_read_files import read_pdf_paginas

@pytest.mark.parametrize('path_file, expected', [
    ('D:\\runners_source_files\\notificaciones\\2023\\02\\01', 0)
])
def test_read_files_excel(path_file, expected):
    assert len(read_files_excel(path_file)) >= expected  


@pytest.mark.parametrize('path_file, expected', [
    ('D:\\runners_source_files\\notificaciones\\2023\\02\\01', 0)
])
def test_read_pdf(path_file, expected):
    assert len(read_pdf_paginas(path_file)) >= expected


