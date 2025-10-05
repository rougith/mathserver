# Ex.05 Design a Website for Server Side Processing
# Date:5/10/25
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
'''
math.html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Incandescent Bulb Power Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: beige;
    }

    .container {
      background-color: yellow;
      padding: 40px 50px;
      border-radius: 15px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
      text-align: center;
      width: 380px;
    }

    h2 {
      margin-bottom: 20px;
      color: #222;
    }

    label {
      display: block;
      text-align: left;
      margin-top: 15px;
      font-weight: bold;
      color: #333;
    }

    input {
      width: 100%;
      padding: 8px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 6px;
    }

    button {
      margin-top: 20px;
      padding: 10px 16px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      width: 100%;
      font-size: 16px;
    }

    button:hover {
      background-color: #0056b3;
    }

    .result-box {
      margin-top: 25px;
      background-color: #e9f5ff;
      border: 2px solid #007bff;
      border-radius: 8px;
      padding: 15px;
      color: #222;
      font-weight: bold;
      font-size: 1.2em;
    }
  </style>
</head>

<body>
  <div class="container">
    <h2>Incandescent Bulb Power Calculator</h2>
    <form method="post">
      {% csrf_token %}
      <label>Current (A):</label>
      <input type="text" name="current" required>

      <label>Resistance (Ω):</label>
      <input type="text" name="resistance" required>

      <button type="submit">Calculate Power</button>
    </form>

    {% if power %}
    <div class="result-box">Your Power: {{ power }} W</div>
    {% endif %}
  </div>
</body>

</html>

views.py 
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

    urls.py
    from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculate_power, name='calculate_power'),
]

'''
# SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-10-05 230436.png>)


# HOMEPAGE:

![alt text](<Screenshot 2025-10-05 230552.png>)


# RESULT:
The program for performing server side processing is completed successfully.
