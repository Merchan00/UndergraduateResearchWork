# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 18:33:03 2023

@author: bioimag

Organizar dataset

train
    image
        file
    masks
        file

test
    image
        file

"""

import os
import nibabel as nib
import matplotlib.pyplot as plt
import cv2
import numpy as np
import time
import pygame
from tqdm import tqdm
from seg_lung import maskara
#import seg_lung
#%%
#path="D:\\Preprocesamiento\\DATA_w_mask\\train" 
#path="E:\\Trabajo_de_grado\\Preprocesamiento\\DATA_org\\train"
path="D:\\Preprocesamiento\\DATA_w_mask\\test"

def mix(img1,img2):
    n,m=img1.shape
    aux=np.zeros((n,m))
    
    for i in range(n):
        for j in range(m):
            if img2[i][j]==1:
                aux[i][j]=img1[i][j]
            else:
                aux[i][j]=np.min(img1)
    
    return aux


def guardar_img(img_pac,paciente,slide,ruta,nombre_save):
    #nombre_save=paciente+"_slide"+"_"+str(slide)    
    nombre_save=nombre_save
    guardar=ruta
    ruta_save=guardar,"\\",nombre_save
    ruta_save=''.join(ruta_save)   
    plt.imshow(img_pac,cmap="gray", origin='lower')
    plt.axis('off')
    plt.tight_layout() 
    my_dpi=89.83
    plt.savefig(ruta_save,bbox_inches="tight",pad_inches=0.0,dpi=my_dpi)
    plt.clf()  
    print(nombre_save+'.png ..... create')
    #print("\n")    


archivo_org="D:\\Preprocesamiento\\validation" #archivo original 
data_org=os.listdir(archivo_org)

#%%
z=0
for z in range(len(data_org)):
#for f in tqdm(data_org):
    
    inicio = time.time()    
    try:
        #archivo de la imagen
        archivo=archivo_org+"\\"+data_org[z]+"\\"+"image"+"\\"+data_org[z]+".nii.gz"
        img=nib.load(archivo)
        img_data = img.get_fdata()
              
    
    except:
        print("No se encontró el archivo: "+data_org[z])


    for i in range(70,231):        
        #print("Entre Paciente: "+data_org[z]+"img:"+str(i))
        #print("."*30)
        
        try:
            d_name=data_org[z]
            d_name=d_name[:8]
            folder_name=d_name+"_slide"+"_"+str(i)
            folder=path+"\\"+folder_name
            os.mkdir(folder)
        
            
            aux=img_data[i,:,:]
            aux=(aux-np.min(aux))/(np.max(aux)-np.min(aux))
            aux=cv2.rotate(aux, cv2.ROTATE_90_COUNTERCLOCKWISE)
            aux2=maskara(aux,1)   
            #
            
            imagen=mix(aux,aux2)
            
            try: 
                #image
                folder_img=folder+"\\"+"image"
                os.mkdir(folder_img)
                ruta=folder+"\\"+"image\\"
                nombre_save=folder_name
                guardar_img(imagen,data_org[z],i,ruta,nombre_save)
                """
                #label
                folder_mask=folder+"\\"+"masks"
                os.mkdir(folder_mask)
                ruta=folder+"\\"+"masks\\"
                nombre_save=folder_name+"_mask"
                guardar_img(aux2,data_org[z],i,ruta,nombre_save)
                """
                
            except:
                print("Carpeta ya creada")
            
        except:
            print("Carpeta ya creada _v")
            pass
        
               
        
        #aux2=maskara(aux,1)    
        #aux=(aux-np.min(aux))/(np.max(aux)-np.min(aux))
        #aux=cv2.rotate(aux, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #aux=cv2.rotate(aux, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #aux=cv2.rotate(aux, cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        #aux2=img_data2[i,:,:]
        #aux2=cv2.flip(aux2,0)
        #aux2=cv2.rotate(aux2, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #aux2=cv2.rotate(aux2, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #aux2=cv2.rotate(aux2, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #imagen=mix(aux,aux2)
        
        #rotate to save
        #imagen=cv2.rotate(imagen, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #imagen=cv2.rotate(imagen, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #imagen=cv2.rotate(imagen, cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        #----
        
            
        
    
    """
    for i in range(300,440):        
        #print("Entre Paciente: "+data_org[z]+"img:"+str(i))
        #print("."*30)
        aux=img_data[i,:,:]
        #aux2=maskara(aux,1)    
        aux=(aux-np.min(aux))/(np.max(aux)-np.min(aux))
        aux=cv2.rotate(aux, cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        #aux2=img_data2[i,:,:]
        #aux2=cv2.flip(aux2,0)
        #aux2=cv2.rotate(aux2, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #imagen=mix(aux,aux2)
        
        #rotate to save
        #imagen=cv2.rotate(imagen, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #imagen=cv2.rotate(imagen, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #imagen=cv2.rotate(imagen, cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        #----
        try: 
            #paciente
            d_name=data_org[z]
            d_name=d_name[:8]
            folder_name=d_name+"_slide"+"_"+str(i)
            folder=path+"\\"+folder_name
            os.mkdir(folder)
            #image
            folder_img=folder+"\\"+"image"
            os.mkdir(folder_img)
            ruta=folder+"\\"+"image\\"
            nombre_save=folder_name
            guardar_img(aux,data_org[z],i,ruta,nombre_save)
            #label
            folder_img=folder+"\\"+"masks"
            os.mkdir(folder_img)
            ruta=folder+"\\"+"image\\"
            nombre_save=folder_name+"_mask"
            guardar_img(aux2,data_org[z],i,ruta,nombre_save)
            
            
        except:
            print("Carpeta ya creada")    
    """
    fin = time.time()
    tiempo=(fin-inicio)/60
    print("\nPaciente "+data_org[z]+" tardó: "+ str(tiempo) +" minutos")
    z=z+1
