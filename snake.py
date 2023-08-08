import turtle

STARTING_LENGTH = 3

class Snake:

	def __init__(self):
		self.create_snake()
		
	def create_snake(self):
		self.segments = []
		x_pos = -20
		for x in range(0, STARTING_LENGTH):
			self.add_segment((x_pos,0))
			x_pos -= 20

		self.head = self.segments[0]	

	def add_segment(self, position):
			turtle_obj = turtle.Turtle()
			turtle_obj.penup()
			turtle_obj.shape("square")
			turtle_obj.color("white")
			turtle_obj.goto(position)
			self.segments.append(turtle_obj)
			
			

	def extend(self):
		self.add_segment(self.segments[-1].position())

	def movement(self):
		for x in range(len(self.segments) - 1 ,0 , -1):
			self.segments[x].goto(self.segments[x-1].pos())
		self.head.forward(20)

	def up(self):
		if (self.head.heading() != 270):
			self.head.setheading(90)	
		
	def down(self):
		if (self.head.heading() != 90):
			self.head.setheading(270)	
		
	def left(self):
		if (self.head.heading() != 0):
			self.head.setheading(180)	
		
	def right(self):
		if (self.head.heading() != 180):
			self.head.setheading(0)	
		
				