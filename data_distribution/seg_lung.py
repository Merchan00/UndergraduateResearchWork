# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 22:10:29 2022

@author: Juan Suarez
"""

import numpy as np 
import skimage.measure as measure
import cv2
from PIL import Image, ImageDraw
from scipy.spatial import ConvexHull


def contour_distance(contour):
    dx = contour[0, 1] - contour[-1, 1]
    dy = contour[0, 0] - contour[-1, 0]
    return np.sqrt(np.power(dx, 2) + np.power(dy, 2))

def set_is_closed(contour):
    if contour_distance(contour) < round(10):
        return True
    else:
        return False


def maskara(actual,case):
    if case==1:
        filtrado = cv2.blur(actual,(15,15))
    else:
        filtrado = cv2.blur(actual,(9,9))
        
    minim=np.min(filtrado)
    minim=-400
    maxim=-600
    #--------------
    n1,m1=np.shape(filtrado)
    imagenr=np.zeros((n1,m1))
    
    for i in range(n1):
        for j in range(m1):
            if filtrado[i,j]>=minim and filtrado[i,j]<=maxim:
                imagenr[i,j]=filtrado[i,j]
            elif filtrado[i,j]>=maxim:
                imagenr[i,j]=np.max(filtrado)
    
    if case==1:
        imagenr[:,450:]=0
        imagenr[:10,100:450]=np.max(filtrado)
    elif case==2:
        imagenr[:10,:]=np.max(filtrado)
    elif case==3:
        imagenr[100:200,200:370]=np.max(filtrado)
           
    ff=measure.find_contours(imagenr, 0.95)
    
    
    contornos_cuerpo_y_pulmones = [] 
    volumen_contornos = [] 
    
    
    for contour in ff:
        hull = ConvexHull(contour,qhull_options="QJ Pp")
    
        if hull.volume > 1900 and set_is_closed(contour):
            contornos_cuerpo_y_pulmones.append(contour)
            volumen_contornos.append(hull.volume)
    
    if len(contornos_cuerpo_y_pulmones) == 2:
        contornos_cuerpo_y_pulmones=contornos_cuerpo_y_pulmones
    elif len(contornos_cuerpo_y_pulmones) > 2:
        volumen_contornos, contornos_cuerpo_y_pulmones = (list(t) for t in
                zip(*sorted(zip(volumen_contornos, contornos_cuerpo_y_pulmones))))
        contornos_cuerpo_y_pulmones.pop(-1) 
        
    
    lung_mask = np.array(Image.new('L',(m1, n1), 0))
    for contour in contornos_cuerpo_y_pulmones:
        x = contour[:, 1]
        y = contour[:, 0]
        polygon_tuple = list(zip(x, y))
        img = Image.new('L',  (m1, n1), 0)
        ImageDraw.Draw(img).polygon(polygon_tuple, outline=0, fill=1)
        mask = np.array(img)
        lung_mask += mask
    
    lung_mask[lung_mask > 1] = 1  # sanity check to make 100% sure that the mask is binary
             
    imxx = cv2.rotate(lung_mask, cv2.ROTATE_90_CLOCKWISE)
    imxx = cv2.rotate(imxx, cv2.ROTATE_90_CLOCKWISE)
    fp = cv2.flip(imxx,1)
    
    return fp  


