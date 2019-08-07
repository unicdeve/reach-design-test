class BudgetCalculator:

    GROCERIES = 0.2  # 30%
    LAUNDARY = 0.05  # 5%
    SUBSCRIPTIONS = 0.05  # 5%
    MISCELLANEOUS = 0.1  # 10%
    HEALTHCARE = 0.05  # 5%
    HOUSEHOLD_REPAIR = 0.05  # 5%
    RENT = 0.1  # 30%
    CLOTHING = 0.1  # 30%
    TRANSPORT = 0.1  # 30%
    SAVINGS = 0.2  # 30%

    # def __init__(self, age, gender, dependents, monthly_income):
    #     self.age = age
    #     self.gender = gender
    #     self.dependents = dependents
    #     self.monthly_income = monthly_income

    def calculator(self, age, gender, dependents, monthly_income):
        self.age = age
        self.gender = gender
        self.dependents = dependents
        self.monthly_income = monthly_income

        if gender == 1:
            return (self.GROCERIES * monthly_income), (self.LAUNDARY * monthly_income), (self.MISCELLANEOUS * monthly_income), (self.SUBSCRIPTIONS * monthly_income), (self.HEALTHCARE * monthly_income), (self.HOUSEHOLD_REPAIR * monthly_income), (self.RENT * monthly_income), (self.CLOTHING * monthly_income), (self.TRANSPORT * monthly_income), (self.SAVINGS * monthly_income)

        elif(gender == 2):
            self.GROCERIES = 0.1
            self.SAVINGS = 0.3
            return (self.GROCERIES * monthly_income), (self.LAUNDARY * monthly_income), (self.MISCELLANEOUS * monthly_income), (self.SUBSCRIPTIONS * monthly_income), (self.HEALTHCARE * monthly_income), (self.HOUSEHOLD_REPAIR * monthly_income), (self.RENT * monthly_income), (self.CLOTHING * monthly_income), (self.TRANSPORT * monthly_income), (self.SAVINGS * monthly_income)

        else:
            return (self.GROCERIES * monthly_income), self.LAUNDARY, (self.MISCELLANEOUS * monthly_income), (self.SUBSCRIPTIONS * monthly_income), (self.HEALTHCARE * monthly_income), (self.HOUSEHOLD_REPAIR * monthly_income), (self.RENT * monthly_income), (self.CLOTHING * monthly_income), (self.TRANSPORT * monthly_income), (self.SAVINGS * monthly_income)
