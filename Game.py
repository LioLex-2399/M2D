import pygame,random
pygame.init()
clock = pygame.time.Clock()
blue = 0,0,255
green = 0,255,0
red= 255,0,0
greendull = 0,90,0
reddull = 90,0,0
bluedull = 0,155,0
black = 0,0,0
white = 255,255,255
gray = 155,155,155

Font50 = pygame.font.Font('amatic-sc.bold.ttf', 50)
Font40 = pygame.font.Font('amatic-sc.bold.ttf', 40)
Font30 = pygame.font.Font('amatic-sc.bold.ttf', 30)
Font25 = pygame.font.Font('amatic-sc.bold.ttf', 25)
Font23 = pygame.font.Font('amatic-sc.bold.ttf', 23)


display_height=550
display_width=800
gameDisplay = pygame.display.set_mode((display_width, display_height))
def lvl1(p1skin,p2skin,att1,att2):
	#Initializing variables
	#Hover checkers(Variables)
	arrowlhov = False
	arrowrhov = False
	arrowuhov = False
	arrowdhov = False

	P2LeftTriggered = False
	P2RightTriggered = False
	p2AbilityTriggered = False

	keyahov = False
	keydhov = False
	keywhov = False
	keyshov = False

	P1RightTriggered = False
	p1AbilityTriggered = False
	
	x1=350
	y1=480
	x3=0
	y3=0
	p1bullet=False
	plyrhlth=100
	plyrdamage=10
	p1AbilityTriggered=False

	p2_x=350
	p2_y=10
	p2_Attack_x=0
	p2_Attack_y=0
	p2bullet=False
	p2hlth=100
	p2Damage=10
	p2AbilityTriggered=False

	# player images
	playerscale = 3.5
	ScaleImg = pygame.image.load("M2D/Types/Normal.png").convert_alpha()
	new_w = ScaleImg.get_width() *playerscale
	new_h = ScaleImg.get_height() *playerscale
	NormalP1 = pygame.transform.scale(pygame.image.load("M2D/Types/Normal.png").convert_alpha(), (new_w, new_h))
	AttackP1 = pygame.transform.scale(pygame.image.load("M2D/Types/Attacker.png").convert_alpha(), (new_w, new_h))
	DefenseP1 = pygame.transform.scale(pygame.image.load("M2D/Types/Defence.png").convert_alpha(), (new_w, new_h))
	Player1 = NormalP1
	Player2 = pygame.transform.rotate(Player1, 180)

	GameEnded = False
	GamePaused = False
	PauseReason = 0
	# PauseReason 1 = NumLock is off
	notPaused = not GamePaused or PauseReason == 0
	while notPaused and not GameEnded:
			Mouse_x, Mouse_y = pygame.mouse.get_pos()
			background_colour=0,200,55
			gameDisplay.fill(background_colour)
			#Player1
			text_surface = Font30.render('health: '+str(plyrhlth)+"%", True, (0, 0, 0))
			
			gameDisplay.blit(text_surface, (4,490))		
			pygame.draw.line(gameDisplay, (6,6,6), (0, 480), (800, 480),(4))
			gameDisplay.blit(Player1, (x1, y1))
	#		print()


			#Player2
			pygame.draw.line(gameDisplay, (6,6,6), (0, 50), (800, 50),(4))		

			gameDisplay.blit(Player2, (p2_x, p2_y))
			
			text_surface = Font30.render('health: '+str(p2hlth)+"%", True, (0, 0, 0))
			
			gameDisplay.blit(text_surface, (4,4))
			

			if plyrhlth <= 0 or p2hlth<=0:
				print("game over")
				break

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					GameEnded = True
				
				
				mods = pygame.key.get_mods()
				if not (mods & pygame.KMOD_NUM):
					GamePaused = True
					PauseReason = 1
					while GamePaused:
							for event in pygame.event.get():
								if pygame.key.get_mods() & pygame.KMOD_NUM:
									if PauseReason == 1:
										print ("numlock on")
										PauseReason = 0
										GamePaused = False
			
								if event.type == pygame.QUIT:
									pygame.quit()
									quit()
							pygame.draw.rect(gameDisplay,gray,pygame.Rect(display_width/2-150,display_height/2-100,300,200))
							pygame.draw.rect(gameDisplay,black,pygame.Rect(display_width/2-150,display_height/2-100,300,200),5)
							#Draw text
							#Thicker lettering for the title
							text_surface = Font50.render('Game Paused', True, (0, 0, 0))
							gameDisplay.blit(text_surface, (display_width/2-80,display_height/2-80))
							text_surface = Font50.render('Game Paused', True, (0, 0, 0))
							gameDisplay.blit(text_surface, (display_width/2-79,display_height/2-80))
			
							text_surface = Font30.render('Numlock is required for this game', True, (0, 0, 0))
							gameDisplay.blit(text_surface, (display_width/2-140,display_height/2+10))
							text_surface = Font30.render('Please turn on NumLock', True, (0, 0, 0))
							gameDisplay.blit(text_surface, (display_width/2-140,display_height/2+50))
			
							pygame.display.update()
	
				elif event.type == pygame.KEYDOWN:


					if event.key == pygame.K_1 :
						x1-=20
					elif event.key==pygame.K_2:
						x1+=20
					elif event.key == pygame.K_3:
						p1bullet=True


					if event.key == pygame.K_KP_1:
						p2_x-=20
					elif event.key==pygame.K_KP_2:
						p2_x+=20
					elif event.key == pygame.K_KP_3:
						p2bullet=True

					if event.key == pygame.K_a :
						x1-=20
					elif event.key==pygame.K_d:
						x1+=20
					elif event.key == pygame.K_w:
						p1bullet=True
					elif event.key == pygame.K_s:
						p1AbilityTriggered=True

					
					if event.key == pygame.K_UP:
						p2bullet=True
					elif event.key == pygame.K_LEFT :
						p2_x-=20
					elif event.key==pygame.K_RIGHT:
						p2_x+=20
					elif event.key == pygame.K_DOWN:
						p2AbilityTriggered=True
				elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
					
					if arrowuhov:
						p2bullet=True

					if arrowlhov:
						P2LeftTriggered=True
					else:
						P2LeftTriggered=False

					if arrowrhov:
						P2RightTriggered=True
					else:
						P2RightTriggered=False

					if arrowdhov:
						p2AbilityTriggered=True
					else:
						p2AbilityTriggered=False

					if keywhov:
						p1bullet=True
					else:
						p1bullet=False

					if keyahov:
						P1RightTriggered=True
					else:
						P1RightTriggered=False

					if keydhov:
						P2LeftTriggered=True
					else:
						P2LeftTriggered=False

					if keyshov:
						p1AbilityTriggered=True
					else:
						p1AbilityTriggered=False
	#########################################################################
	###########################Bullet mechanics##############################					
			if p1bullet:
				y3-=10
				image1 = pygame.image.load(att1)
				gameDisplay.blit(image1, (x3, y3))
			if y3 == p2_y and x3 == p2_x:
				p2hlth-= plyrdamage
				x3=x1
				y3=y1
				p1bullet=False
			if y3 == 0:
				x3=x1
				y3=y1
				p1bullet=False
			if not p1bullet:
				x3=x1
				y3=y1
	##########################################################################
			if p2bullet:
				p2_Attack_y+=10
				image1 = pygame.image.load(att2)
				gameDisplay.blit(image1, (p2_Attack_x, p2_Attack_y))
			if p2_Attack_y == y1 and p2_Attack_x <= x1+50 and p2_Attack_x >= x1:
				plyrhlth-= p2Damage
				p2bullet=False
				p2_Attack_x=p2_x
				p2_Attack_y=p2_y

			if p2_Attack_y == 550:
				p2_Attack_x=p2_x+25
				p2_Attack_y=p2_y
				p2bullet=False

			if not p2bullet:
				p2_Attack_x=p2_x+25
				p2_Attack_y=p2_y
	#########################################################################
	################Keeping players within bounds############################
			if x1 <= 100:
				x1+=20

			if p2_x <= 100:
				p2_x+=20		

			if x1 >= 790:
				x1-=20

			if p2_x >= 790:
				p2_x-=20

	##########################################################################		
	################# buttons ################################################

			pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 85, 130, 35))

			text_surface = Font25.render('shoot(up)', True, (0, 0, 0))
			gameDisplay.blit(text_surface, (14,85))

			pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 129, 130, 35))

			text_surface = Font25.render('Ability(Down)', True, (0, 0, 0))
			gameDisplay.blit(text_surface, (14,129))

	##########################################################################

			pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 173, 130, 35))

			text_surface = Font25.render('move left( <-- )', True, (0, 0, 0))
			gameDisplay.blit(text_surface, (15,173))

	###########################################################################

			pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 217, 130, 35))

			text_surface = Font25.render('move right( --> )', True, (0, 0, 0))
			gameDisplay.blit(text_surface, (14,217))
	###############################################################################
	####################### borders  ##############################################
	########																#######
			text_surface = Font25.render('P1 CONTROLS', True, (0, 0, 0)) 		###
			gameDisplay.blit(text_surface, (14,450))
							
			text_surface = Font25.render('P2 CONTROLS', True, (0, 0, 0)) 		###
			gameDisplay.blit(text_surface, (14,50))							###
	#																			###
			pygame.draw.line(gameDisplay,black, (0, 270), (150, 270) ,6)	###
	#		pygame.draw.line(gameDisplay,black, (0, 478), (150, 478) ,6)    ###
			pygame.draw.line(gameDisplay,black, (150, 233), (150, 50),6)    ###
			pygame.draw.line(gameDisplay,black, (150, 233), (150, 478),6)   ###
			if Mouse_x > 0 and Mouse_x < 150:print()


	########																#######
	###############################################################################
	####################### player 1 ##############################################

			pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 277, 130, 35))

			text_surface = Font25.render('Attack(w)', True, (0, 0, 0))
			gameDisplay.blit(text_surface, (14,277))

			pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 322, 130, 35))

			text_surface = Font25.render('Ability(s)', True, (0, 0, 0))
			gameDisplay.blit(text_surface, (14,322))

	###########################################################################

			pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 366, 130, 35))
			text_surface = Font25.render('move left( a)', True, (0, 0, 0))
			gameDisplay.blit(text_surface, (14,366))
	###########################################################################

			pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 410, 130, 35))

			text_surface = Font25.render('move right( d )', True, (0, 0, 0))
			gameDisplay.blit(text_surface, (14,410))


	############################################################################
	####### button cord-testers ################################################ p2_x = x1 + 38
	#		pygame.draw.line(gameDisplay,red, (10, 330), (139, 330) ,1)
	#		pygame.draw.line(gameDisplay,red, (139, 330), (139, 368),1)
	#		pygame.draw.line(gameDisplay,red, (139, 368), (10, 368),1)
	#		pygame.draw.line(gameDisplay,red, (10, 330), (10, 368),1)

	############################################################################
	########################## mouse hover checkers ############################
			if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 85 and Mouse_y <=  120:
				arrowuhov = True
				pygame.draw.rect(gameDisplay,black,pygame.Rect(10, 85, 130, 35),2)
			else:
				arrowuhov = False
	############################################################################

			if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 129 and Mouse_y <= 164:
				pygame.draw.rect(gameDisplay,black,pygame.Rect(10, 129, 130, 35),2)
				arrowlhov= True
	#			print("l")
			else:
				arrowlhov=False
			
	############################################################################
			
			if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 173 and Mouse_y <= 208:
				pygame.draw.rect(gameDisplay,black,pygame.Rect(10, 173, 130, 35),2)
				arrowrhov= True
	#			print("l")
			else:
				arrowrhov=False
			
	############################################################################
			
			if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 217 and Mouse_y <= 252:
				pygame.draw.rect(gameDisplay,black,pygame.Rect(10, 217, 130, 35),2)
				arrowdhov= True
	#			print("l")
			else:
				arrowdhov=False
			
	#############################################################################
	#############################################################################
			if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 277 and Mouse_y <= 312:
				pygame.draw.rect(gameDisplay,black,pygame.Rect(10, 277, 130, 35),2)
				keywhov= True
	#			print("l")
			else:
				keywhov=False
			
	#############################################################################
			if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 322 and Mouse_y <= 357:
				pygame.draw.rect(gameDisplay,black,pygame.Rect(10, 322, 130, 35),2)
				keyshov= True
	#			print("l")
			else:
				keyshov=False

	#############################################################################		
			if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 366 and Mouse_y <= 401:
				pygame.draw.rect(gameDisplay,black,pygame.Rect(10, 366, 130, 35),2)
				keyahov= True
	#			print("l")
			else:
				keyahov=False
			
	#############################################################################
			if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 410 and Mouse_y <= 445:
				pygame.draw.rect(gameDisplay,black,pygame.Rect(10, 410, 130, 35),2)
				keydhov= True
	#			print("l")
			else:
				keydhov=False
			""""""
	############################################################################
	############################################################################
			if P2LeftTriggered:
				p2_x-=20

			if P2RightTriggered:
				p2_x+=20

			if P1RightTriggered:
				x1-=20

			if P2LeftTriggered:
				x1+=20
			P2LeftTriggered=False
			P2RightTriggered=False
			P2LeftTriggered=False
			P1RightTriggered=False
	#####################################################################################
	################################# Special Ability ###################################
	#####################################################################################
			if p1AbilityTriggered:
				p2hlth-= 20
				p1AbilityTriggered=False
			if p2AbilityTriggered:
				plyrhlth-= 20
				p2AbilityTriggered=False

			pygame.display.update()
			clock.tick(60)
	

			#Draw a box

p2b="M2D/bullet2/Lloyd.png"
p1b="M2D/bullets/Lloyd.png"
p1p="M2D/plyrs/s8.png"
lvl1(p1p,p1p,p2b,p1b)		
