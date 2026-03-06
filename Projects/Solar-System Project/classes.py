import random, pygame
pygame.init()


win = pygame.display.set_mode((800, 600)) #define display

#define fonts used in text and buttons
fontA = pygame.font.SysFont('Arial', 20)
fontbtn = pygame.font.SysFont('Arial', 20)
fontB = pygame.font.SysFont('freestylescript', 80)



class Button:
	def __init__(self, text, x_pos, y_pos, enabled, width, height, colour, clickcolour):   #need for all classes, initialises
		self.text = text  #allows u tp reference in another function in this class
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.enabled = enabled
		self.width = width
		self.height = height
		self.colour = colour
		self.clickcolour = clickcolour
		self.draw() #button is drawn on screen

	def draw(self): #if init has self, all functions should have self parameter
		button_text = fontbtn.render(self.text, True, 'black')
		button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
		text_rect = button_text.get_rect(center=(self.x_pos + (self.width / 2), self.y_pos + (self.height /2)))
		
		if self.enabled == True: #only draws when enabled is true, so button isn't permanently on screen
			if self.check_click() == True: #changes button colour to clickcolour when pressed on
				pygame.draw.rect(win, self.clickcolour,button_rect, 0, 5)
			else:
				pygame.draw.rect(win, self.colour,button_rect, 0, 5)
		
			pygame.draw.rect(win, 'black', button_rect, 2, 5) #border of button
			win.blit(button_text, text_rect) #draws text

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		left_click = pygame.mouse.get_pressed()[0]  #ensure check left not all
		button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
		if left_click and button_rect.collidepoint(mouse_pos) and self.enabled: #checks if button is clicked
			return True
		else:
			return False


class Text: #for writing on the screen
	def __init__(self, text, x_pos, y_pos, colour, font, enabled, background, bg_size, bg_colour): #initialise values
		self.text = text
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.colour = colour
		self.font = font
		self.enabled = enabled
		self.background = background
		self.bg_size = bg_size #size of background
		self.bg_colour = bg_colour
		self.draw()

	def draw(self): #draws text on screen
		text = self.font.render(self.text, True, self.colour) #renders the font
		text_rect = text.get_rect(center=(self.x_pos, self.y_pos)) #finds the position of the text and makes it center
		if self.enabled:
			if self.background == True: #to add a backround to make it easier to read
				background = pygame.rect.Rect(((self.x_pos - (self.bg_size[0]/2)), (self.y_pos - (self.bg_size[1]/2))), (self.bg_size[0], self.bg_size[1])) #moves the background into the centre.
				pygame.draw.rect(win, 'black', background, 2, 5)
				pygame.draw.rect(win, self.bg_colour, background, 0, 5)
			win.blit(text, text_rect) #draws the text on the screen. 


class Star:
	def __init__(self, colour, enabled):
		self.colour = colour
		self.enabled = enabled
		self.radius = random.randint(0, 5)
		
# can split stars into sections, two triangles ontop of each other, and work out coordinates of each point
		self.y_pos = random.randint(0, 600) #top point of star
		self.y_pos2 = self.y_pos + (self.radius /3) #split into 4 sections, top point, second layer
		self.y_pos3 = self.y_pos + (2 * self.radius / 3) #3rd layer and final point at bottom
		self.y_pos4 = self.y_pos + ( 5* self.radius/ 6)
		self.x_pos = random.randint(0, 800) #left side
		self.x_pos2 = self.x_pos + (self.radius /2) #middle, so top and bottom point x coordinate
		self.x_pos3 = self.x_pos + self.radius #right side.
		
		self.draw()

	def draw(self):
		#draw two triangles that over lap using previously defined coordinates. 
		pygame.draw.polygon(win, self.colour, ((self.x_pos2, self.y_pos), (self.x_pos, self.y_pos3), (self.x_pos3, self.y_pos3)))
		pygame.draw.polygon(win, self.colour, ((self.x_pos, self.y_pos2), (self.x_pos2, self.y_pos4), (self.x_pos3, self.y_pos2)))


class Slider:
	def __init__ (self, enabled, colour, colour_s, x, y):
		self.enabled = enabled
		self.colour = colour
		self.colour_s = colour_s
		self.x = x
		self.y = y
		self.draw()
	
	def draw(self):
		
		slider_rect = pygame.rect.Rect((self.x - 50, self.y), (100, 5))
		slider = pygame.rect.Rect((self.x, self.y - 7.5), (10, 20))
		if self.enabled:
			if self.check_click(slider):
				x_pos = pygame.mouse.get_pos()[0]
				slider = pygame.rect.Rect((x_pos, self.y - 7.5), (10, 20))

			pygame.draw.rect(win, self.colour, slider_rect, 0, 5)
			pygame.draw.rect(win, self.colour_s, slider, 0, 1)


	def check_click(self, slider):
		mouse_pos = pygame.mouse.get_pos()
		left_click = pygame.mouse.get_pressed()[0]  #ensure check left not all
		if left_click and slider.collidepoint(mouse_pos) and self.enabled: #checks if button is clicked
			return True
		else:
			return False