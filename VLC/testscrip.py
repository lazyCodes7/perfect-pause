import os
def callVLC(isPlay):
	if(isPlay==True):
		os.system("python3 vlcscrip.py")
	else:
		print("No need to run anything else")
x = bool(input())
callVLC(x)

