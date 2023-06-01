# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, template= 'Hello, <name>!'):
    return template.replace('<name>', name)
greet('Doc')
print(greet)
greet('Bob', 'Hello, <name>!')
print (greet)   

# ##2.Force
def force(mass: float, body: str = 'earth') -> float:
    planet_gravity = {
        
        'mercury': 3.7,
        'venus': 8.9,
        'earth': 9.8,
        'moon': 1.6,
        'mars': 3.7,
        'jupiter': 23.1,
        'saturn': 9.0,
        'uranus': 8.7,
        'neptune': 11.0,
        'pluto': 0.7
    }
    gravity = planet_gravity[body]
    return mass * gravity
earth_force = force(10.0)
print(f"The force exerted by Earth is {earth_force} N." )

# earth_force =force(mass=0.1)    # while calling function body= earth's gravity  is by default  
# print(f"The force exerted by Earth is {earth_force} N")   #  The force = m x g = 5.97 x 9.8 =  58.506 N 
# why wincpy shows keyError : 'sun'
# # #    

# 3.
def pull(m1, m2, d):
    G = 6.674 * (10 ** -11)
    return G * ((m1 * m2) / (d ** 2))
# Calculate the gravitational pull between Earth and the Moon
earth_mass = 5.97 * (10 ** 24 ) # kg    # The Earth has a mass of 5.972×10 power24 kg: m1
moon_mass = 7.34 * (10 ** 22 ) # kg    # Moon has a mass of 7.342×10 power22 kg) : m2
distance = 384400000  # m distance in meters
pull_force = pull(earth_mass, moon_mass, distance)
print(pull_force)  # = 1.985428700763691e+20 


# example from website to test: But a much larger object such as the Moon (with a mass of 7.342×10power22 kg) does have a noticeable effect on the Earth.

# The Moon orbits the Earth at about 384,000 km every 27.3 days

# And the Earth also has an "orbit" (more like a wobble) with the Moon of about 5000 km (which is actually less than the Earth's radius), also every 27.3 days.

# Your turn: try to work out the force of attraction == pull_force, between the Earth and the Moon.