import pytest
import yaml

def getdata():
    with open("./data.yml", encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
    return datas

class TestCal:

    @pytest.mark.parametrize('result,a,b', getdata()['add'])
    def test_add(self, info, result, a, b):
        assert result == info.add(a, b)

    @pytest.mark.parametrize('result,a,b', getdata()['sub'])
    def test_sub(self, info, result, a, b):
        assert result == info.sub(a, b)

    @pytest.mark.parametrize('result,a,b', getdata()['mul'])
    def test_mul(self, info, result, a, b):
        assert result == info.mul(a, b)

    @pytest.mark.parametrize('result,a,b', getdata()['div'])
    def test_div(self, info, result, a, b):
        if b==0:
            assert result=="被除数必须大于等于0"
        else:
            assert result == info.div(a, b)
