fruits=['Apple','Orange','Grapes']
vegetables=['Carrot','Tomato','potato']
beverages=['Water','Pineapplejuice','Grapejuice']
fruits.append("Mango")
print(fruits)
vegetables.insert(1,"Ginger")
print(vegetables)
del beverages[2]
print(beverages)
inventory=[fruits,vegetables,beverages]
print(inventory)
print(fruits[:2])
print(vegetables[-1])
fruit=[len(x) for x in fruits]
print(fruit)
print('Water' in beverages)
first_item=(fruits[0],vegetables[0],beverages[0])
print(first_item)

