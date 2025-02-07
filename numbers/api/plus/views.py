from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from .values import isPrime, isPerfect, digit_sum, check_number_properties

@api_view(['GET'])
def classify_number(request):
    # Validate that 'number' exists in query params
    number_param = request.query_params.get('number', None)
    if number_param is None or number_param == '':
        return JsonResponse({"error": "true", "number": ""}, status=400)

    # Check if the number is a valid integer (positive or negative)
    try:
        number = int(number_param)
    except ValueError:
        return JsonResponse({"error": "true", "number": number_param}, status=400)
    
    # Call your number functions
    is_prime = isPrime(number)
    is_perfect = isPerfect(number)
    properties = check_number_properties(number)
    digit_sum_ = digit_sum(number)

    # Fetch fun fact about the number
    fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math")  # Fun fact about the number
    fun_fact = fun_fact_response.text
    
    response = {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum_,
        "fun_fact": fun_fact
    }
    
    return JsonResponse(response, status=200)