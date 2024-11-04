outcomes = "W W L T T W"
points_map = {"W": 2, "T": 1, "L": 0}
points = [points_map[outcome] for outcome in outcomes.split()]
print(points)
