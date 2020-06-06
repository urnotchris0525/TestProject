from pythoncode.TestDemo import *

if __name__ == '__main__':
    #不带return的函数默认返回None，不能被打印，只能在函数内打印结果
    name = func_haveNoReturn("apple")
    #带有return的函数会将返回值返回给调用者灵活处理结果
    print(func_haveReturn("watermelon"))
    #传递参数
    print("my shape is "+func_haveArgs("square"))
    #无需传递参数，直接调用，返回默认值
    print("my color is "+func_haveNoArgs())