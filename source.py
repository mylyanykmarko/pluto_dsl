from lark import Lark, Transformer

grammar = """
    start: instruction+
    instruction: repeat | log | declare | procedure | step | conferment | comparator | comparator1

    procedure: "procedure" step* "end procedure"
    step: "initiate and confirm step" name activity "end step;"
    repeat: "repeat" NUMBER instruction
    log: "log" double_quoted* "+"* name* ";"
    STRING: /[a-zA-Z0-9_.-]{2,}/
    declare: "declare" variable* "end declare"
    variable: "variable" name "of type" type
    conferment: name ":=" double_quoted ";"
    comparator: "if value of" name "!=" name "then" activity "end if;"
    comparator1: "if" name "!=" name "then" activity "end if;"
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
    def activity(self, matches):
        #print(len(matches))
        return matches

    def declare(self, matches):
        return str(matches[0])

    def instruction(self, matches):
        return str(matches[0])

    def variable(self, matches):
        return f"{matches[0]} = {matches[1]}"

    def name(self, matches):
        return str(matches[0])

    def type(self, matches):
        if matches[0] == "integer":
            return "int()"
        elif matches[0] == "string":
            return "str()"

    def procedure(self, matches):
        return str(matches[0])

    def step(self, matches):
        out = f"def {matches[0]}():\n\t"
        for i in matches[1:]:
            for j in i:
                out += str(j) + "\n" + "\t"
        return out

    def conferment(self, matches):
        return f"{matches[0]} = {matches[1]}"

    def comparator(self, matches):
        return f"if {matches[0]} != {matches[1]}:\n\t\t{str(matches[2][0])}"

    def comparator1(self, matches):
        return f"if {matches[0]} != {matches[1]}:\n\t\t{str(matches[2][0])}"

    def log(self, matches):
        out = ""
        for i in matches:
            out += i + " + "
        if out[-3:] == " + ":
            out = out[:-3]
        return f"print({out})"

    def double_quoted(self, matches):
        return str(matches[0])

    def start(self, matches):
        return matches[0]


parser = Lark(grammar)

with open("in.pluto") as f:
    text = "\n".join(f.readlines()).strip()

tree = parser.parse(text)

p_code = MyTransformer().transform(tree)
print(p_code)
