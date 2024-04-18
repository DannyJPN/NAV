import turtle
from LSystem.LSystemModel import LSystemModel


class LSystemRender:
    def __init__(self, animation: bool = True):
        self.animation = animation

    def render(self, model: LSystemModel):
        t = turtle.Turtle()
        window = turtle.Screen()
        window.setup(width=1.0, height=1.0)
        t.up()
        # t.back(200)
        t.goto(model.start_pos[0], model.start_pos[1])
        t.down()
        turtle.delay(0)
        if not self.animation:
            turtle.tracer(0, 0)
        stack = []
        for command in model.instructions:
            if command == 'F':
                t.forward(model.distance)
            elif command == '+':
                t.right(model.angle)
            elif command == '-':
                t.left(model.angle)
            elif command == '[':
                stack.append(t.pos())
            elif command == ']':
                pos = stack.pop()
                t.penup()
                t.goto(pos[0], pos[1])
                t.pendown()

        turtle.update()
        # window.exitonclick()


