G: float = 6.67 * 10 ** -11
EARTH_MASS: float = 5.98 * 10 ** 24
EARTH_RADIOUS: float = 6.37 * 10 ** 6
SUN_MASS: float = 1.98 * 10 ** 30
SUN_RADIOUS: float = 6.95 * 10 ** 8
AE: float = 1.49 * 10 ** 11

planet_mass: float = float(input("enter the planet mass (in Earth's masses) : ")) * EARTH_MASS
planet_radious: float = float(input("enter the planet radious (in Earth's radiuoses): ")) * EARTH_RADIOUS
distance_from_sun: float = float(input("enter the distance to the sun (in a.e.): ")) * AE

r = distance_from_sun + SUN_RADIOUS + planet_radious

f: float = (G * planet_mass * EARTH_MASS) / (r ** 2)
g: float = (G * planet_mass) / (planet_radious ** 2)

print(f)
print(g)