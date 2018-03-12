#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Programa creado por https://github.com/Ssaki-chan
import sys
import Tkinter
import tkMessageBox
import tkFileDialog
import StringIO
import cmath,math 
gui = Tkinter.Tk()
ColorFondo="brown"
gui.configure(background=ColorFondo)
#Titulo del GUI
gui.title("LOGO")
#Dimensiones (ancho,alto,posicion x,posicion y)
gui.geometry("800x600")
w = Tkinter.Canvas(gui, width=780, height=361, bg="gray")
w.place(x=10, y=45)
#Delimitacion de la pantalla
gui.resizable(width=False,height=False)
#variables globales
#triangulo=Tkinter.PhotoImage(file='triangulo.gif') 
idioma="Español"
estado=False
Pgrados=0
grados=0
valorG=0
cx0=390
cy0=181
cx1=390
cy1=180
xP=[]
xF=[]
yP=[]
yF=[]
x=0
borrar=0
gradia=0
gradib=0 
Lgrados=[]
dibujarl=w.create_line(cx0,cy0,cx1,cy1,arrow="last",arrowshape=[15,15,15],fill=ColorFondo,tags='linea') 
def crearLinea():
	global xP,xF,yP,yF,x,dibujarl
	for i in range(x):
		w.itemconfig(dibujarl,arrow="last",arrowshape=[0,0,0])
		dibujarl=w.create_line(xP[i],yP[i],xF[i],yF[i],arrow="last",arrowshape=[15,15,15],fill=ColorFondo,tags='linea')
		#print xP[i],yP[i],xF[i],yF[i]
#Eventos de los botones 
def actAyuda():
	tkMessageBox.showinfo( "Ayuda","Comandos en Español \n av= Avanza || gd=gira a la derecha || gi= Gira la izquierda|| hogar= vuelve al lugar de inicio ||br=borrar|| re= retroceder"+"\n Commands in English \n fd = Forward || rr= turns right || rl = Turn left || home = returns to the starting || bk = back || cl = clear ")
def actErrorCodigo(palabraM):
	tkMessageBox.showinfo( "Error", "No se como realizar "+palabraM)			   

def actAviso(estado):
	if estado== True:
		tkMessageBox.showinfo( "Aviso","Catarina intento pasar un muro, regresa a casa con la cabeza quebrada.")
def idioma_assign():
	global idioma
	bandera=tkMessageBox.askyesno("Cambiar idioma","desea cambiar a idioma ingles")
	if bandera==True:
		BAyuda= Tkinter.Button (gui, text="Help", fg= "gold",bg="firebrick",width="10", height="1", command =actAyuda).place(x=700, y=10)
		BSalir= Tkinter.Button (gui, text="Exit", fg= "gold",bg="firebrick",width="15", height="3", command =gui.quit).place(x=670, y=430)
		BIdioma= Tkinter.Button (gui, text="Change language", fg= "gold",bg="firebrick",width="14", height="1",command=idioma_assign).place(x=580, y=10)
		BCapturar= Tkinter.Button (gui, text="Image capture", fg= "gold",bg="firebrick",width="15", height="3", command =gui.quit).place(x=550, y=430)
		BCargar= Tkinter.Button (gui, text="execute",fg= "gold",bg="firebrick",width="15", height="3",command=actAnalizador).place(x=550, y=510)
		BCargarr= Tkinter.Button (gui, text="Test Code",fg= "gold",bg="firebrick",width="15", height="3",command=llamada).place(x=670, y=510)
		idioma="Ingles"
	elif bandera==False:		
		BAyuda= Tkinter.Button (gui, text="Ayuda", fg= "gold",bg="firebrick",width="10", height="1", command =actAyuda).place(x=700, y=10)
		BSalir= Tkinter.Button (gui, text="Salir", fg= "gold",bg="firebrick",width="15", height="3", command =gui.quit).place(x=670, y=430)
		BIdioma= Tkinter.Button (gui, text="Cambiar idioma", fg= "gold",bg="firebrick",width="14", height="1",command=idioma_assign).place(x=580, y=10)
		BCapturar= Tkinter.Button (gui, text="Capturar Imagen", fg= "gold",bg="firebrick",width="15", height="3", command =gui.quit).place(x=550, y=430)
		BCargar= Tkinter.Button (gui, text="Ejecutar",fg= "gold",bg="firebrick",width="15", height="3",command=actAnalizador).place(x=550, y=510)
		BCargarr= Tkinter.Button (gui, text="Probar codigo",fg= "gold",bg="firebrick",width="15", height="3",command=llamada).place(x=670, y=510)
		idioma="Español"		
