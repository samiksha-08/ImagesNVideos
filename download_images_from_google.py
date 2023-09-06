#Prerequests : pip install simple_image_download==0.4

from simple_image_download import simple_image_download as simp 

response = simp.simple_image_download

keywords = ["carrot cubes","onion cubes","chick peas","sliced dish mushrooms pieces raw"]   #specify names for downloading images 

for k in keywords:
    response().download(k, 3)      #response().download(iterater, no. of images to download)