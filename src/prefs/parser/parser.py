import ast
import pkgutil
import lark
from lark.indenter import Indenter


class PrefsIndenter(Indenter):
    NL_type = "_NEWLINE"
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = "_INDENT"
    DEDENT_type = "_DEDENT"
    tab_len = 4


class PrefsTransformer(lark.Transformer):
    def nested(self, x):
        return x[0], dict(x[1:])

    start = dict
    pair = tuple
    value = lambda self, x: x[0]

    list = list
    set = set
    tuple = tuple
    dict = dict
    range = lambda self, x: range(*x)

    NONE = lambda self, x: None
    BOOL = lambda self, x: True if x == "True" else False
    KEY = lambda self, x: x.value
    STRING = lambda self, x: ast.literal_eval(x)

    INT = int
    FLOAT = float


def create_parser() -> lark.Lark:
    if __name__ == "__main__":
        with open("grammar.lark", "r") as file:
            grammar = file.read()
    else:
        grammar = pkgutil.get_data(__name__, "grammar.lark").decode()

    parser = lark.Lark(
        grammar,  
        parser="lalr", 
        postlex=PrefsIndenter(), 
        transformer=PrefsTransformer(), 
    )

    return parser

def parse(string=None, path=None, parser=None) -> dict:
    if (string is None and path is None) or (string is not None and path is not None):
        raise ValueError("One of 'string' and 'path' paramters must be specified, neither both nor none.")

    if parser is None:
        parser = create_parser()

    if string is None:
        with open(path, "r") as file:
            string = file.read()

    if string.strip() == "":
        return {}

    string += "\n" # After the end of the string there has to be a new line

    try:
        return parser.parse(string)
    except lark.exceptions.UnexpectedToken as error:
        raise SyntaxError(
            f"Invalid syntax at line {error.line}, column {error.column}{f' in {path}' if path is not None else ''}. Got {error.token.type!r}, expected one of {error.expected}"
        )
