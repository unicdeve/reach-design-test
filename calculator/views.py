from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .budget_calculator import BudgetCalculator


@csrf_exempt
def home(request):
    if request.method == "POST":
        income = request.POST.get('income')
        age = request.POST.get('age')
        marital_status = request.POST.get('marital_status')
        dependents = request.POST.get('dependents')
        gender = request.POST.get('gender')

        errors = {}
        print(type(income))
        if (income == ''):
            errors.update({"income": "please enter a valid income"})

        elif(int(income) < 30000):
           errors.update({"income": "enter income not less than 30000"})

        else:
           errors = {}

        if not dependents:
            errors.update({"dependents": "please enter number of dependents"})
        
        if (marital_status == "Pls select an option."):
            errors.update({"marital status": "please select a valid marital status"})

        if (gender == "Pls select an option."):
            errors.update({"gender": "please select your gender"})

        if not age:
            errors.update({"age": "please enter a valid age"})

        
        if (len(errors) > 0):
            return JsonResponse(errors, status=400)
            

        if not dependents:
            errors.update({"dependents": "please number of dependents"})
            return JsonResponse(errors, status=400)

        budget = BudgetCalculator()
        GROCERIES, LAUNDARY, MISCELLANEOUS, SUBSCRIPTIONS, HEALTHCARE, HOUSEHOLD_REPAIR, RENT, CLOTHING, TRANSPORT, SAVINGS = budget.calculator(age, gender, dependents, float(income))

        result = {
          "groceries": GROCERIES,
          "laundry": LAUNDARY,
          "miscellaneous": MISCELLANEOUS,
          "subscriptions": SUBSCRIPTIONS,
          "healthcare": HEALTHCARE,
          "household_repair": HOUSEHOLD_REPAIR,
          "rent": RENT,
          "clothing": CLOTHING,
          "transport": TRANSPORT,
          "saving": SAVINGS,
          "income": income
        }
        if request.is_ajax():
            return JsonResponse(result)
    return render(request, 'calculator/index.html')


def calculateBudget(request):
    return render(request, 'calculator/index.html')
