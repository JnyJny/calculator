"""
"""
from typing import Union, Callable
import operator
from collections import ChainMap


class Calculator:
    @property
    def binary_op_map(self):
        try:
            return self._binary_op_map
        except AttributeError:
            pass

        self._binary_opmap = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        return self._binary_opmap

    @property
    def unary_op_map(self):
        try:
            return self._unary_op_map
        except AttributeError:
            pass
        self._unary_op_map = {
            "~": operator.invert,
            "!": operator.neg,
        }
        return self._unary_op_map

    @property
    def op_map(self):
        try:
            return self._op_map
        except AttributeError:
            pass
        self._op_map = ChainMap(self.binary_op_map, self.unary_op_map)
        return self._op_map

    def is_binary_operation(self, op):
        return op in self.binary_op_map.values()

    def is_unary_operation(self, op):
        return op in self.unary_op_map.values()


class InfixCalculator(Calculator):
    pass


class StackUnderflow(Exception):
    def __str__(self):
        return "Stack Underflow Occurred"


class RPNCalculator(Calculator):
    def __init__(self):
        self.stack = []

    def __str__(self):

        if not self.stack:
            return "<EMPTY>"

        return "\n".join(map(str, reversed(self.stack)))

    def push(self, value: str) -> None:
        """
        """
        op = self.op_map.get(value)
        if op:
            value = op
        else:
            value = float(value)

        self.stack.append(value)

    def pop(self) -> Union[float, Callable]:
        """
        """
        try:
            return self.stack.pop(-1)
        except IndexError:
            raise StackUnderflow() from None

    def execute(self) -> Union[float, None]:
        """
        """
        while self.stack:
            op = self.pop()
            if isinstance(op, float):
                return op

            a = self.pop()
            if not isinstance(a, float):
                raise ArithmeticError("Expected value on top of stack", a)

            if self.is_unary_operation(op):
                self.push(op(a))
                continue

            if self.is_binary_operation(op):
                b = self.pop()
                self.push(op(a, b))
                continue

            raise ArithmeticError("Unknown operation", op)
