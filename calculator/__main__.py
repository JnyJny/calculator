from typer import Typer

from .model import InfixCalculator
from .model import RPNCalculator
from .model import StackUnderflow


infix_cli = Typer()


@infix_cli.command()
def infix_main():
    """Infix Notation Calculator
    """
    raise NotImplementedError("infix_main")


rpn_cli = Typer()


@rpn_cli.command()
def rpn_main():
    """Reverse Polish Notation Calculator

    """

    calc = RPNCalculator()

    while True:

        cmd = input("CMD [?]: ")

        cmd = cmd.casefold()

        if not cmd:
            continue

        if cmd == "?":
            print(" ? -> this help")
            print(" # -> print stack")
            print(" . -> execute and print result")
            print(" c -> clear stack")
            print(" x -> exit")
            continue

        if cmd[0] in ["x", "q"]:
            break

        if cmd[0] == "#":
            print(calc)
            continue

        if cmd[0] == "c":
            calc.stack.clear()
            print("Stack cleared.")
            continue

        if cmd[0] in [" ", "."]:
            try:
                snapshot = str(calc)
                result = calc.execute()
                calc.push(result)
                print(calc)
            except StackUnderflow as error:
                print(f"ERROR: {error}")
                for line in snapshot.splitlines():
                    print(f"ERR STK> {line}")
            continue

        try:
            calc.push(cmd)
        except ArithmeticError as error:
            print(f"ERROR: {error}")
        except ValueError as error:
            print(f"INVALID: {error}")
