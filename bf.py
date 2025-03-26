#brainfuck interpreter

import sys
from time import sleep

class tape():
	
	def __init__(self):
		self.fulltape = [0] * 10
		self.index = 0
		self.currentvalue = self.fulltape[self.index]
		
	def incrementindex(self):
		if self.index < 29999:
			self.index = self.index + 1
		else:
			print("out of bounds error: tape has a maximum of 30000 cells")
			quit()
			
	def decrementindex(self):
		if self.index > 0:
			self.index = self.index - 1
		else:
			print("out of bounds error: tape does not wrap")
			quit()
			
	def incrementcell(self):
		self.currentvalue = self.fulltape[self.index]
		if self.currentvalue >= 255:
			self.currentvalue = 0
		else:
			self.currentvalue = self.currentvalue + 1
		self.fulltape[self.index] = self.currentvalue

	def decrementccell(self):
		self.currentvalue = self.fulltape[self.index]
		if self.currentvalue <= 0:
			self.currentvalue = 255
		else:
			self.currentvalue = self.currentvalue - 1
			print(f"currentvalue {self.currentvalue} cell value{self.fulltape[self.index]}")
		self.fulltape[self.index] = self.currentvalue
		
	def printcell(self):
		self.fulltape[self.index]
		sys.stdout.write(chr(int(self.currentvalue)))
		sys.stdout.flush()
		#sys.stdout.write(f"{int(self.currentvalue)}")
		#sys.stdout.flush()
	def fillcellbyascii(self, newcharacter):
		##TODO I HAVE NO IDEA HOW I DID THIS BUT THIS SHOULD BE TAKING ACTUAL KEYBOARD INPUT OR FILE INPUT NOT THE NEXXT CHAR IN THE BUFFER OOPS
		self.fulltape[self.index]
		if type(newcharacter) is str:
			if len(newcharacter) == 1:
				self.currentvalue = ord(newcharacter)
				self.fulltape[self.index] = self.currentvalue
			else:
				print("internal error: more than one character passed to fillcellbyascii")
				quit()
		else:
			print("internal error: non string passed to fillcellbyascii")
			quit()
			
class bfengine():
	
	def __init__(self):
		self.tape = tape()
		if len(sys.argv) == 2:
			self.bffile = open(sys.argv[1], "r")
			self.programbuffer = self.bffile.readlines()
		else:
			self.programbuffer = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."


		if type(self.programbuffer) is list:
			self.programbuffer = "".join(self.programbuffer)
		elif type(self.programbuffer) is not str:
			print("error: issues reading the bf file please ensure it is actually a brainfuck program")
		self.programbuffer = list(self.programbuffer)
		self.instructionindex = 0
		print(self.programbuffer)
		self.running = 1
		while self.running == 1:
			#sleep(1)
			self.tape.currentvalue = self.tape.fulltape[self.tape.index]
			if self.instructionindex == len(self.programbuffer):
				quit()
			self.instruction = self.programbuffer[int(self.instructionindex)]
			#print(f"insstruction:{self.instruction} instructionnindex: {self.instructionindex}")#debug
			#print(f"current cell:{self.tape.currentvalue} tape index: {self.tape.index}")#debug
			#print(self.tape.fulltape)
			if self.instruction == "<":
				self.tape.decrementindex()
			elif self.instruction == ">":
				self.tape.incrementindex()
			elif self.instruction == "+":
				self.tape.incrementcell()
			elif self.instruction == "-":
				self.tape.decrementccell()
			elif self.instruction == ".":
				self.tape.printcell()
			elif self.instruction == ",":
				self.tape.fillcellbyascii(self.programbuffer[self.instructionindex + 1])
			elif self.instruction == "[":
				if self.tape.currentvalue == 0:
					if self.instructionindex + 1 < len(self.programbuffer):
						self.instructionindex = self.instructionindex + 1
						self.instruction = self.programbuffer[self.instructionindex]
						openbrackets = 0
						while self.instruction != "]" and self.openbrackets == 0:
							if self.instruction =="[":
								openbrackets = openbrackets + 1
							elif self.instruction == "]":
								openbrackets = openbrackets - 1
							
							if self.instructionindex + 1 < len(self.programbuffer):
								self.instructionindex = self.instructionindex + 1
								self.instruction = self.programbuffer[self.instructionindex]
							else:
								print("syntax error: unmatched brackets")
								quit()

					else:
						print("syntax error: unmatched brackets")
						quit()

			elif self.instruction == "]":
				if self.tape.currentvalue != 0:
					if self.instructionindex > 0:
						self.instructionindex = self.instructionindex - 1
						self.instruction = self.programbuffer[self.instructionindex]
					else:
						print("syntax error: unmatched brackets")
						quit()
					closedbrackets = 0
					while self.instruction != "[" and closedbrackets == 0:
						if self.instruction == "]":
							closedbrackets = closedbrackets + 1
						elif self.instruction == "[":
							closedbrackets = closedbrackets - 1
						if self.instructionindex > 0:
							#print(f"in ] instructionindex: {self.instructionindex} instruction: {self.instruction}") #debug
							self.instructionindex = self.instructionindex - 1
							self.instruction = self.programbuffer[self.instructionindex]
						else:
							print("syntax error: unmatched brackets")
							quit()
			if self.instructionindex + 1 < len(self.programbuffer):

				self.instructionindex = self.instructionindex + 1
				self.instruction = self.programbuffer[self.instructionindex]
			else:
				self.running = 0
		print("program completed with no errors")
		print (self.tape.fulltape)
confused_serpent = bfengine()
