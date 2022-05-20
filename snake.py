import curses as c
# import time
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from random import randint

c.initscr()
win = c.newwin(20,60,0,0)
win.keypad(1)
c.noecho()
c.curs_set(0)
win.border(0)
win.nodelay(1)

snake = [[4,10],[4,9],[4,8]]
food = [10,20]

win.addch(food[0], food[1], 'O')

key = KEY_RIGHT

while key != 27: #27 is ASCII for ESC
    win.border(0)
    win.timeout(100) #speed for snake
    default_key = key
    event = win.getch()
    key = key if event == -1 else event
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
        key = default_key
    
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), 
    snake[0][1] + (key == KEY_LEFT and -1)+ (key == KEY_RIGHT and 1)])

    if snake[0] == food:
        food = []
        while food == []:
            food = [randint(1,10), randint(1,58)]
            if food in snake:
                food = []
        win.addch(food[0], food[1], 'O')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], 'X')

    if snake[0] in snake[1:]:
        break
    
# time.sleep(10)
c.endwin()
