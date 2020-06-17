class Calculator:

    # 加
    def add(self, a, b):
        return a + b

    # 减
    def sub(self, a, b):
        return a - b

    # 乘
    def mul(self, a, b):
        return a * b

    # 除
    def div(self, a, b):
        if b==0:
            return "被除数必须大于等于0"
        else:
            return a / b
