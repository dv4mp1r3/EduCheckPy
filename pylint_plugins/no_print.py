# pylint_plugins/no_print.py
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from pylint.checkers.utils import check_messages

class NoPrintChecker(BaseChecker):
    __implements__ = IAstroidChecker
    name = "no-print"
    msgs = {
        "W5001": (
            "Use of print() is forbidden by policy",
            "print-used",
            "Запрет на использование print() в коде",
        ),
    }

    @check_messages("print-used")
    def visit_call(self, node: nodes.Call) -> None:
        if isinstance(node.func, nodes.Name) and node.func.name == "print":
            self.add_message("print-used", node=node)

def register(linter):
    linter.register_checker(NoPrintChecker(linter))
