import pyglet

music = pyglet.media.load('alarm.wav')
music.play()
def exiter(dt):
    pyglet.app.exit()
print "Song length is: %f" % music.duration

pyglet.clock.schedule_once(exiter, music.duration)
pyglet.app.run()

