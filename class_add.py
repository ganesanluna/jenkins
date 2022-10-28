#!/usr/bin/env python3
class Calculator:
    def add(self, a, b) -> int:
        """
        :type : a: int
        :type : b: int
        """
        return a + b
    def sub(self, a:int, b:int) -> int:
        return a - b
    def mul(self, a:int, b:int) -> int:
        return a * b
    def div(self, a:int, b:int) -> float:
        return a / b
        
cal_obj = Calculator()
x = 10
y = 20
add = cal_obj.add(x, y)
sub = cal_obj.sub(x, y)
mul = cal_obj.mul(x, y)
div = cal_obj.div(x, y)
print(f"Adding : {add}\nSubtracting : {sub}\nMultiplication : {mul}\nDivision : {div}\n")