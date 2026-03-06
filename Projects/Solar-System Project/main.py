import pygame, random, tkinter
from tkinter.filedialog import askopenfilename
from database import* 
from classes import*
from planets import*

pygame.init()

win = pygame.display.set_mode((800, 600)) #display
pygame.display.set_caption('Planet Simulator') #title
timer = pygame.time.Clock()
db = 'Planets.db' #default database
centre_x = 400 #defining the centre of the screen
centre_y = 300
x_coord = [0, 0, 0, 0, 0, 0, 0, 0, 0]#arrays for the x and y coord of planets
y_coord = [0, 0, 0, 0, 0, 0, 0, 0, 0]

run = True #condition to run the program
stars = True #displays stars on scree
welcome = True #displays welcome screen until start is clicked
start = False #displays load and new page
planet = False #displays planets, and solar system
value = 0 #changes the scale, larger value means larger scale
playbtntext = 'Play' #original text of play solar system
move = False #whether planets are paused or moving
scale =False #display toscale button
toscale = False 
play = False #declare outside while loop, so it isnt reset every iteration
days = 0 #counts how many years have passed (earth years)


#pop up boolean dependent on the planet
suntext = False 
merctext = False
info_screen = False




stars_arr = []
for i in range(200):
	stars_arr.append(Star('white', True)) #adds stars to an array


