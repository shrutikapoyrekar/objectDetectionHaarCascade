# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:36:05 2022

@author: admin
"""

import cv2 
image = cv2.imread("positive/1596724594.7233658.jpg")


start_point = (892, 363)
end_point = (892+132 , 363+142 )
color = (255, 0, 0)
image = cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)


#913 2 104 51

start_point = (913, 2)
end_point = (913+104 , 2+51 )
color = (255, 0, 0)
image = cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)

cv2.imwrite("newImage.jpg",image)

