#PREGUNTAR
# IP APUNTA SIGUIENTE OPCION
#LECTURA DE REGISTROS
#AUMENTAR VALOR DE REGISTROS
#PREGUNTAR QUE VA DE ARGUMENTO EN LOS IFS
#---------------------------------------

# 24/06 Maquina virtual

#Usamos una clase para definir la maquina virtual
class maquina_virtual:
	#Definimos los atributos (caracteristicas) de la MV
	def__init__(self):
		self.memoria = [0] * 65536 #Vector que representa la memoria 0 a 65535
        self.xp = 1028                #Variable entera que representa registro XP
        self.ip = 100			   #Variable entera que representa registro IP

#Cargar en memoria de MV archivo binario
    #Definir metodo para abrir archivo y cargarlo
    def__ejecutar(self, archivo):
    	self.cargar_archivo(archivo)

#Carga archivo en registro IP, en sus posiciones
    #Se crea un bucle para que el registro IP vaya cargando los datos contenidos en el
    #archivo binario cargado. Mientras que la posicion del registro IP sea menor a la
    #longitud del archivo binario, seguira leyendo y almacenando estos datos en el 
    #registro IP, aumentando su posicion en 1 en cada pasaje por el ciclo.
    	while self.ip < len(archivo): 
    		opcode += archivo[self.ip]
    		self.ip += 1

#Comprobar a que tipo de operacion (MOV, JMP, etc) hace referencia el opcode
	#'>>' desplaza el valor del opcode hacia la derecha 4 posiciones, para aislar los 
	#primeros 4 bits, lo que permite compararlos con el opcode correspondiente a la funcion
	#Ejemplo: si fuera el opcode '0xA2' se tomaria solo '0xA' ignorando el '2'
	
	hex(opcode)

#Opcode 0xA0: Mueve una constante a una posición de memoria. Recibe dos parámetros, 
#primero la dirección de memoria y luego el valor.
	def__ejecutar_mov0(self, constante, posicion_memoria):
		constante = 1
		posicion_memoria = 1025
		memoria[posicion_memoria] = constante

#Opcode 0xA1: Mueve el contenido del registro IP (100) a una posición de memoria. Recibe como 
#parámetro la posición de memoria inicial. Tome en cuenta que los registros son de 16 
#bits, con lo cual almacenará los primeros 8 en la dirección recibida como parámetro y 
#los restantes en la posición de memoria siguiente.
	def__ejecutar_mov1(self, posicion_memoria):
		self.memoria[posicion_memoria] = ip >> 8
		self.memoria[posicion_memoria+1] = ip & 0xFF

#Opcode 0xA2: Mueve el contenido de una posición de memoria al registro IP. Recibe como 
#parámetro la posición de memoria inicial. Tome en cuenta que los registros son de 16 bits, 
#con lo cual obtendrá los primeros 8 en la dirección recibida como parámetro y los restantes 
#en la posición de memoria siguiente.
	def__ejecutar_mov2(self, posicion_memoria):
		self.ip[posicion_memoria] = posicion_memoria >> 8
		self.ip[posicion_memoria+1] = posicion_memoria & 0xFF

#Opcode 0xA3: Mueve valores entre posiciones de memoria. Recibe dos parámetros, el primero es
#la posición de memoria de origen, y el segundo es la posición de memoria de destino.
	def__ejecutar_mov3(self, posicion_memoria_origen, posicion_memoria_destino):
		posicion_memoria_origen = 1026
		posicion_memoria_destino = 1027
		valor1 = self.memoria[posicion_memoria_origen] 
		self.memoria[posicion_memoria_destino] = valor1
	
#Opcode 0xA4: Mueve el valor desde una posición de memoria, a la posición de memoria que 
#contiene XP. Es decir, si XP contiene D1FA el valor se moverá a esa dirección de memoria. 
#Recibe sólo un parámetro, la posición de memoria de origen, ya que el destino se encuentra 
#en XP.
	def__ejecutar_mov4(self, posicion_memoria_origen):
		valor1 = self.memoria[posicion_memoria_origen]
		self.memoria[self.xp] = self.memoria[valor1]

