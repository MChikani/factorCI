class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        # Connect the output of the fromgate to the input of the togate
        tgate.set_pin_a(fgate)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate
