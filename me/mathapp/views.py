from django.shortcuts import render

def calculate_power(request):
    power = None 
    if request.method == "POST":
        try:
            current = float(request.POST.get("current"))
            resistance = float(request.POST.get("resistance"))
            power = (current ** 2) * resistance
            print(f"current: {current} A, resistance: {resistance} ohm, power: {power:.2f} W")
        except (ValueError, TypeError):
            power = "Invalid input! Please enter numbers only."

    return render(request, 'mathapp/math.html', {'power': power})

