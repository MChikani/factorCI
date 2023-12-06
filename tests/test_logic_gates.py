# tests/test_logic_gates.py
import unittest
from src.logic_gates import ANDGate, ORGate, XORGate, adder, eight_bit_adder

class TestLogicGates(unittest.TestCase):
    def test_and_gate(self):
        # Test case 1: Both inputs are True
        gate = ANDGate("and_gate")
        gate.set_pin_a(True)
        gate.set_pin_b(True)
        result = gate.perform_gate_logic()
        self.assertTrue(result)

        # Test case 2: One input is False
        gate.set_pin_a(False)
        gate.set_pin_b(True)
        result = gate.perform_gate_logic()
        self.assertFalse(result)

        # Add more test cases as needed

    def test_or_gate(self):
        # Test case 1: Both inputs are True
        gate = ORGate("or_gate")
        gate.set_pin_a(True)
        gate.set_pin_b(True)
        result = gate.perform_gate_logic()
        self.assertTrue(result)

        # Test case 2: One input is False
        gate.set_pin_a(False)
        gate.set_pin_b(True)
        result = gate.perform_gate_logic()
        self.assertTrue(result)

        # Add more test cases as needed

    def test_xor_gate(self):
        # Test case 1: One input is True and the other is False
        gate = XORGate("xor_gate")
        gate.set_pin_a(True)
        gate.set_pin_b(False)
        result = gate.perform_gate_logic()
        self.assertTrue(result)

        # Test case 2: Both inputs are True
        gate.set_pin_a(True)
        gate.set_pin_b(True)
        result = gate.perform_gate_logic()
        self.assertFalse(result)
 
    def test_one_bit_adder(self):
        for a in [0, 1]:
            for b in [0, 1]:
                c, s = adder(a, b, 0)
                expected_output = f"{a} + {b} = {c}{s}"
                self.assertEqual(expected_output, f"{a} + {b} = {c}{s}")

    def test_eight_bit_adder(self):
            input1 = "10101010"
            input2 = "01010101"
            output = eight_bit_adder(input1, input2)
            expected_output = f"Input: {input1} + {input2}, Output: {output}"
            self.assertEqual(expected_output, f"Input: {input1} + {input2}, Output: {output}")

            input1 = "00000001"
            input2 = "01111111"
            output = eight_bit_adder(input1, input2)
            expected_output = f"Input: {input1} + {input2}, Output: {output}"
            self.assertEqual(expected_output, f"Input: {input1} + {input2}, Output: {output}")


if __name__ == "__main__":
    unittest.main()
