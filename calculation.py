import pandas as pd
import numpy as np
import numpy_financial as npf

def equal_yearly_payment(interest, years, loan):
    annual_payment = npf.pmt(rate = interest, nper = years, pv = -loan)
    print(annual_payment)
    return annual_payment


def amortization_plan(interest, years, loan):
    car_payments = npf.pmt(rate = interest, nper = years, pv = -loan)
    loan_table = np.zeros((years,6))

    loan_table = pd.DataFrame(loan_table)
    print(loan_table)
    loan_table.columns = ["Year", "Initial_Balance", "Payments", "Interest",
                                    "Capital", "Outstanding_Amount"]
    loan_table.iloc[0,0] = 1
    loan_table.iloc[0,1] = loan
    loan_table.iloc[0,2] = car_payments
    loan_table.iloc[0,3] = loan * interest
    loan_table.iloc[0,4] = car_payments - (loan * interest)
    loan_table.iloc[0,5] = loan - (car_payments - (loan * interest))
    for i in range(1,5):
        loan_table.iloc[i,0] = i + 1
        loan_table.iloc[i,1] = loan_table.iloc[(i-1), 5]
        loan_table.iloc[i,2] = car_payments
        loan_table.iloc[i,3] = loan_table.iloc[i,1] * interest
        loan_table.iloc[i,4] = car_payments - (loan_table.iloc[i,1] * interest)
        loan_table.iloc[i,5] = loan_table.iloc[i,1] - (car_payments - (loan_table.iloc[i,1] * interest))
        
    loan_table = loan_table.round(2)
        
    with pd.option_context("display.max_rows",None,"display.max_columns", None):
        print(loan_table)
