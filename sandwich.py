+import math
 +
 +name = "HOAGIE"
 +class Sandwich():
 +  name = "HOAGIE"
 +  def __init__(self, name, ingredients):
 +    self.name = name
 +    self.ingredients = ingredients
 +
 +  def getCost(self, markup = 0.33 ):
 +    total = 0
 +
 +    for ingredient in self.ingredients:
 +      total = total + ingredient.cost
 +
 +    total = total + total * markup
 +    return math.ceil(total)
 +
 +class CostedItem():
 +  def __init__(self, name, cost):
 +    self.name = name
 +    self.cost = cost
 +
 +meat = CostedItem("meat", 1.00)
 +roll = CostedItem("kaiser roll", 0.75)
 +hoagieRoll = CostedItem("amoroso roll", 1.00)
 +tuna = CostedItem("tuna", 1.50)
 +cheese = CostedItem("cheeze", 0.75)
 +lettuce = CostedItem("lettuce", 0.5)
 +tomato = CostedItem("tomato", 0.5)
 +mayo = CostedItem("mayo", 0.25)
 +order = [
 +  Sandwich("italian hoagie", [meat, meat, meat, cheese, mayo, lettuce, tomato, hoagieRoll]),
 +  Sandwich("cheese hoagie", [cheese, meat, tuna, mayo, lettuce, hoagieRoll]),
 +  Sandwich("tuna hoagie", [tuna, tomato, lettuce, mayo, cheese, hoagieRoll]),
 +  Sandwich("burger", [meat, meat, cheese, lettuce, tomato, mayo, roll]),
 +]
 +
 +sum = 0
 +for wich in order:
 +  print (wich.name + " " + str(wich.getCost()))
 +  sum = sum + wich.getCost()
 +
 +print ("TOTAL: " + str(sum))
