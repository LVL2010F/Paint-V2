#by LVL2010F
from turtle import *
from random import *
from ion import *
speed(10)
color('orange')
forward(1)
backward(1)
a=1
left(90)
while True:
  if a<0:
    a=0
  if a>100:
    a=100
  pensize(a)
  if keydown(KEY_UP):
    forward(5)
  if keydown(KEY_DOWN):
    backward(5)
  if keydown(KEY_LEFT):
    left(5)
  if keydown(KEY_RIGHT):
    right(5)
  if keydown(KEY_OK):
    a=randint(1,100)
  if keydown(KEY_ONE):
    a=10
  if keydown(KEY_TWO):
    a=20
  if keydown(KEY_THREE):
    a=30
  if keydown(KEY_FOUR):
    a=40
  if keydown(KEY_FIVE):
    a=50
  if keydown(KEY_SIX):
    a=60
  if keydown(KEY_SEVEN):
    a=70
  if keydown(KEY_EIGHT):
    a=80
  if keydown(KEY_NINE):
    a=90
  if keydown(KEY_ZERO):
    a=1
  if keydown(KEY_PLUS):
    a=a+5
  if keydown(KEY_MINUS):
    a=a-5
  if keydown(KEY_VAR):
    color('blue')
  if keydown(KEY_TOOLBOX):
    color('red')
  if keydown(KEY_BACKSPACE):
    color('green')
  if keydown(KEY_EXP):
    color('yellow')
  if keydown(KEY_LN):
    color('brown')
  if keydown(KEY_LOG):
    color('black')
  if keydown(KEY_IMAGINARY):
    color('white')
  if keydown(KEY_COMMA):
    color('pink')
  if keydown(KEY_POWER):
    color('orange')
  if keydown(KEY_SINE):
    color('purple')
  if keydown(KEY_COSINE):
    color('gray')
  if keydown(KEY_SHIFT):
    left(90)
    forward(5)
    right(90)
  if keydown(KEY_ALPHA):
    right(90)
    forward(5)
    left(90)
  if keydown(KEY_XNT):
    goto(0,0)
  if keydown(KEY_ANS):
    write(input())
  if keydown(KEY_DIVISION):
    forward(5)
    penup()
    forward(5)
    pendown()
  if keydown(KEY_MULTIPLICATION):
    backward(5)
    penup()
    backward(5)
    pendown()
  if keydown(KEY_LEFTPARENTHESIS):
    penup()
    left(90)
    forward(5)
    right(90)
    pendown()
    left(90)
    forward(5)
    right(90)
  if keydown(KEY_RIGHTPARENTHESIS):
    penup()
    right(90)
    forward(5)
    left(90)
    pendown()
    right(90)
    forward(5)
    left(90)
  b=randint(1,3)  
  if keydown(KEY_DOT):
   if b==1:
     color('green')
   elif b==2:
    color('red')
   elif b==3:
    color('blue')