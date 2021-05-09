from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import random, uniform
from kivy.graphics import Color, Ellipse, Line

class Ball(Widget):
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	color = ListProperty ([0,0,0])

	def move(self):
		self.color = self.color
		self.pos = Vector(*self.velocity) + self.pos

class BallGame(Widget):
	ball1 = Ball()
	ball2 = Ball()
	move1 = False
	move2 = False


	def startgame(self):
		color = [random(), random(), random()]
		color = (color[0]/(color[0]**2+color[1]**2)**0.5, color[1]/(color[0]**2+color[1]**2)**0.5, color[2]/(color[0]**2+color[1]**2)**0.5)
		self.ball1.color = color

		vel = (uniform(-1, 1), uniform(-1, 1))
		# change speed to 4
		vel = (vel[0]*4/(vel[0]**2+vel[1]**2)**0.5, vel[1]*4/(vel[0]**2+vel[1]**2)**0.5)

		self.ball1.velocity = vel

		color = [random(), random(), random()]
		color = (color[0]/(color[0]**2+color[1]**2)**0.5, color[1]/(color[0]**2+color[1]**2)**0.5, color[2]/(color[0]**2+color[1]**2)**0.5)
		self.ball2.color = color
		
		vel = (uniform(-1, 1), uniform(-1, 1))
		# change speed to 4
		vel = (vel[0]*4/(vel[0]**2+vel[1]**2)**0.5, vel[1]*4/(vel[0]**2+vel[1]**2)**0.5)

		self.ball2.velocity = vel

	def update(self, dt):
		self.ball1.move()
		self.ball2.move()

		# bounce off left and right
		if (self.ball1.x < 0) or (self.ball1.right > self.width):
			color = [random(), random(), random()]
			color = (color[0]/(color[0]**2+color[1]**2)**0.5, color[1]/(color[0]**2+color[1]**2)**0.5, color[2]/(color[0]**2+color[1]**2)**0.5)
			self.ball1.color = color
			self.ball1.velocity_x *= -1
		if (self.ball2.x < 0) or (self.ball2.right > self.width):
			color = [random(), random(), random()]
			color = (color[0]/(color[0]**2+color[1]**2)**0.5, color[1]/(color[0]**2+color[1]**2)**0.5, color[2]/(color[0]**2+color[1]**2)**0.5)
			self.ball2.color = color
			self.ball2.velocity_x *= -1
		# bounce off top and bottom
		if (self.ball1.y < 0) or (self.ball1.top > self.height):
			color = [random(), random(), random()]
			color = (color[0]/(color[0]**2+color[1]**2)**0.5, color[1]/(color[0]**2+color[1]**2)**0.5, color[2]/(color[0]**2+color[1]**2)**0.5)
			self.ball1.color = color
			self.ball1.velocity_y *= -1
		if (self.ball2.y < 0) or (self.ball2.top > self.height):
			color = [random(), random(), random()]
			color = (color[0]/(color[0]**2+color[1]**2)**0.5, color[1]/(color[0]**2+color[1]**2)**0.5, color[2]/(color[0]**2+color[1]**2)**0.5)
			self.ball2.color = color
			self.ball2.velocity_y *= -1
		# if collide
		if self.ball1.collide_widget(self.ball2):
			if self.ball1.velocity != [0, 0] and self.ball2.velocity != [0, 0]:
				print(self.ball1.velocity)
				temp = self.ball1.velocity_x
				self.ball1.velocity_x = self.ball2.velocity_x
				self.ball2.velocity_x = temp
				temp = self.ball1.velocity_y
				self.ball1.velocity_y = self.ball2.velocity_y
				self.ball2.velocity_y = temp

	def on_touch_up(self, touch):
		if BallGame.move1:
			self.ball1.x = touch.x - 25
			self.ball1.y = touch.y - 25
			BallGame.touch_border_change(self, self.ball1) 
			color = [random(), random(), random()]
			color = (color[0]/(color[0]**2+color[1]**2)**0.5, color[1]/(color[0]**2+color[1]**2)**0.5, color[2]/(color[0]**2+color[1]**2)**0.5)
			self.ball1.color = color
			vel = [uniform(-1, 1), uniform(-1, 1)]
			vel = [vel[0]*4/(vel[0]**2+vel[1]**2)**0.5, vel[1]*4/(vel[0]**2+vel[1]**2)**0.5]
			self.ball1.velocity = vel
			BallGame.move1 = False
		elif BallGame.move2:
			self.ball2.x = touch.x - 25
			self.ball2.y = touch.y - 25
			BallGame.touch_border_change(self, self.ball2) 
			color = [random(), random(), random()]
			color = (color[0]/(color[0]**2+color[1]**2)**0.5, color[1]/(color[0]**2+color[1]**2)**0.5, color[2]/(color[0]**2+color[1]**2)**0.5)
			self.ball2.color = color
			vel = [uniform(-1, 1), uniform(-1, 1)]
			vel = [vel[0]*4/(vel[0]**2+vel[1]**2)**0.5, vel[1]*4/(vel[0]**2+vel[1]**2)**0.5]
			self.ball2.velocity = vel
			BallGame.move2 = False


	def on_touch_down(self, touch):
		if self.ball1.collide_point(touch.x, touch.y):
			BallGame.move1 = True
		elif self.ball2.collide_point(touch.x, touch.y):
			BallGame.move2 = True

	def on_touch_move(self, touch):
		if BallGame.move1:
			self.ball1.x = touch.x - 25
			self.ball1.y = touch.y - 25
			BallGame.touch_border_change(self, self.ball1)
			self.ball1.velocity = [0, 0]
		if BallGame.move2:
			self.ball2.x = touch.x - 25
			self.ball2.y = touch.y - 25
			BallGame.touch_border_change(self, self.ball2)
			self.ball2.velocity = [0, 0]

	def touch_border_change(self, ball):
		if ball.x < 0:
			ball.x = 0
		elif ball.x > self.width - 50:
			ball.x = self.width - 50
		if ball.y < 0:
			ball.y = 0
		elif ball.y > self.height - 50:
			ball.y = self.height - 50

class BallApp(App):
	def build(self):
		game = BallGame()
		game.startgame()
		Clock.schedule_interval(game.update, 1.0 / 60.0)
		return game

if __name__ == '__main__':
	BallApp().run()
