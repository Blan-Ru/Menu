#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()


def get_num(field):
value = form.getvalue(field, "0")
if value.isdigit():
return int(value)
return 0


bottom_bun = get_num("bottom_bun")
top_bun = get_num("top_bun")
beef_patty = get_num("beef_patty")
bacon = get_num("bacon")
fried_egg = get_num("fried_egg")
cheese = get_num("cheese")
lettuce = get_num("lettuce")
tomato = get_num("tomato")
onion = get_num("onion")
pickle = get_num("pickle")
ketchup = get_num("ketchup")
mayo = get_num("mayo")
mustard = get_num("mustard")


bottom_bun_cal = bottom_bun * 120
top_bun_cal = top_bun * 120
beef_patty_cal = beef_patty * 280
bacon_cal = bacon * 45
fried_egg_cal = fried_egg * 90
cheese_cal = cheese * 70
lettuce_cal = lettuce * 5
tomato_cal = tomato * 10
onion_cal = onion * 15
pickle_cal = pickle * 5
ketchup_cal = ketchup * 20
mayo_cal = mayo * 90
mustard_cal = mustard * 10


total = (bottom_bun_cal + top_bun_cal + beef_patty_cal +
bacon_cal + fried_egg_cal + cheese_cal +
lettuce_cal + tomato_cal + onion_cal +
pickle_cal + ketchup_cal + mayo_cal + mustard_cal)


print("Content-Type: text/html\r\n\r\n", end="")

print(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Your Burger Calories</title>
<link rel="stylesheet" href="../css/style.css">
</head>
<body>

<h1>Your Burger Results</h1>

<table>
<tr><td>Bottom Bun</td> <td>{bottom_bun} x 120 kcal = {bottom_bun_cal} kcal</td></tr>
<tr><td>Top Bun</td> <td>{top_bun} x 120 kcal = {top_bun_cal} kcal</td></tr>
<tr><td>Beef Patty</td> <td>{beef_patty} x 280 kcal = {beef_patty_cal} kcal</td></tr>
<tr><td>Bacon Strip</td> <td>{bacon} x 45 kcal = {bacon_cal} kcal</td></tr>
<tr><td>Fried Egg</td> <td>{fried_egg} x 90 kcal = {fried_egg_cal} kcal</td></tr>
<tr><td>Cheese Slice</td><td>{cheese} x 70 kcal = {cheese_cal} kcal</td></tr>
<tr><td>Lettuce Leaf</td><td>{lettuce} x 5 kcal = {lettuce_cal} kcal</td></tr>
<tr><td>Tomato Slice</td><td>{tomato} x 10 kcal = {tomato_cal} kcal</td></tr>
<tr><td>Onion Ring</td> <td>{onion} x 15 kcal = {onion_cal} kcal</td></tr>
<tr><td>Pickle Slice</td><td>{pickle} x 5 kcal = {pickle_cal} kcal</td></tr>
<tr><td>Ketchup</td> <td>{ketchup} x 20 kcal = {ketchup_cal} kcal</td></tr>
<tr><td>Mayonnaise</td> <td>{mayo} x 90 kcal = {mayo_cal} kcal</td></tr>
<tr><td>Mustard</td> <td>{mustard} x 10 kcal = {mustard_cal} kcal</td></tr>
</table>

<h2>Total: {total} kcal</h2>

<br>
<a href="../index.html">Go Back</a>

</body>
</html>
""")