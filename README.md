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
repeat 3 repeat 4 print 'hello world'
```

output is:

```
for _ in range(3):
    for _ in range(4):
        print('hello world')
```
For content in file "in.pluto" : 

```
procedure
	initiate and confirm step step1
		declare
			variable CMD_TM_LINK_VALUE of type string,
			variable TRSP2_RECEIVER_STATUS of type string
		end declare
		
		CMD_TM_LINK_VALUE := "TM FLOW";
		TRSP2_RECEIVER_STATUS := "TC tracking";
			
		if value of CMD_TM_LINK != CMD_TM_LINK_VALUE then
			log "There is no TM FLOW.";
		end if;

  	 	if NTR80220 != TRSP2_RECEIVER_STATUS then
			log "TRSP2 is " + NTR80220;
		end if;

	end step;

	initiate and confirm step step2
		initiate and confirm ZDW17001;
	end step;

end procedure
```

output is:
```
def procedure1():

	def step1():
		# initialization of variables
		CMD_TM_LINK_VALUE = str()
		TRSP2_RECEIVER_STATUS = str()
		
		CMD_TM_LINK_VALUE = "TM FLOW"
		TRSP2_RECEIVER_STATUS = "TC tracking"
		if CMD_TM_LINK.value != CMD_TM_LINK_VALUE:
			print("There is no TM FLOW.")
		if NTR80220 != TRSP2_RECEIVER_STATUS:
			print("TRSP2 is " + NTR80220)
	
	step1()
	
	def step2():
		ZDW17001()
	
	step2()
```
