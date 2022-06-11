#!/usr/bin/env python

import pydrm
import time

# Initialize the screen to white
drm = pydrm.SimpleDrm()
drm.draw.rectangle(
    (
        (0, 0),
        (drm.framebuffer.width, drm.framebuffer.height)
    ), fill='white', width=0
)
drm.flush()

time.sleep(2)
# print('Press ENTER to continue')
# input()


def draw_rect(x1, x2, y1, y2, color=0):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            offset = (y * drm.framebuffer.width + x) * 4
            # black = 0x00
            # drm.framebuffer.bo.map[offset] = 0x00
            for sub in range(4):
                drm.framebuffer.bo.map[offset + sub] = 0
    pydrm.framebuffer.DrmFramebuffer.flush(
        drm.framebuffer,
        x1 + 1,
        y1 + 1,
        x2 + 1,
        y2 + 1,
    )


for i in range(0, 500, 100):
    print('Drawing rect')
    draw_rect(i, i + 130, i, i + 130)
    # delay a bit so drawing starts on the previous rect
    time.sleep(0.07)

print('Press ENTER to finish')
input()
