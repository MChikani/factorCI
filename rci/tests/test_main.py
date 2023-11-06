import sys
sys.path.append("./rci/")

from main import Fraction, ANDGate, ORGate, XORGate, NOTGate

def test_fraction_addition():
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(2, 3)
    result = fraction1 + fraction2
    assert result == Fraction(7, 6)

def test_fraction_subtraction():
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(2, 3)
    result = fraction1 - fraction2
    assert result == Fraction(-1, 6)

def test_and_gate():
    gate = ANDGate("AND")
    gate.set_pins(1, 1)
    result = gate.perform_gate_logic()
    assert result == 1

def test_or_gate():
    gate = ORGate("OR")
    gate.set_pins(0, 1)
    result = gate.perform_gate_logic()
    assert result == 1
