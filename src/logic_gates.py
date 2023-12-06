# src/logic_gates.py

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

    def get_pin_a(self):
        return self.pin_a 

    def get_pin_b(self):
        return self.pin_b 

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        elif self.pin_b is None:
            self.pin_b = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

        

class ANDGate(BinaryGate):
    def __init__(self, lbl):
        super(ANDGate, self).__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return a & b

    def set_pin_a(self, value):
        self.pin_a = bool(value)

    def set_pin_b(self, value):
        self.pin_b = bool(value)

class ORGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == True or b == True:
            return 1
        else:
            return 0

    def set_pin_a(self, value):
        self.pin_a = bool(value)

    def set_pin_b(self, value):
        self.pin_b = bool(value)

class UnaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.get_label() + "-->"))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate):
    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1

class XORGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return (a and not b) or (not (a and b))

    def set_pin_a(self, value):
        self.pin_a = bool(value)

    def set_pin_b(self, value):
        self.pin_b = bool(value)

def adder(a, b, c):
    # XOR gate for sum
    xor_gate = XORGate("xor_sum")
    xor_gate.set_pin_a(a)
    xor_gate.set_pin_b(b)
    sum_bit = xor_gate.perform_gate_logic()

    # AND gate for carry
    and_gate = ANDGate("and_carry")
    and_gate.set_pin_a(a)
    and_gate.set_pin_b(b)
    carry_bit = and_gate.perform_gate_logic()

    # OR gate for final carry-out
    or_gate = ORGate("or_carry_out")
    or_gate.set_pin_a(carry_bit)
    or_gate.set_pin_b(c)
    carry_out = or_gate.perform_gate_logic()

    return carry_out, sum_bit


def eight_bit_adder(input1, input2):
    if len(input1) != 8 or len(input2) != 8:
        raise ValueError("Input strings must be of length 8")

    result = ""
    carry = 0

    for i in range(7, -1, -1):
        bit_a = int(input1[i])
        bit_b = int(input2[i])

        carry, sum_bit = adder(bit_a, bit_b, carry)

        # Prepend the sum bit to the result string
        result = str(sum_bit) + result

    # Append the final carry-out bit
    result = str(carry) + result

    return result
