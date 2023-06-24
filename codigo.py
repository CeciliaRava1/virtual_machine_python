# 24/06 Maquina virtual

#Usamos una clase para definir la maquina virtual
class maquina_virtual:
	#Definimos los atributos (caracteristicas) de la MV
	def__init__(self):
		self.memoria = [0] * 65536 #Vector que representa la memoria 0 a 65535
        self.XP = 0                #Variable entera que representa registro XP
        self.IP = 100			   #Variable entera que representa registro IP

#Cargar en memoria de MV programa binario
    #Definir metodo para abrir archivo y se carga
    def__ejecutar(self, archivo):
    	self.cargar_archivo(archivo)

#Carga programa en registro IP, en sus posiciones
    #Se crea un bucle para que el registro IP vaya cargando los datos contenidos en el
    #archivo binario cargado. Mientras que la posicion del registro IP sea menor a la
    #longitud del archivo binario, seguira leyendo y almacenando estos datos en el 
    #registro IP, aumentando su posicion en 1 en cada pasaje por el ciclo.
    while self.ip < len(archivo): 
    	opcode = archivo[self.ip]
    	self.ip += 1

#Comprobar a que tipo de operacion (MOV, JMP, etc) hace referencia el opcode
	#'>>' desplaza el valor del opcode hacia la derecha 4 posiciones, para aislar los 
	#primeros 4 bits, lo que permite compararlos con el opcode correspondiente a la funcion
	#Ejemplo: si fuera el opcode '0xA2' se tomaria solo '0xA' ignorando el '2'

 	def ejecutar(self):
        while True:
            opcode = self.memoria[self.IP]
            if opcode == 0xF1: #Es un HLT (operacion de sistema de terminacion)
                break          #Termina el bucle y la ejecucion del programa
			elif opcode >> 4 == 0xA:   #Es un MOV
    			self.ejecutar_mov(opcode)
    		elif opcode >> 4 == 0xB: #Es un JMP
    			self.ejecutar_jmp(opcode)
   			elif opcode >> 4 == 0xC: #Es una operacion logica
    			self.ejecutar_logica(opcode)
    		elif opcode >> 4 == 0xD: #Es una operacion aritmetica
    			self.ejecutar_aritmetica(opcode)
    		elif opcode >> 4 == 0xF: #Es una operacion de sistema
    			self.ejecutar_sistema(opcode)

#Cargar archivo a partir de la direccion de memoria 100 de la maquina virtual
	#Se toma el vector memoria desde su posicion 100, cargando el archivo en direcciones
	#consecutivas hasta cargarlo por completo.
	def cargar_archivo(self, archivo):
		self.memoria[100:100+len(archivo)] = archivo



#PENDIENTE:
#Si valor supera '255' debera ser cortado (mas de 8 bits) Bytes mas/menos significativo
#Desarrollar las diferentes variaciones de las funciones realizadas alla arriba


