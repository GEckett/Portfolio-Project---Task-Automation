
class Rates:
    def income_tax_rate(self, income):
        if 12571 < income < 50270:
            return 0.2
        elif 50270 < income < 150000:
            return 0.4
        elif 150000 < income:
            return 0.45
        else:
            return 0

    def cap_gains_tax_rate(self, cap_gains):
        if cap_gains < 6000:
            return 0
        else:
            return 0.2



