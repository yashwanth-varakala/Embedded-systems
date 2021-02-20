class IC:

    def __init__(self, voltage_I, diff_current):
        self.diff_current = diff_current
        self.voltage_I = voltage_I
        return


    def inductance(self, voltage_I, diff_current):
        diff_current = float(input("\nenter the differentiated current value in amps"))
        voltage_I = float(input("enter the voltage value in volts"))
        ind = voltage_I / diff_current

        return ind


