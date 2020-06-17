import pytest
import yaml
from pytestTestOne.cal import Calculator

@pytest.fixture()
def info():
    cal = Calculator()
    print("开始计算")
    yield cal
    print("计算结束")

#
# @pytest.fixture(scope='session')
# def getdata():
#     with open("./data.yml") as f:
#         datas=yaml.safe_load(f)
#     return datas
