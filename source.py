from lark import Lark, Transformer

grammar = """
    start: instruction+
    instruction: repeat | log | declare | procedure | step | assignment | ifstatement | ifstatement1 | initialization

    procedure: "procedure" step* "end procedure"
    step: "initiate and confirm step" name activity "end step;"
    initialization: "initiate and confirm" name";"
    repeat: "repeat" NUMBER instruction
    log: "log" double_quoted* "+"* name* ";"
    STRING: /[a-zA-Z0-9_.-]{2,}/
    declare: "declare" variable* "end declare"
    variable: "variable" name "of type" type
    assignment: name ":=" double_quoted ";"
    ifstatement: "if value of" name COMPARISON name "then" activity "end if;"
    ifstatement1: "if" name COMPARISON name "then" activity "end if;"
    double_quoted: /"[^"]*"/
    COMPARISON: ">="|"<="|">"|"<"|"=="|"!="
    
    
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
        return matches

    def declare(self, matches):
        out = "\t"
        for i in matches:
            out += str(i) + "\n\t"
        return "# initialization of variables\n" + out

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
        out = ""
        for i in matches:
            out += "\n\t".join(i.split("\n"))
        return "def procedure1():\n" + out

    def step(self, matches):
        out = f"\ndef {matches[0]}():\n\t"
        for i in matches[1:]:
            for j in i:
                out += str(j) + "\n" + "\t"
        return out[:-1] + f"\n{matches[0]}()\n"

    def assignment(self, matches):
        return f"{matches[0]} = {matches[1]}"

    def ifstatement(self, matches):
        return f"if {matches[0]}.value {matches[1]} {matches[2]}:\n\t\t{str(matches[3][0])}"

    def initialization(self, matches):
        return f"{matches[0]}()"

    def ifstatement1(self, matches):
        return f"if {matches[0]} {matches[1]} {matches[2]}:\n\t\t{str(matches[3][0])}"

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

with open("out.py", "w") as f:
    f.write(p_code)
