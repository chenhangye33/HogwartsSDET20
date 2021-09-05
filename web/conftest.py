#数据共享：公共数据或方法
from typing import List
import pytest
from pytest_exerice.pythocode.calculator import Calculator
from web.page_object.index_page import IndexPage

"""
1、conftest.py 不需要导入，直接使用
2、名字是固定的，pytest会自动识别这个文件
3、将conftest.py放在项目的根目录下
4、conftest.py结合fixture
"""

# @pytest.fixture(autouse=True,scope="class")
# def get_index():
#     print("index实例化开始")
#     index = IndexPage()
#     yield index
#     print("index实例化结束")
#


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    #遍历所有的用例
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')







