from lark import Lark, Transformer

grammar = """
    start: instruction+
    instruction: repeat | print | declare | procedure | step | conferment | comparator

    procedure: "procedure" step* "end procedure"
    step: "initiate and confirm step" name activity "end step;"
    repeat: "repeat" NUMBER instruction
    print: "log" double_quoted ";"
    STRING: /[a-zA-Z0-9_.-]{2,}/
    declare: "declare" variable* "end declare"
    variable: "variable" name "of type" type
    conferment: name ":=" double_quoted ";"
    comparator: "if value of" name "!=" name "then" activity "end if;"
    double_quoted: /"[^"]*"/
    name: STRING
    type: STRING
    activity: instruction*

    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
    %ignore ","
"""


class MyTransformer(Transformer):
    def declare(self, matches):
        return matches[0]

    def instruction(self, matches):
        return matches[0]

    def variable(self, matches):
        return f"{matches[0]} = {matches[1]}"

    def name(self, matches):
        return matches[0]

    def type(self, matches):
        if matches[0] == "integer":
            return "int()"
        elif matches[0] == "string":
            return "str()"

    def procedure(self, matches):
        return matches

    def step(self, matches):
        return matches

    def conferment(self, matches):
        return matches

    def comparator(self, matches):
        return matches

    def start(self, matches):
        return "\n".join(matches)


parser = Lark(grammar)

with open("in.pluto") as f:
    text = "\n".join(f.readlines()).strip()

tree = parser.parse(text)
#print(tree)

p_code = MyTransformer().transform(tree)
print(p_code)