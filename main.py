import snake
import turtle
import time
import food
import score

screen = turtle.Screen()
food = food.Food()
score = score.Score()
curr_score = 0
score.show_score(curr_score)
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)


#snake:

snake = snake.Snake()
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
		
curr_score = 0

game_continues = True

while(game_continues):
	screen.update()
	time.sleep(0.1)
	snake.movement()
	

	#food collision detection:

	if snake.head.distance(food) < 15:
		food.new_location()
		curr_score += 1
		snake.extend()
		score.show_score(curr_score)

	#wall collision detection:

	if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
		game_continues = False

	#snake tail collision detection:

	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
				game_continues = False
				score.game_over()	

score.game_over()

screen.exitonclick()