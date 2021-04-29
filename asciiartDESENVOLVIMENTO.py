import os
import random
import sys
import matplotlib.pyplot as plt
import skimage
from skimage import data, color, io
from skimage.color import rgb2gray
from skimage.transform import rescale, resize, downscale_local_mean
def loadphoto():
	photo = io.imread(fname=sys.argv[1])
	r = 0
	g = 1
	b = 2
	asciiart = []
	for row in range(len(photo)):
		for col in range(len(photo[0])):
			#print(photo)
			asciiart.append(
			((int(photo[row,col,r]) 
			+int(photo[row,col,g]) 
			+int(photo[row,col,b]))/255)/3)
	if(sys.argv[2] == "cursed"):
		art(asciiart,len(photo[0]))
	elif(sys.argv[2] == "file"):
		write(asciiart,len(photo[0]))
	else:
		print("Escolha como segundo argumento cursed ou file" )
def brightness(i) :
	brightness = [" ",".",":","!","?","%","&","$","#","@"]
	switch = {
			"0.0" : brightness[0],
			"0.1" : brightness[1],
			"0.2" : brightness[2],
			"0.3" : brightness[3],
			"0.4" : brightness[4],
			"0.5" : brightness[5],
			"0.6" : brightness[6],
			"0.7" : brightness[7],
			"0.8" : brightness[8],
			"0.9" : brightness[9],
			"1.0"   : brightness[9]                      
			}
	return switch.get(i)
def art(art,limiter): 
	conta = 0
	render = []
	for i in range(len(art)):
		conta += 1
		render.append(brightness(str(round(art[i],1))))
		print(render[i], end = "")
		if(conta == limiter):
			conta = 0
print("\n")
def write(art,limiter):
	randomize = str(random.randint(1,60000))
	f = open("Ascii"+randomize+".txt", "w")
	conta = 0
	render = []
	for i in range(len(art)):
		conta += 1
		render.append(brightness(str(round(art[i],1))))
		f.write(render[i])
		if(conta == limiter):
			conta = 0
			f.write("\n")
	f.close
	print("sua file Ascii"+randomize+".txt foi criada com sucesso!")
loadphoto()               
# Comentario para o leandro ja que ele vai esquecer amanha ctz
# Seguinte você conseguiu converter os valores de claro e escuro para um array
# Agora você vai ter que converter esse valores para caracteres,e apos isso pegar
# o tamanho do seu row, e preencher com esses valores da array até daar esse tamanho
# boa sorte mlk brilha
