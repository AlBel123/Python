import turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
TURN_ANGLE = 90
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        # 3 -segments snake creation and starting position setting. Option 2
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = turtle.Turtle(shape="circle")
        segment.color("purple", "violet")
        segment.penup()
        segment.setpos(position)
        self.snake_list.append(segment)

    def extend_snake(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for seg in range(len(self.snake_list) - 1, 0, -1):
            new_position_x = self.snake_list[seg - 1].xcor()
            new_position_y = self.snake_list[seg - 1].ycor()
            self.snake_list[seg].goto(new_position_x, new_position_y)
        self.head.forward(MOVE_DISTANCE)
        # self.snake_list[0].left(TURN_ANGLE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.snake_list:
            segment.goto(1000,1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]
