# Pluto DSL in Python

### Summary 
 
This is a solution to a warmup challenge for Pluto DSL in Python.
It is made using [Lark parser](https://github.com/lark-parser/lark).

This program takes PLUTO's code as an input and returns valid Python code.

### Running

```
python3 source.py
```

This will print the python alternative for a code provided in `in.pluto`.

You can execute the python code immediately with the following command:

```
python3 source.py | python3
```

### Examples

For content in file "in.pluto" : 

```
repeat 10 print 'hello world'
```

output is:

```
for _ in range(10):
    print('hello world')
```
---

For content in file "in.pluto" : 

```
Content in file "in.pluto" : repeat 3 repeat 4 print 'hello world'
```

output is:

```
for _ in range(3):
    for _ in range(4):
        print('hello world')
```
