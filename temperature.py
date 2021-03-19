tempincelsius = input("Please enter a temperature in celsius...")
tempinfahrenheit = float(tempincelsius) * 1.8 + 32
roundedF = round(tempinfahrenheit, 2)
print(tempincelsius + " degrees celsius is " + str(roundedF) + "degrees fahrenheit.")
