import allure
import pytest
import yaml

#读取测试数据文件 calc.yml
#1、先定义数据文件
#2、定义一个方法，读取整个文件的内容， return 想要的数据格式

def get_datas():
    #只能load一次,第二次load为none
    with open("./datas/calc.yml",'r',encoding='UTF-8') as f:
        datas=yaml.safe_load(f)
    add_int_datas = datas.get("add").get("int").get("datas")
    add_int_ids = datas.get("add").get("int").get("ids")
    add_float_datas = datas.get("add").get("float").get("datas")
    add_float_ids = datas.get("add").get("float").get("ids")
    div_error_datas = datas.get("div").get("error").get("datas")
    div_error_ids = datas.get("div").get("error").get("ids")

    return (add_int_datas,add_int_ids,add_float_datas,add_float_ids,div_error_datas,div_error_ids)
#打印读取到数据
# def test_getdatas():
#       print(get_datas())


#通过fixture传递参数
@pytest.fixture(params=get_datas()[4],ids=get_datas()[5])
def  get_datas_byfixture(request):
     print(f"request.parm == {request.param}")
     return request.param

#打印get_datas_byfixture方法返回值
# def test_fixture(get_datas_byfixture):
#     print(get_datas_byfixture)

@allure.feature("计算器模块")
class TestCalc:
    @allure.story("加法计算参数int类型")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_datas()[0],ids=get_datas()[1])
    def test_add_int(self,get_calc,a,b,expect):
        result = get_calc.add(a,b)
        assert result==expect

    @allure.story("加法计算参数float类型")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", get_datas()[2], ids=get_datas()[3])
    def test_add_float(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert round(result,2) == expect

    #@pytest.mark.parametrize("a,b,expect",  get_datas()[4], ids=get_datas()[5])
    @allure.story("除法计算")
    @pytest.mark.run(order=1)
    def test_div(self,get_calc,get_datas_byfixture):
        try:
          result = get_calc.div(get_datas_byfixture[0],get_datas_byfixture[1])
        except ZeroDivisionError as e :
          result="ZeroDivisionError"
          print(result)
        except TypeError as e:
            result = "TypeError"
            print(result)

        assert result == get_datas_byfixture[2]

        allure.attach.file("./result2/b.png", attachment_type=allure.attachment_type.PNG)
