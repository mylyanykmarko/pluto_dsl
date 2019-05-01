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
	