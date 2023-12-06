 # -*- coding: utf-8 -*-
"""CMPSC132 - Homework 1.py

I have included that code snippets for the <a href= "https://runestone.academy/runestone/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html">PSADS book below</a>. You need to extend the code in order to meet the criteria listed at the end of the chapter.
"""
def gcd(m, n):
      while m % n != 0:
        m, n = n, m % n
      return n
  
def int_to_fraction(x):
  if type(x) == int:
    return Fraction(x, 1)
  elif type(x) == Fraction:
    return x
  else:
    raise TypeError("Must be an int/Fraction")

class Fraction:
    def __init__(self, top, bottom):
        cmmn = gcd(top, bottom)
        self.num = top // cmmn
        self.den = bottom // cmmn
        

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)


  
    def __sub__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.den \
        - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __mul__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    def __gt__(self, other_fraction):
      return (self.num * other_fraction.den > other_fraction.num * self.den)

    def __ge__(self, other_fraction):
      return (self.num * other_fraction.den >= other_fraction.num * self.den)

    def __lt__(self, other_fraction):
      return (self.num * other_fraction.den < other_fraction.num * self.den)

    def __le__(self, other_fraction):
      return (self.num * other_fraction.den <= other_fraction.num * self.den)

    def __ne__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num != second_num

    def __repr__(self):
      return self.__str__()

    def __radd__(self, left):
      """
      print(f"self: {self}")
      print(f"left: {left}")
      """
      return self + left
      #return None
      
    def __repr__(self):
      return self.__str__()

    def get_num(self):
      return self.num
    def get_den(self):
      return self.den
      
    def show(self):
        print(self.__str__())


class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


#class BinaryGate(LogicGate):

    def __init__(self,n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        # a = self.getPinA()
        # b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

#class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        #a = self.getPinA()
        #b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

#class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


#class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

#class XORGate(BinaryGate): 
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    def performGateLogic(self):
      #return self.pinA ^ self.pinB
      return(self.pinA and not self.pinB) or (not (self.pinA and self.pinB))  


#class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

def __init__(self, lbl):
        self.name = lbl
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class LogicGate:

    def __init__(self, lbl):
        self.name = lbl
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, lbl):
        super(BinaryGate, self).__init__(lbl)
        self.pin_a = None
        self.pin_b = None

    #Programmatically set value
    def set_a(self,a):
        self.pin_a = a
    def set_b(self,b):
        self.pin_b = b
    #Grab values from the user
    def set_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter pin A input for gate " + self.get_label() + ": "))
    def set_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter pin B input for gate " + self.get_label() + ": "))
    # Call to set both pins with user data
    def set_pins(self):
        self.pin_a = self.set_pin_a()
        self.pin_b = self.set_pin_b()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
    
    def get_pin_a(self):
        return self.pin_a
    
    def get_pin_b(self):
        return self.pin_b


class ANDGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        assert self.pin_a != () and self.pin_b != ()
        return((self.pin_a and self.pin_b))  

class ORGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class XORGate(BinaryGate): 
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)
    def perform_gate_logic(self):
        return((self.pin_a or self.pin_b) and not(self.pin_a and self.pin_b))  

class UnaryGate(LogicGate):

    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input("Enter pin input for gate " + self.get_label() + ": "))
        else:
            return self.pin
            

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NOTGate(UnaryGate):

    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class NANDGate(ANDGate):
    
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class NORGate(ORGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(fgate.get_output())

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


def adder(a,b,c=0):
  #define all gates
  xor1= XORGate("xor1")
  xor2= XORGate("xor2")
  and1= ANDGate("and1")
  and2= ANDGate("and2")
  or1= ORGate("or1")
  # set all input values
  xor1.pin_a = a
  xor1.pin_b = b  
  and2.pin_a = a
  and2.pin_b = b
  and1.pin_b = c
  xor2.pin_b = c
  #now set the connectors
  ca = Connector(xor1, xor2)
  cb = Connector(xor1, and1)
  
  cc = Connector(and1, or1)
  cd = Connector(and2, or1)
  
  #NATE: Make sure the outputs are correct to match the schematic
  # https://en.wikipedia.org/wiki/Adder_(electronics)
  return int(or1.perform_gate_logic()), int(xor2.perform_gate_logic())
 
