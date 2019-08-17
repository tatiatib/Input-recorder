import pyglet
import time
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", default=None, type=str, required=True, help="The output file where JSON commands will be written")
args = parser.parse_args()

filename = args.o
window = pyglet.window.Window()

cur_schedule = []
start = time.time()

def add_to_schedule(x, y, event_type):
    schedule_entry = {"time":time.time() - start, "x":x, "y":y, "touchType":event_type}
    cur_schedule.append(schedule_entry)

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    add_to_schedule(x, y, "down")

@window.event
def on_mouse_press(x, y, button, modifiers):
    add_to_schedule(x, y, "down")

@window.event
def on_mouse_release(x, y, button, modifiers):
    add_to_schedule(x, y, "up")
    data = {"type":"Command", "commandId":"SynthesizeTouchInput", "touchSchedule": cur_schedule}
    with open(filename, "w") as file:
        file.write(json.dumps(data))

pyglet.app.run()
    