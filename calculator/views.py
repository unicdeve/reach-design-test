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
        print(type(income))
        budget = BudgetCalculator()
        GROCERIES, LAUNDARY, MISCELLANEOUS, SUBSCRIPTIONS, HEALTHCARE, HOUSEHOLD_REPAIR, RENT, CLOTHING, TRANSPORT, SAVINGS = budget.calculator(17, 2, 4, float(income))

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
