class OV:

    def __init__(self, current, resistance):
        self.current = current
        self.resistance = resistance
        return
    
    def ohmsVoltage(self, current, resistance):
        current= float(input("\nenter the currrent value"))
        resistance= float(input("enter the resistance value"))
        voltage = current * resistance
        return voltage

    
