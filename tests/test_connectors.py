# tests/test_connectors.py
import unittest
from src.connectors import Connector
from src.logic_gates import ANDGate, ORGate

class TestConnectors(unittest.TestCase):
    def test_connector(self):
        # Create logic gates
        and_gate = ANDGate("AND1")
        or_gate = ORGate("OR1")
 
        # Set input values for AND gate
        and_gate.set_pin_a(True)
        and_gate.set_pin_b(True)

 # Connect the gates using connectors

        connector = Connector(and_gate, or_gate)
 
 
        # Get output from OR gate
        result = or_gate.get_output()

        # Assert the expected result
        self.assertEqual(result, 1, f"Expected 1, but got {result}")

if __name__ == "__main__":
    unittest.main()
