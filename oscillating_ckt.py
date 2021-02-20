
class OCL:

    def __init__(self, inductance_F, capacity_F):
        self.inductance = inductance_F
        self.capacity = capacity_F
        return

    def frequency(self,inductance_F, capacity_F):
        inductance_F = float(input("\nenter the inductance value in henry"))
        capacity_F = float(input("enter the capacity value in farads"))

        Osc_freq = 1/ (2 * 3.14 * ((inductance_F * capacity_F)**1/2))

        return Osc_freq


