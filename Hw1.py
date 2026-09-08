rice = 45
sugar = 40
oil = 130
rice_quantity = 3
sugar_quantity = 2.5
oil_quantity = 1.8
rice_total=rice*rice_quantity
print("RiceTotal:",rice_total)
sugar_total=sugar*sugar_quantity
print("SugarTotal",sugar_total)
oil_total=oil*oil_quantity
print("OilTotal",oil_total)
total_bill=rice+sugar+oil
print("Totalbill",total_bill)
total_int=int(total_bill)
print("The totalbill as interger",total_int)
total_string=str(total_int)
print("The string of the interger"+total_string)
import random
delivery_charge=random.randrange(5,10)
print("Deliverycharge:",delivery_charge)
final_bill=total_int+delivery_charge
print("Final",final_bill)

