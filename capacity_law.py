class CL:

    def __init__(self, current_C, diff_voltage):
        self.diff_voltage = diff_voltage
        self.current_C = current_C
        return

    def capacitance(self,current_C, diff_voltage):
        diff_voltage = float(input("\nenter the differentiated voltage value in volts"))
        current_C = float(input("enter the current value in amps"))

        c =   current_C / diff_voltage

        return c



