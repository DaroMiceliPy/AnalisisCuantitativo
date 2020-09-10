#We going to calculate de future value of one cash flow
import numpy as np

np.fv(0.1, 2, 0,-100) #We must to put the present value as negative number
#For numpy can solve de future value
input()

#If we put..
np.pv(0.1, 2, 0, -121)
#Its correspond to present value of two payment in two years

#For perpetuity, we have
5000/0.025 #Where the 5000 is the payment y 0.025 is the interest rate

#Another form to calculate those is...
import numpy.lib.financial as fin
fin.pv(0.1, 2, 0, -121)
#If the first payment is today
fin.pv(0.1, 2, 0, -121, when="begin")

'''We going to see the net present value
We assume that we have an investment with $200 value and we has estimated the next
incomes for the next five years are:
$80, $90, $40, $70, $50, with an interest rate of 2% '''
-200 + 80/(1 + 0.02) + 90/(1 + 0.02)**2 + 40/(1+ 0.02)**3 + 70/(1 + 0.02)**4 + 50/(1 + 0.02)**5

#Using numpy..
cashflow = [-200, 80, 90, 40, 70, 50]
np.npv(0.02, cashflow)
input()

import matplotlib.pyplot as plp

rates = np.linspace(0.01, 0.5, num=100) 
npv = []
for i in rates:
    npv.append(np.npv(i, cashflow))
x = (0, 0.7)
y = (0, 0)
plp.plot(rates, npv, color="green")
plp.title("Net Present Value for each interest rate")
plp.plot(x, y)
plp.show()


#The Internal rate of return is
np.irr(cashflow) #We can see the same interest rates that makes the cashflow net present value equal to zero
input()
