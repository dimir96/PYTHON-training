

# САМАЯ ДАЛЕКАЯ ПЛАНЕТА
def find_farthest_orbit(list_of_orbits):
    powerch = [(x[0] * x[1]) for x in list_of_orbits if x[0]!=x[1]]
    key = max(powerch)
    return [orbit for orbit in list_of_orbits if (orbit[0] * orbit[1]) == key]



orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))