import pyglet

if __name__ == '__main__':
    window = pyglet.window.Window()
    pyglet.app.run()

    @window.event
    def on_draw():
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glBegin(GL_TRIANGLES)
        glVertex2f(0, 0)
        glVertex2f(window.width, 0)
        glVertex2f(window.width, window.height)
        glEnd()   
