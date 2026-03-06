import sqlite3, pygame, math
from database import*
from classes import*

pygame.init()

win = pygame.display.set_mode((800, 600)) #display name

class Planets: #contains all planet method
	def __init__(self, num, value, database, enabled, move): #initialise variables
		self.num = num
		self.value = value
		self.database = database
		self.enabled = enabled
		self.move = move


		db = Connect(self.database) #connects to the databse
		
		#define each piece of data in table as variable
		sun_mass = db.getValues(1, 'Massx24') * 10e25
		self.name = db.getValues(self.num, 'Name')
		self.colour = '#' + db.getValues(self.num, 'Colour')
		self.mass = (db.getValues(self.num, 'Massx24')) * 10e24 #into Kg
		self.orbitalRadius = (db.getValues(self.num, 'OrbitalRadius')) *2e7  #into km
		self.orbitalVelocity = (db.getValues(self.num, 'OrbitalVelocity')) * 10e3 #into m/s
		self.diameter = (db.getValues(self.num, 'Diameter')) * 10e3 #into m
		self.gravity = db.getValues(self.num, 'Gravity') #in N/Kg
		self.angle = math.radians(db.getValues(self.num, 'OrbitalInclination')) #in radians
		

		self.scale = 10000000 #initial scale
		if self.value < 0: #if value is less than 0, increase the scale 
			self.value = self.value * -1 #magnitude
			for x in range(self.value):
				self.scale = self.scale * 1.1 #by 1%
		elif self.value > 0: #if value is more than 0, decrease the scale.
			for x in range(self.value):
				self.scale = self.scale * 0.9 #by 1%
		radius = (self.diameter / self.scale) /2  #works out radius to scale
		



	def draw(self, radius, position_x, position_y):#draws planet onscreen
		if self.enabled: #when the enabled is true
			circle = pygame.draw.circle(win, self.colour, (position_x, position_y), radius) #draws planet on screen
			text = Text(self.name, (10 + position_x), (10 + position_y) ,'white', fontA, True, False, 0, 'white') #draws planet label on screen



	def createAngle(self, position_y, position_x, centre_y, centre_x): 
		#the angle needs to be based on distance from sun to planet, not whole screen so sub centre.
		position_x = position_x - centre_x 
		position_y = position_y - centre_y
		angle = math.atan2(position_y, position_x) #calc current angle.

		return angle


	def velocityincrease(self):

		velocity_x = self.orbitalVelocity * math.cos(self.angle) #calculates x velocity
		velocity_y = self.orbitalVelocity * math.sin(self.angle) #calculates y velocity
		angle = math.atan2(velocity_y, velocity_x)  #calcs angle that should be added on, based on the size of velocity
		#using angle ensure circular motion
		return angle

	
	def position(self, position_x, position_y):

		centre_x = 400 #define middle of screen
		centre_y = 300
		angle = self.createAngle(position_y, position_x, centre_y, centre_x) #find the current angle based on pos
		angle = angle + self.velocityincrease() #increase angle
		position_x = centre_x + (self.orbitalRadius / self.scale) * math.cos(angle) #calc new position, with new angle
		position_y = centre_y + (self.orbitalRadius / self.scale) * math.sin(angle)
		return position_x, position_y 


	
	def check_click(self, position_x, position_y):
		mouse_pos = pygame.mouse.get_pos() #get mouse position
		left_click = pygame.mouse.get_pressed()[0]  #ensure check left not all
		diameter = self.diameter /self.scale #define diameter of rectangle
		planet_pos = pygame.rect.Rect(position_x - (diameter/2), position_y - (diameter /2), diameter, diameter) #rect where planet is
		
		if left_click and planet_pos.collidepoint(mouse_pos) and self.enabled: #checks if planet rectangle is clicked
			return True #was clicked
		else:
			return False #wasn't clicked

