from lark import Lark, Transformer

grammar = """
    start: instruction+
    instruction: repeat | print
    
    repeat: "repeat" NUMBER instruction
    print: "print" STRING
    STRING: /'[^']*'/
    
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

parser = Lark(grammar)


class MyTransformer(Transformer):
    def repeat(self, matches):
        return f"for _ in range({matches[0]}):\n\t" + "\n\t".join(matches[1].split('\n'))

    def print(self, matches):
        return f"print({matches[0]})"

    def start(self, matches):
        return "\n".join(matches)

    def instruction(self, commands):
        return commands[0]


text = "repeat 10 repeat 10 print 'Hello World'"
tree = parser.parse(text)

new_tree = MyTransformer().transform(tree)
print(new_tree)