while run:
	timer.tick(60)	

	if planet:
		stars = True #redraws stars after each iteration

	if stars:
		win.fill('black') #paints screen black
		for x in stars_arr:
			x.draw() #draws stars
			if i == 199:
				stars = False#stops drawing at end of array

	startbtn = Button('Start', 350, 275, welcome, 100, 50, '#ad42f5', '#5f059c') #draws start button on screen
	title = Text('Planet Simulator', 400, 100, 'purple', pygame.font.SysFont('freestylescript', 100), welcome, False, [0, 0], 'white') #draws title on screen
	if startbtn.check_click():
		welcome = False #stops start screen being on screen
		stars = True #redraws stars
		start = True #enables next screen objects

	newbtn = Button('New', 50, 200, start, 300, 150, '#ad42f5', '#5f059c') #select new solar system
	ldabtn = Button('Load', 450, 200, start, 300, 150, '#ad42f5', '#5f059c') #select previous save 
	starttext = Text('Select "New" for a new solar system or select "Load" to import a previous save', 400, 75, 'white', fontA, start, True, [700, 25], 'purple') #prompt text


	if newbtn.check_click():
		open_def = Connect(db) #connects to default
		open_def.connect()
		start = False #loads a blank screen - will have planets on in future
		stars = True #redraws stars
		planet = True

	if ldabtn.check_click():
		filename = tkinter.filedialog.askopenfilename()
		con = File(filename)

		if con.validate() == True: #move onto the next screen
			start = False
			planet = True
			stars = True
			db = filename

		else:
			tryagain = Text('Please select a valid database file', 400, 100, 'white', fontA, start, True, [300, 25], 'purple')


	zoomin = Button('+', 350, 540, planet, 50, 50, 'white', 'grey')
	zoomout = Button('-', 400, 540, planet, 50, 50, 'white', 'grey')

	playbtn = Button(playbtntext , 10, 10, planet, 60, 50, 'white', 'grey')
	toscalebtn = Button('To Scale', 690, 10, scale, 100, 50, 'white', 'grey')

	if playbtn.check_click(): #changes from play to pause when clicked
		if playbtntext == 'Play': 
			playbtntext = 'Pause'
			move = True

		elif playbtntext == 'Pause': #pause to play
			playbtntext = 'Play'
			move = False


	if zoomin.check_click(): #zooms in by changing the scale
		value = value + 1
		win.fill('black')
		stars = True #redraws stars
	
	if zoomout.check_click(): #zooms out by changing the scale
		value = value - 1
		win.fill('black')
		stars = True #redraws stars
		if value < -15:
			scale = True #enables toscale button
		else:
			scale = False #doesnt display toscale
	
	if days < 365: #changes to years after 1 full earth orbit
		dayscounter = Text(('Days: ' + str(days)), 50, 580, 'white', fontA, planet, True, [100, 25], 'purple') #displays days
	else:
		years = days // 365 #finds div
		yearcounter = Text(('Years: ' + str(years)), 50, 580, 'white', fontA, planet, True, [100, 25], 'purple') #displays years + div


	#define and draw planets using Planets method
	sun = Planets(1, value, db, planet, False) #defines sun as a planet.
	mercury = Planets(2, value, db, planet, move)
	venus = Planets(3, value, db, planet, move)
	earth = Planets(4, value, db, planet, move)
	mars = Planets(5, value, db, planet, move)
	jupiter = Planets(6, value, db, planet, move)
	saturn = Planets(7, value, db, planet, move)
	uranus = Planets(8, value, db, planet, move)
	neptune = Planets(9, value, db, planet, move)

	
	planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune] #planets in an array

	for p in planets:
		radius = (p.diameter /2) / p.scale
		if playbtntext == 'Play': #if play, puts planets in one position
			angle = p.angle #access angle
			position_x = centre_x + (p.orbitalRadius / p.scale) * math.cos(angle) #position in x position
			position_y = centre_y + (p.orbitalRadius / p.scale) * math.sin(angle) #position in the y position
			days = 0


		if p == sun and toscalebtn.check_click() and value < -15: #sun at an accurate size to jupiter when far away enough
			scales = True
		else:
			scales = False

		if scales: #changes radius to actual value when zoomed out enough
			radius = radius * 10

		if playbtntext == 'Pause': #if pause, moves planets

			position_x, position_y = p.position(x_coord[p.num-1], y_coord[p.num-1]) #works out new position
		

		p.draw(radius, position_x, position_y) #draws the planets on the screen

		#saves current position in array at planet id.
		x_coord[p.num - 1] = position_x 
		y_coord[p.num - 1] = position_y

	#adds to day counter when planets are moving
	if playbtntext == 'Pause':
		days = days + 1

	#checks if sun or planets have been clicked. 
	if sun.check_click(x_coord[0], y_coord[0]):
		suntext = True

	if mercury.check_click(x_coord[1], y_coord[1]):
		merctext = True
	
	#pop up text information
	#sun info, key characterics and fun facts. 
	sun_text = Text('Sun', 200, 40, 'white', fontB, suntext, True, (400, 1200), '#7D8CC4') 
	Text('Mass: 1.99 x10^30 Kg', 200, 80, 'white', fontA, suntext, False, (0,0), 'white')
	Text('Volume: 1,412,000 x10^12 Km', 200, 100, 'white', fontA, suntext, False, (0,0), 'white')
	Text('Diameter: 1,391, 400 Km ', 200, 120, 'white', fontA, suntext, False, (0,0), 'white')
	Text('Gravity: 247 N/Kg', 200, 140, 'white', fontA, suntext, False, (0,0), 'white')
	Text('- The part of the sun that we see from earth', 200, 280, 'white', fontA, suntext, False, (0,0), 'white')
	Text("is called a photosphere", 200, 300, 'white', fontA, suntext, False, (0,0), 'white')
	Text("- The temperature of the Sun's core is about", 200, 320, 'white', fontA, suntext, False, (0,0), 'white')
	Text("15 million degrees C", 200, 340, 'white', fontA, suntext, False, (0,0), 'white') 


	#mercury info, key characterstics and fun facts
	merc_text = Text('Mercury', 200, 40, 'white', fontB, merctext, True, (400, 1200), '#7D8CC4')
	Text('Mass: 0.33 x 10^24 Kg', 200, 80, 'white', fontA, merctext, False, (0,0), 'white')
	Text('Orbital Velocity: 47.9 Km/s ', 200, 100, 'white', fontA, merctext, False, (0,0), 'white')
	Text('Diameter: 4879 Km', 200, 120, 'white', fontA, merctext, False, (0,0), 'white')
	Text('Distace From Sun: 57.9 x10^6 Km', 200, 140, 'white', fontA, merctext, False, (0,0), 'white')
	Text('Orbital Peroid (in earth days): 88 days ', 200, 160, 'white', fontA, merctext, False, (0,0), 'white')
	Text('Gravity: 3.7 N/Kg ', 200, 180, 'white', fontA, merctext, False, (0,0), 'white')
	Text('- A day (24hrs) on Mercury is about 176', 200, 280, 'white', fontA, merctext, False, (0,0), 'white')
	Text('Earth days', 200, 300, 'white', fontA, merctext, False, (0,0), 'white')
	Text('-A day on Mercury is twice as long as its year', 200, 330, 'white', fontA, merctext, False, (0,0), 'white')
	Text('This is because it orbits the sun quicker than', 200, 350, 'white', fontA, merctext, False, (0,0), 'white')
	Text('it rotates on its axis', 200, 370, 'white', fontA, merctext, False, (0,0), 'white')

	if suntext or merctext: #if one of the options are true
		info_screen = True #sets this to true, things that need to be displayed on all info texts
	else:
		info_screen = False
	
	#displayed on all info screens 
	exit = Button('X', 375, 0, info_screen, 25, 25, 'purple', '#7D8CC4')
	question_text = Text('Did you know?', 200, 230, 'white', fontB, info_screen, False, (0,0), 'white')
	change_Mass = Text('Use the slider below to change the Mass', 200, 450, 'white', fontA, info_screen, False, (0,0), 'white')
	
	#draw slider
	slider = Slider(info_screen, 'white', 'black', 200, 500)

	if exit.check_click(): #when x in top corner is clicked, stops drawing them on screen.
		suntext = False
		merctext = False

	#checks if program is exited
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.display.flip()


pygame.quit()

