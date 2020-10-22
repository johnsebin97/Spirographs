#pip install pycairo

import cairo
import math

WIDTH = 30
HEIGHT = 30
PIXEL_SCALE = 20

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH*PIXEL_SCALE, HEIGHT*PIXEL_SCALE)
ctx = cairo.Context(surface)
ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.fill()

ctx.translate(WIDTH/2, HEIGHT/2)

# Create the spirograph points
def create_spiro(a, b, d):
    dt = 0.01
    t = 0
    pts = []
    while t < 2*math.pi*b/math.gcd(a, b):
        t += dt
        x = (a - b) * math.cos(t) + d * math.cos((a - b)/b * t)
        y = (a - b) * math.sin(t) - d * math.sin((a - b)/b * t)
        pts.append((x, y))
    return pts

# Draw the curve
def draw_spiro(ctx, a, b, d, color):
    ctx.set_line_width(.1)
    ctx.set_source_rgb(*color)
    pts = create_spiro(a, b, d)
    ctx.move_to(pts[0][0], pts[0][1])
    for x, y in pts[1:]:
        ctx.line_to(x, y)
    ctx.stroke()

#0
#draw_spiro(ctx, 16, 11, 7, (0, 0, 0.5))

#1
#for b in range(8, 15):
#    draw_spiro(ctx, 16, b, 7, (0, 0, 0.5))

#2
#for i, a in enumerate(range(8, 16, 2)):
#    draw_spiro(ctx, a, 9, 7, (i*.25, 0, 1-i*.25))

#3
for d in range(50, 80, 5):
    draw_spiro(ctx, 11, 7, d/10, (1, 0.5, 0))
    ctx.rotate(0.03)


surface.write_to_png('spirograph3.png')