#Opcode 0xA5: Mueve el valor desde la posición de memoria que contiene XP, a otra posición de 
#memoria. Es decir, si XP contiene el D1FA el valor se moverá desde esa dirección de memoria 
#a otra que se recibe como parámetro. Recibe sólo un parámetro, la posición de memoria de 
#destino, ya que el origen se encuentra en XP.
	def__ejecutar_mov5(self, posicion_memoria_destino):
		self.memoria[posicion_memoria_destino] = self.memoria[self.xp] >> 8
		self.memoria[posicion_memoria_destino+1] = self.memoria[self.xp] & 0xFF

#Opcode 0xA6: Mueve el contenido de XP a una posición de memoria. En este caso si se mueve 
#el contenido de XP, es decir, si XP contiene D1FA, D1 se movera a la posición de memoria 
#recibida como parámetro y FA a la posición siguiente. Recibe sólo un parámetro, que es la 
#posición de memoria de destino.
	def__ejecutar_mov6(self, posicion_memoria_destino):
		self.memoria[posicion_memoria_destino] = self.xp >> 8
		self.memoria[posicion_memoria_destino+1] = self.xp & 0xFF

#Opcode 0xA7: Mueve el contenido de una posición de memoria a XP. Sólo recibe como parámetro
#la posición de memoria de origen. Tomar en cuenta nuevamente que XP es de 16 bits, por lo 
#tanto se utilizaran la posición de memoria como parámetro y la siguiente para rellenar XP.
	def__ejecutar_mov7(self, posicion_memoria_origen):
		xp = self.memoria[posicion_memoria_origen] >> 8
		xp = self.memoria[posicion_memoria_origen+1] & 0xFF



#JMP




 	def ejecutar(self):
        while True:
            opcode = self.memoria[self.IP]
            if opcode == '0xF1': #Es un HLT (operacion de sistema de terminacion)
                break          #Termina el bucle y la ejecucion del programa
            elif opcode == '0xA0':
				self.def__ejecutar_mov0(self, constante, posicion_memoria)
			elif opcode == '0xA1':
				self.def__ejecutar_mov1(self, posicion_memoria)
			elif opcode == '0xA2':
				self.def__ejecutar_mov2(self, posicion_memoria)
			elif opcode == '0xA3':
				self.def__ejecutar_mov3(self, posicion_memoria_origen, posicion_memoria_destino)
			elif opcode == '0xA4':
				self.def__ejecutar_mov4(self, posicion_memoria_origen)
			elif opcode == '0xA5':
				self.def__ejecutar_mov5(self, posicion_memoria_destino)
			elif opcode == '0xA6':
				self.def__ejecutar_mov6(self, posicion_memoria_destino)
			elif opcode == '0xA7':
				self.def__ejecutar_mov7(self, posicion_memoria_origen)
#----------------listo---------------------


    		elif opcode == '0xB0': #Es un JMP
    			self.ejecutar_jmp0(opcode)
    		elif opcode == '0xB1': #Es un JMP
    			self.ejecutar_jmp1(opcode)

   			elif opcode == '0xC0': #Es una operacion logica
    			self.ejecutar_logica0(opcode)
    		elif opcode == '0xC1': #Es una operacion logica
    			self.ejecutar_logica1(opcode)
    		elif opcode == '0xC2': #Es una operacion logica
    			self.ejecutar_logica2(opcode)
    		elif opcode == '0xC3': #Es una operacion logica
    			self.ejecutar_logica3(opcode)

    		elif opcode == '0xD0': #Es una operacion aritmetica
    			self.ejecutar_aritmetica0(opcode)
    		elif opcode == '0xD1': #Es una operacion aritmetica
    			self.ejecutar_aritmetica1(opcode)
    		elif opcode == '0xD2': #Es una operacion aritmetica
    			self.ejecutar_aritmetica2(opcode)

    		elif opcode == '0xF0': #Es una operacion de sistema
    			self.ejecutar_sistema0(opcode)

#Cargar archivo a partir de la direccion de memoria 100 de la maquina virtual
	#Se toma el vector memoria desde su posicion 100, cargando el archivo en direcciones
	#consecutivas hasta cargarlo por completo.
	def cargar_archivo(self, archivo):
		self.memoria[100:100+len(archivo)] = archivo



#PENDIENTE:
#Si valor supera '255' debera ser cortado (mas de 8 bits) Bytes mas/menos significativo
#Desarrollar las diferentes variaciones de las funciones realizadas alla arriba


