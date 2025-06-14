import pytest
import sys
import os
import importlib.util
from typing import List, Dict, Tuple, Set, Union, Any, Optional

def dynamic_import(module_name, file_path):
    abs_path = os.path.abspath(file_path)
    if module_name in sys.modules:
        del sys.modules[module_name]
    module = type(sys)(module_name)
    names = ['List', 'Dict', 'Tuple', 'Set', 'Union', 'Any', 'Optional']
    for name in names:
        if hasattr(__import__('typing'), name):
            setattr(module, name, getattr(__import__('typing'), name))
    sys.modules[module_name] = module
    spec = importlib.util.spec_from_file_location(module_name, abs_path)
    spec.loader.exec_module(module)
    return module

@pytest.fixture(scope="module")
def solution_fixture(request):
    module_name = f"src.{request.param}"
    file_path = f"src/{request.param}.py"
    return dynamic_import(module_name, file_path).Solution