#brainfuck interpreter
import numpy
import sys
class tape():
	
	def __init__(self):
		self.fulltape = numpy.zeros(30000)
		self.pointer = 0
		self.currentvalue = self.fulltape[self.pointer]
		
	def incrementpointer(self):
		if self.pointer < 29999:
			self.pointer = self.pointer + 1
		else:
			print("out of bounds error: tape has a maximum of 30000 cells")
			quit()
			
	def decrementpointer(self):
		if self.pointer > 0:
			self.pointer = self.pointer - 1
		else:
			print("out of bounds error: tape does not wrap")
			quit()
			
	def incrementcell(self):
		self.currentvalue = self.currentvalue + 1
	
	def decrementccell(self):
		if self.currentvalue > 0:
			print("value error: cells cannot go negative")
			quit()
			
	def printcell(self):
		print(chr(self.currentvalue))
		
	def fillcellbyascii(self, newcharacter):
		if type(newcharacter) is str:
			if len(self.newcharacter) == 1:
				self.currentvalue = ord(newcharacter)
			else:
				print("internal error: more than one character passed to fillcellbyascii")
				quit()
		else:
			print("internal error: non string passed to fillcellbyascii")
			quit()
			
class bfengine():
	
	def __init__(self):
		self.tape = tape()
		if len(sys.argv) > 0:
			self.bffile = open(sys.argv[1], "r")
		else:
			print("Usage: python3 confused-serpent.py your-brainfuck-program.bf")
			quit()
		self.programbuffer = self.bffile.readlines()
		if type(self.programbuffer) is list:
			self.programbuffer = "".join(self.programbuffer)
		elif type(self.programbuffer) is not str:
			print("error: issues reading the bf file please ensure it is actually a brainfuck program")
		self.programbuffer = list(self.programbuffer)
		self.instructionpointer = 0
		self.instruction = self.programbuffer[self.instructionpointer]
		self.running = 1
		while self.running == 1:
			if self.instruction == "<":
				self.tape.decrementpointer()
			elif self.instruction == ">":
				self.tape.incrementpointer()
			elif self.instruction == "+":
				self.tape.incrementcell()
			elif self.instruction == "-":
				self.tape.decrementccell
			elif self.instruction == ".":
				self.tape.printcell()
			elif self.instruction == ",":
				self.tape.fillcellbyascii(self.programbuffer[self.instructionpointer + 1])
			elif self.instruction == "[":
				if self.tape.currentvalue == 0:
					if self.instrucctionpointer <= len(self.programbuffer) + 1:
						self.instructionpointer = self.instructionpointer + 1
						while self.instruction != "]":
							if self.instrucctionpointer <= len(self.programbuffer) + 1:
								self.instructionpointer = self.instructionpointer + 1
							else:
								print("syntax error: unmatched brackets")
								quit()
					else:
						print("syntax error: unmatched brackets")
						quit()
			elif self.instruction == "]":
				if self.tape.currentvalue != 0:
					if self.instructionpointer > 0:
						self.instructionpointer = self.instructionpointer - 1
					else:
						print("syntax error: unmatched brackets")
						quit()
					while self.instruction != "[":
						if self.instructionpointer > 0:
							self.instructionpointer = self.instructionpointer - 1
						else:
							print("syntax error: unmatched brackets")
							quit()
			if self.instructionpointer < len(self.programbuffer):
				self.instructionpointer = self.instructionpointer + 1
				print("one loop down")
			else:
				running = 0
		print("program completed with no errors")
	
confused_serpent = bfengine()
