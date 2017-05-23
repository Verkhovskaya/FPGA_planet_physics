import numpy as np
import cv2
import copy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

positions_file = open("/Users/2017-A/Dropbox/fpga_simulation_result.txt")
data = []

count = 0

new_frame = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for frame in range(500):
    object_num = int(positions_file.readline().rstrip(), 2)
    while object_num > 8:
        object_num = int(positions_file.readline().rstrip(), 2)
        print "Out of line"
    skip1 = positions_file.readline().rstrip()
    x_position = int(positions_file.readline().rstrip(), 2)
    skip3 = positions_file.readline().rstrip()
    y_position = int(positions_file.readline().rstrip(), 2)
    skip2 = positions_file.readline().rstrip()
    if (skip1 != skip2):
        print "error"
    else:
        new_frame[object_num] = [x_position, y_position]
        data.append(copy.copy(new_frame))

for line in data:
    print line

slides = []
count = 0
for line in data:
    img = np.zeros((650, 1290, 3), np.uint8)
    if line != "error":
        #faster to copy paste :)
        point = line[0]
        cv2.circle(img, (point[0]*10+10,point[1]*10+10), 5, (255, 0, 0), 3)
        point = line[1]
        cv2.circle(img, (point[0]*10+10,point[1]*10+10), 5, (0, 255, 0), 3)
        point = line[2]
        cv2.circle(img, (point[0]*10+10,point[1]*10+10), 5, (0, 0, 255), 3)
        point = line[3]
        cv2.circle(img, (point[0]*10+10,point[1]*10+10), 5, (255, 255, 0), 3)
        point = line[4]
        cv2.circle(img, (point[0]*10+10,point[1]*10+10), 5, (255, 0, 255), 3)
        point = line[5]
        cv2.circle(img, (point[0]*10+10,point[1]*10+10), 5, (0, 255, 255), 3)
        point = line[6]
        cv2.circle(img, (point[0]*10+10,point[1]*10+10), 5, (255, 255, 255), 3)
        point = line[7]
        cv2.circle(img, (point[0]*10+10,point[1]*10+10), 5, (0, 100, 0), 3)
    cv2.imwrite('/Users/2017-A/Dropbox/mojo_projects/physics_simulator_2/physics_simulator_3/computer_side/fpga_results/'+str(count)+'.png',img)
    count += 1
    cv2.imshow("word", img)
    cv2.waitKey(0)
