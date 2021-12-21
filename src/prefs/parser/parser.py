# Libraries
import ast
import lark
import pkgutil
from lark.indenter import Indenter


class PrefsIndenter(Indenter):
    NL_type = "_NEWLINE"
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = "_INDENT"
    DEDENT_type = "_DEDENT"
    tab_len = 4


class PrefsTransformer(lark.Transformer):
    def process(self, data):
        return {ele[0]:(ele[1:] if len(ele) > 2 else ele[1]) for ele in data}

    def clean(self, data):
        for key, val in data.items():
            if isinstance(val, (tuple, list)):
                data[key] = self.process(val)
                self.clean(data[key])
        
        return data

    def to_dict(self, data):
        return self.clean(self.process(data))

    def start(self, x):
        return self.to_dict(x)

    def STRING(self, x):
        if x[0] == "b": # Bytes
            return ast.literal_eval(x)

        return x[1:-1]

    line = tuple
    value = lambda self, x: x[0]

    list = list
    set = set
    tuple = tuple
    dict = dict
    range = lambda self, x: range(*x)

    NONE = lambda self, x: None
    BOOL = lambda self, x: True if x == "True" else False
    KEY = lambda self, x: x.value

    INT = int
    FLOAT = float


def create_parser():
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

def parse(string=None, path=None, parser=None):
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