def actAnalizador():
	npalabra=str(palabra.get())
	#print npalabra
	tempo1=npalabra.split(' ')
	tempo2=tempo1
	#print tempo2
	global Pgrados,grados,valorG,cx0,cy0,cx1,cy1,borrar,gradia,gradib,Lgrados,xP,xF,yP,yF,x,dibujarl,w,estado
	#giros a la derecha 
	if ((idioma=="Español" and 'gd'==tempo2[0]) or (idioma=="Ingles" and 'rr'==tempo2[0])):
		Lgrados.append(tempo2[1])
		Pgrados=int(eval('+'.join(Lgrados)))
		#print eval('+'.join(Lgrados))
		grados=grados+int(round(Pgrados))
		lComandos.insert(Tkinter.END,palabra.get())
		if (grados>=0 or grados<=90):
			dif=90-grados
			Pgrados==90-dif
		elif (grados>90 or grados<=180):
			dif=180-grados
			Pgrados==180-dif
		elif (grados>180 or grados<=270):
			dif=270-grados
			Pgrados==270-dif
		elif (grados>270 or gradoss<360):
			dif=360-grados
			Pgrados==360-dif
		elif (gradoss==360):
			Pgrados==0   
			grados=0
		elif(gradoss==0):
			Pgrados==grados
		#giros izquierda	
	elif ((idioma=="Español" and tempo2[0]=="gi") or (idioma=="Ingles" and tempo2[0]=='rl')):
		Lgrados.append(tempo2[1])
		Pgrados=int(eval('+'.join(Lgrados)))
		#print eval('+'.join(Lgrados))
		Pgrados=int(Lgrados[0])
		grados= grados-int(round(Pgrados))
		lComandos.insert(Tkinter.END,palabra.get())
		if (grados<360):
			dif=grados*-1
			Pgrados=360-dif
		elif(grados==0):
			Pgrados=grados	
		elif(Pgrados==360):
			grados=0
	elif((idioma=="Español" and tempo2[0]=="br") or (idioma=="Ingles" and tempo2[0]=="cl")):
		w.delete(Tkinter.ALL)
		dibujarl=w.create_line(390,181,390,180,arrow="last",arrowshape=[15,15,15],fill=ColorFondo,tags='linea') 
		lComandos.insert(Tkinter.END,palabra.get())
	    #Home
	elif((idioma=="Español" and tempo2[0]=="hogar") or (idioma=="Ingles" and tempo2[0]=="home")):	
		cx0=390
		cy0=181
		cx1=390
		cy1=180
		Pgrados=0
		grados=0
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())	
		# grados directos 0, 90, 180, 270 y 360
		#==0
	elif ((idioma=="Español" and tempo2[0]=="av" and Pgrados==0) or (idioma=="Ingles" and tempo2[0]=='fd' and Pgrados==0)):
		valorG=int(tempo2[1])
		#print Pgrados
		cx0=cx1
		cy0=cy1
		cy1=cy0-valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#==180
	elif ((idioma=="Español" and tempo2[0]=="av" and Pgrados==180) or (idioma=="Ingles" and tempo2[0]=='fd' and Pgrados==180)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cy1=cy0+valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#==90
	elif ((idioma=="Español" and tempo2[0]=="av" and Pgrados==90) or (idioma=="Ingles" and tempo2[0]=='fd' and Pgrados==90)):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cx1=cx0+valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#==270
	elif ((idioma=="Español" and tempo2[0]=="av" and Pgrados==270) or (idioma=="Ingles" and tempo2[0]=='fd' and Pgrados==270)):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cx1=cx0-valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#avanza con diferentes grados
		#>0 or <90
	elif ((idioma=="Español" and tempo2[0]=="av" and (Pgrados>0 or Pgrados< 90)) or (idioma=="Ingles" and tempo2[0]=='fd' and (Pgrados>0 or Pgrados< 90))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0+gradiai
		gradibi=int(round(gradib))
		cy1=cy0-gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#>90 or <180
	elif ((idioma=="Español" and tempo2[0]=="av" and (Pgrados>90 or Pgrados< 180)) or (idioma=="Ingles" and tempo2[0]=='fd' and (Pgrados>90 or Pgrados < 180))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0+gradiai
		gradibi=int(round(gradib))
		cy1=cy0-gradibi	
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()	
		lComandos.insert(Tkinter.END,palabra.get())
		#>180 or <270
	elif ((idioma=="Español" and tempo2[0]=="av" and (Pgrados>180 or Pgrados< 270)) or  (idioma=="Ingles" and tempo2[0]=='fd' and (Pgrados>180 or Pgrados < 270))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0+gradiai
		gradibi=int(round(gradib))
		cy1=cy0-gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#>270 or <360
	elif ((idioma=="Español" and tempo2[0]=="av" and (Pgrados>270 or Pgrados< 360)) or (idioma=="Ingles" and tempo2[0]=='fd' and (Pgrados>270 or Pgrados < 360))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0+gradiai
		gradibi=int(round(gradib))
		cy1=cy0-gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#retroceder 
		#grados==0
	elif ((idioma=="Español" and tempo2[0]=="re" and Pgrados==0) or (idioma=="Ingles" and tempo2[0]=="bk" and Pgrados==0)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cy1=cy0+valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#grados==180
	elif ((idioma=="Español" and tempo2[0]=="re" and Pgrados==180) or (idioma=="Ingles" and tempo2[0]=='bk' and Pgrados==180)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cy1=cy0-valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#grados==90
	elif ((idioma=="Español" and tempo2[0]=="re" and Pgrados==90) or (idioma=="Ingles" and tempo2[0]=='bk' and Pgrados==90)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cx1=cx0-valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#grados==270
	elif ((idioma=="Español" and tempo2[0]=="re" and Pgrados==180) or (idioma=="Ingles" and tempo2[0]=='bk' and Pgrados==180)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cx1=cx0-valorG 
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#retroceder en cualquier grado
		#>0 or <90
	elif ((idioma=="Español" and tempo2[0]=="re" and (Pgrados>0 or Pgrados< 90)) or (idioma=="Ingles" and tempo2[0]=='bk' and (Pgrados>0 or Pgrados< 90))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0-gradiai
		gradibi=int(round(gradib))
		cy1=cy0+gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#>90 or <180
	elif ((idioma=="Español" and tempo2[0]=="re" and (Pgrados>90 or Pgrados< 180)) or (idioma=="Ingles" and tempo2[0]=='bk' and (Pgrados>90 or Pgrados< 180))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0-gradiai
		gradibi=int(round(gradib))
		cy1=cy0+gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#>180 or <270
	elif ((idioma=="Español" and tempo2[0]=="re" and (Pgrados>180 or Pgrados< 270)) or (idioma=="Ingles" and tempo2[0]=='bk' and (Pgrados>180 or Pgrados< 270))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0-gradiai
		gradibi=int(round(gradib))
		cy1=cy0+gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
		#>270 or <360
	elif ((idioma=="Español" and tempo2[0]=="re" and (Pgrados>270 or Pgrados< 360)) or  (idioma=="Ingles" and tempo2[0]=='bk' and (Pgrados>270 or Pgrados< 360))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0-gradiai
		gradibi=int(round(gradib))
		cy1=cy0+gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,palabra.get())
	else:
		actErrorCodigo(npalabra)
def actAnalizadorDoc(npalabra):
	#print npalabra
	tempo2=npalabra
	#print tempo2
	global Pgrados,grados,valorG,cx0,cy0,cx1,cy1,borrar,gradia,gradib,Lgrados,xP,xF,yP,yF,x
	#giros a la derecha 
	if ((idioma=="Español" and 'gd'==tempo2[0]) or (idioma=="Ingles" and 'rr'==tempo2[0])):
		Lgrados.append(tempo2[1])
		Pgrados=int(eval('+'.join(Lgrados)))
		#print eval('+'.join(Lgrados))
		grados=grados+int(round(Pgrados))
		lComandos.insert(Tkinter.END,npalabra)
		if (grados>=0 or grados<=90):
			dif=90-grados
			Pgrados==90-dif
		elif (grados>90 or grados<=180):
			dif=180-grados
			Pgrados==180-dif
		elif (grados>180 or grados<=270):
			dif=270-grados
			Pgrados==270-dif
		elif (grados>270 or gradoss<360):
			dif=360-grados
			Pgrados==360-dif
		elif (gradoss==360):
			Pgrados==0   
			grados=0
		elif(gradoss==0):
			Pgrados==grados
		#giros izquierda	
	elif ((idioma=="Español" and tempo2[0]=="gi") or (idioma=="Ingles" and tempo2[0]=='rl')):
		Lgrados.append(tempo2[1])
		Pgrados=int(eval('+'.join(Lgrados)))
		#print eval('+'.join(Lgrados))
		Pgrados=int(Lgrados[0])
		grados= grados-int(round(Pgrados))
		lComandos.insert(Tkinter.END,npalabra)
		if (grados<360):
			dif=grados*-1
			Pgrados=360-dif
		elif(grados==0):
			Pgrados=grados	
		elif(Pgrados==360):
			grados=0
	elif((idioma=="Español" and tempo2[0]=="br") or (idioma=="Ingles" and tempo2[0]=="cl")):
		w.delete(dibujarl)
		lComandos.insert(Tkinter.END,npalabra)
	    #Home
	elif((idioma=="Español" and tempo2[0]=="hogar") or (idioma=="Ingles" and tempo2[0]=="home")):		
		cx0=376
		cy0=166
		cx1=376
		cy1=166
		Pgrados=0
		grados=0
		lComandos.insert(Tkinter.END,npalabra)	
		# grados directos 0, 90, 180, 270 y 360
		#==0
	elif ((idioma=="Español" and tempo2[0]=="av" and Pgrados==0) or (idioma=="Ingles" and tempo2[0]=='fd' and Pgrados==0)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cy1=cy0-valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#==180
	elif ((idioma=="Español" and tempo2[0]=="av" and Pgrados==180) or (idioma=="Ingles" and tempo2[0]=='fd' and Pgrados==180)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cy1=cy0+valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#==90
	elif ((idioma=="Español" and tempo2[0]=="av" and Pgrados==90) or (idioma=="Ingles" and tempo2[0]=='fd' and Pgrados==90)):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cx1=cx0+valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#==270
	elif ((idioma=="Español" and tempo2[0]=="av" and Pgrados==270) or (idioma=="Ingles" and tempo2[0]=='fd' and Pgrados==270)):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cx1=cx0-valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#avanza con diferentes grados
		#>0 or <90
	elif ((idioma=="Español" and tempo2[0]=="av" and (Pgrados>0 or Pgrados< 90)) or (idioma=="Ingles" and tempo2[0]=='fd' and (Pgrados>0 or Pgrados< 90))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0+gradiai
		gradibi=int(round(gradib))
		cy1=cy0-gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#>90 or <180
	elif ((idioma=="Español" and tempo2[0]=="av" and (Pgrados>90 or Pgrados< 180)) or (idioma=="Ingles" and tempo2[0]=='fd' and (Pgrados>90 or Pgrados < 180))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0+gradiai
		gradibi=int(round(gradib))
		cy1=cy0-gradibi	
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()	
		lComandos.insert(Tkinter.END,npalabra)
		#>180 or <270
	elif ((idioma=="Español" and tempo2[0]=="av" and (Pgrados>180 or Pgrados< 270)) or  (idioma=="Ingles" and tempo2[0]=='fd' and (Pgrados>180 or Pgrados < 270))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0+gradiai
		gradibi=int(round(gradib))
		cy1=cy0-gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#>270 or <360
	elif ((idioma=="Español" and tempo2[0]=="av" and (Pgrados>270 or Pgrados< 360)) or (idioma=="Ingles" and tempo2[0]=='fd' and (Pgrados>270 or Pgrados < 360))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0+gradiai
		gradibi=int(round(gradib))
		cy1=cy0-gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#retroceder 
		#grados==0
	elif ((idioma=="Español" and tempo2[0]=="re" and Pgrados==0) or (idioma=="Ingles" and tempo2[0]=="bk" and Pgrados==0)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cy1=cy0+valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#grados==180
	elif ((idioma=="Español" and tempo2[0]=="re" and Pgrados==180) or (idioma=="Ingles" and tempo2[0]=='bk' and Pgrados==180)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cy1=cy0-valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#grados==90
	elif ((idioma=="Español" and tempo2[0]=="re" and Pgrados==90) or (idioma=="Ingles" and tempo2[0]=='bk' and Pgrados==90)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cx1=cx0-valorG
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#grados==270
	elif ((idioma=="Español" and tempo2[0]=="re" and Pgrados==180) or (idioma=="Ingles" and tempo2[0]=='bk' and Pgrados==180)):
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		cx1=cx0-valorG 
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#retroceder en cualquier grado
		#>0 or <90
	elif ((idioma=="Español" and tempo2[0]=="re" and (Pgrados>0 or Pgrados< 90)) or (idioma=="Ingles" and tempo2[0]=='bk' and (Pgrados>0 or Pgrados< 90))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0-gradiai
		gradibi=int(round(gradib))
		cy1=cy0+gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#>90 or <180
	elif ((idioma=="Español" and tempo2[0]=="re" and (Pgrados>90 or Pgrados< 180)) or (idioma=="Ingles" and tempo2[0]=='bk' and (Pgrados>90 or Pgrados< 180))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0-gradiai
		gradibi=int(round(gradib))
		cy1=cy0+gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#>180 or <270
	elif ((idioma=="Español" and tempo2[0]=="re" and (Pgrados>180 or Pgrados< 270)) or (idioma=="Ingles" and tempo2[0]=='bk' and (Pgrados>180 or Pgrados< 270))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0-gradiai
		gradibi=int(round(gradib))
		cy1=cy0+gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
		#>270 or <360
	elif ((idioma=="Español" and tempo2[0]=="re" and (Pgrados>270 or Pgrados< 360)) or  (idioma=="Ingles" and tempo2[0]=='bk' and (Pgrados>270 or Pgrados< 360))):	
		valorG=int(tempo2[1])
		cx0=cx1
		cy0=cy1
		gradia=math.radians(Pgrados)
		gradia=math.sin(gradia)
		gradia=gradia*valorG
		gradib=math.radians(Pgrados)
		gradib=math.cos(gradib)
		gradib=gradib*valorG
		gradiai=int(round(gradia))
		cx1=cx0-gradiai
		gradibi=int(round(gradib))
		cy1=cy0+gradibi
		xP.append(cx0)
		xF.append(cx1)
		yP.append(cy0)
		yF.append(cy1)
		x=x+1
		crearLinea()
		lComandos.insert(Tkinter.END,npalabra)
	else:
		actErrorCodigo(npalabra)
def llamada():
	nombre = tkFileDialog.askopenfilename(title="Probar logo")
	archivo=open(nombre,'r')
	for linea in archivo:
		arch2=linea.strip()
		arch2=arch2.split(' ')
		actAnalizadorDoc(arch2)

#paneles donde se van a mostrar el codigo
palabra=Tkinter.StringVar()
lComandos = Tkinter.Listbox(gui, height=6,width=80,bg=ColorFondo, fg="gray")
lComandos.place(x=10, y= 420)
Vcodigo= Tkinter.Entry(gui,bg="gray",textvar=palabra,width=80).place (x=10, y=530)
#Botones
Titulo=Tkinter.Label(gui, text="LOGO CON PYTHON").place(x=10,y=12)
BAyuda= Tkinter.Button (gui, text="Ayuda", fg= "gold",bg="firebrick",width="10", height="1", command =actAyuda).place(x=700, y=10)
BSalir= Tkinter.Button (gui, text="Salir", fg= "gold",bg="firebrick",width="15", height="3", command =gui.quit).place(x=670, y=430)
BIdioma= Tkinter.Button (gui, text="Cambiar idioma", fg= "gold",bg="firebrick",width="14", height="1",command=idioma_assign).place(x=580, y=10)
BCapturar= Tkinter.Button (gui, text="Capturar Imagen", fg= "gold",bg="firebrick",width="15", height="3", command =gui.quit).place(x=550, y=430)
BCargar= Tkinter.Button (gui, text="Ejecutar",fg= "gold",bg="firebrick",width="15", height="3",command=actAnalizador).place(x=550, y=510)
BCargarr= Tkinter.Button (gui, text="Probar codigo",fg= "gold",bg="firebrick",width="15", height="3",command=llamada).place(x=670, y=510)
#Cargar el GUI
gui.mainloop()