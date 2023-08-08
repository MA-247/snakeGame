import turtle

class Score(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color("white")
		self.goto(0, 270)

	def show_score(self, current_score):
		self.clear()
		self.write(f"Score: {current_score}", move=False, align="center", font=("courier", 15, 'bold'))

	def game_over(self):
		self.goto(0, 0)
		self.write("Game Over", align="center", font=("courier", 20,"bold"))	