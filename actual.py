class MaquinaVirtual:
  # Declaracion atributos MV - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  def __init__(self):
			self.memoria = [0] * 65536  # Vector que representa la memoria desde direccion 0 a 65535
			self.xp = 1025              # Variable entera que representa registro XP
			self.ip = 100			          # Variable entera que representa registro IP

  # Declaracion de metodos para las operaciones - - - - - - - - - - - - - - - - - - - - - - - -
  # Operacion MOV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  # Opcode 0xA0: Mueve una constante a una posición de memoria. Recibe dos parámetros,
  # primero la dirección de memoria y luego el valor.
  def Opcode_0xA0(self, direccion_memoria, valor):
    print('Opcode_0xA0')
    self.memoria[direccion_memoria] = valor

  # Opcode 0xA1: Mueve el contenido del registro IP a una posición de memoria. Recibe como
  # parámetro la posición de memoria inicial. Tome en cuenta que los registros son de 16
  # bits, con lo cual almacenará los primeros 8 en la dirección recibida como parámetro y
  # los restantes en la posición de memoria siguiente.
  def Opcode_0xA1(self, direccion_memoria_inicial):
    print('Opcode_0xA1')
    valor = self.memoria[self.ip]
    print('valor ',valor)
    self.memoria[direccion_memoria_inicial] = valor

  # Opcode 0xA2: Mueve el contenido de una posición de memoria al registro IP. Recibe como
  # parámetro la posición de memoria inicial. Tome en cuenta que los registros son de 16 bits,
  # con lo cual obtendrá los primeros 8 en la dirección recibida como parámetro y los restantes
  # en la posición de memoria siguiente.
  def Opcode_0xA2(self, direccion_memoria_inicial):
    print('Opcode_0xA2')
    valor = self.memoria[direccion_memoria_inicial]
    print('valor ',valor)
    self.memoria[self.ip] = valor

  # Opcode 0xA3: Mueve valores entre posiciones de memoria. Recibe dos parámetros, el primero es
  # la posición de memoria de origen, y el segundo es la posición de memoria de destino.
  def Opcode_0xA3(self, direccion_memoria_origen, direccion_memoria_destino):
    print('Opcode_0xA3')
    valor = self.memoria[direccion_memoria_origen]
    print('valor ',valor)
    self.memoria[direccion_memoria_destino] = valor

  # Opcode 0xA4: Mueve el valor desde una posición de memoria, a la posición de memoria que
  # contiene XP. Es decir, si XP contiene D1FA el valor se moverá a esa dirección de memoria.
  # Recibe sólo un parámetro, la posición de memoria de origen, ya que el destino se encuentra
  # en XP.
  def Opcode_0xA4(self, direccion_memoria):
    print('Opcode_0xA4')
    print('XP ', self.xp)
    valor = self.memoria[direccion_memoria]
    print('valor ',valor)
    self.memoria[self.xp] = valor

  # Opcode 0xA5: Mueve el valor desde la posición de memoria que contiene XP, a otra posición de
  # memoria. Es decir, si XP contiene el D1FA el valor se moverá desde esa dirección de memoria
  # a otra que se recibe como parámetro. Recibe sólo un parámetro, la posición de memoria de
  # destino, ya que el origen se encuentra en XP.
  def Opcode_0xA5(self, direccion_memoria):
    print('Opcode_0xA5')
    print('XP ', self.xp)
    valor = self.memoria[self.xp]
    print('valor ',valor)
    self.memoria[direccion_memoria] = valor

  # Opcode 0xA6: Mueve el contenido de XP a una posición de memoria. En este caso si se mueve
  # el contenido de XP, es decir, si XP contiene D1FA, D1 se movera a la posición de memoria
  # recibida como parámetro y FA a la posición siguiente. Recibe sólo un parámetro, que es la
  # posición de memoria de destino.
  def Opcode_0xA6(self, direccion_memoria):
    print('Opcode_0xA6')
    print('XP ', self.xp)
    parte1 = (self.xp >> 8) & 0xFF
    parte2 = self.xp & 0xFF
    print('parte 1 %d, parte 2 %d'% (parte1, parte2))
    self.memoria[direccion_memoria] = parte1
    self.memoria[direccion_memoria+1] = parte2

  # Opcode 0xA7: Mueve el contenido de una posición de memoria a XP. Sólo recibe como parámetro
  # la posición de memoria de origen. Tomar en cuenta nuevamente que XP es de 16 bits, por lo
  # tanto se utilizaran la posición de memoria como parámetro y la siguiente para rellenar XP.
  def Opcode_0xA7(self, direccion_memoria):
    print('Opcode_0xA7')
    self.xp = (self.memoria[direccion_memoria] << 8) | self.memoria[direccion_memoria+1]
    print('XP ', self.xp)

  # Operacion JMP  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  # Opcode 0xB0: Salto condicional. Recibe dos parámetros, el primero es la dirección a saltar, 
  # si posición de memoria apuntada por el segundo parametro contiene 0. Es decir, si el segundo 
  # parametro es D1F4 y en esa posición de memoria contiene un 0, se salta a la dirección que 
  # ofrece el primer parámetro, de lo contrario se continua con ejecución en instrucción que sigue.
  def Opcode_0xB0(self, direccion_memoria_destino, direccion_memoria_condicion):
    print('Opcode_0xB0')
    if (self.memoria[direccion_memoria_condicion] == 0x00):
      self.xp = direccion_memoria_destino

  #Opcode 0xB1: Salto obligado. Recibe como parámetro la dirección de salto, y salta siempre.
  def Opcode_0xB1(self, posicion_memoria):
    print('Opcode_0xB1')
    self.xp = self.memoria[posicion_memoria]

  # Operaciones logicas - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # Opcode 0xC0: Operación lógica NOT, es la única que recibe sólo 1 parámetro que es la posición
  # de memoria a operar. Ejemplo si se recibe D1F4, dicha posición de memoria se aplica un NOT 
  # binario,es decir si contiene 10001010 quedará almacenado 01110101.
  def Opcode_0xC0(self, posicion_memoria): #NOT
    print('Opcode_0xC0')
    ~self.memoria[posicion_memoria]

  # Opcode 0xC1: AND entre las posiciones de memoria recibidas como parámetro.
  def Opcode_0xC1(self, posicion_memoria,posicion_memoria_2): #AND
    print('Opcode_0xC1')
    self.memoria[posicion_memoria_2] &= self.memoria[posicion_memoria]

  # Opcode 0xC2: OR entre las posiciones de memoria recibidas como parámetro.
  def Opcode_0xC2(self, posicion_memoria,posicion_memoria_2): #OR
    print('Opcode_0xC2')
    self.memoria[posicion_memoria_2] |= self.memoria[posicion_memoria]

  # Opcode 0xC3: XOR entre las posiciones de memoria recibidas como parámetro.
  def Opcode_0xC3(self, posicion_memoria,posicion_memoria_2): #XOR
    print('Opcode_0xC3')
    self.memoria[posicion_memoria_2] ^= self.memoria[posicion_memoria]

  # Operaciones aritmeticas - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # Opcode 0xD0: ADD, suma el contenido de las posiciones de memoria recibidos como parámetros.
  def Opcode_0xD0(self, posicion_memoria,posicion_memoria_2):
    print('Opcode_0xD0')
    self.memoria[posicion_memoria_2] += self.memoria[posicion_memoria]

  # Opcode 0xD1: SUB, suma el contenido de las posiciones de memoria recibidos como parámetros.
  # El primer parámetro es el minuendo y el segundo el sustraendo.
  def Opcode_0xD1(self, posicion_memoria,posicion_memoria_2):
    print('Opcode_0xD1')
    self.memoria[posicion_memoria_2] -= self.memoria[posicion_memoria]

  # Opcode 0xD2: MOD, calcula el módulo del contenido de las posiciones de memoria recibidos.
  # El primer parámetro es el divisor y el segundo el dividendo.
  def Opcode_0xD2(self, posicion_memoria,posicion_memoria_2):
    print('Opcode_0xD2')
    result = self.memoria[posicion_memoria_2] % self.memoria[posicion_memoria]
    self.memoria[posicion_memoria_2] = result

  # Declaracion de metodo para cargar archivo binario  - - - - - - - - - - - - - - - - - - - - - 
  def cargar_archivo(self, archivo):
	  self.memoria[100:100+len(archivo)] = archivo

  # Declaracion de metodo para obtener posicion de memoria  - - - - - - - - - - - - - - - - - - -
  def getPosicionMemoria(self, ip):
    #obtengo los primeros y segundos 8 bit de memoria
    valorMemoria1 = self.memoria[ip+1]
    valorMemoria2 = self.memoria[ip+2]
    #uno y obtengo la posicion de memoria de 16bit
    posicion_memoria = (valorMemoria1 << 8) | valorMemoria2
    return posicion_memoria

  # Delaracion del metodo para lograr ejecucion de la MV  - - - - - - - - - - - - - - - - - - - - -
  def ejecutar(self):
    while True:
      print('IP ',self.ip)
      print('XP ',self.xp)
      opcode = self.memoria[self.ip]
      print(hex(opcode))

      if opcode == 0xF1 : #Es un HLT (operacion de sistema de terminacion)
        print('FINAL')
        break #Termina el bucle y la ejecucion del programa

      elif opcode == 0xA0: #160
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)
        constante = self.memoria[self.ip+3]
        print('constante ',constante)
        self.Opcode_0xA0(posicion_memoria, constante)
        #seteo Ip como proxima instruccion
        self.ip += 4 #proxima direccion

      elif opcode == 0xA1: #161
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)
        self.Opcode_0xA1(posicion_memoria)
        #seteo Ip como proxima instruccion
        self.ip += 3 #proxima direccion

      elif opcode == 0xA2: #162
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)

        self.Opcode_0xA2(posicion_memoria)
        #seteo Ip como proxima instruccion
        self.ip += 3 #proxima direccion

      elif opcode == 0xA3:
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria_origen = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria_origen
        print('posicion origen ',posicion_memoria_origen)

        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria_destino = self.getPosicionMemoria(self.ip+2)
        #self.xp = posicion_memoria_destino
        print('posicion destino ',posicion_memoria_destino)

        self.Opcode_0xA3(posicion_memoria_origen, posicion_memoria_destino)
        #seteo Ip como proxima instruccion
        self.ip += 5 #proxima direccion

      elif opcode == 0xA4:
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria_origen = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria_origen
        print('posicion origen ',posicion_memoria_origen)

        self.Opcode_0xA4(posicion_memoria_origen)
        #seteo Ip como proxima instruccion
        self.ip += 3 #proxima direccion

      elif opcode == 0xA5:
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria_destino = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria_destino
        print('posicion origen ',posicion_memoria_destino)

        self.Opcode_0xA5(posicion_memoria_destino)
        #seteo Ip como proxima instruccion
        self.ip += 3 #proxima direccion

      elif opcode == 0xA6:
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria_destino = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria_destino
        print('posicion origen ',posicion_memoria_destino)

        self.Opcode_0xA6(posicion_memoria_destino)
        #seteo Ip como proxima instruccion
        self.ip += 3 #proxima direccion

      elif opcode == 0xA7: #167
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria_origen = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria_origen
        print('posicion origen ',posicion_memoria_origen)

        self.Opcode_0xA7(posicion_memoria_origen)
        #seteo Ip como proxima instruccion
        self.ip += 3 #proxima direccion


      elif opcode == 0xB0: #Es un JMP 176
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria_saltar = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria_saltar
        print('posicion ',posicion_memoria_saltar)

        posicion_memoria_condicion = self.getPosicionMemoria(self.ip+2)
        #self.xp = posicion_memoria_condicion
        print('posicion ',posicion_memoria_condicion)

        self.Opcode_0xB0(posicion_memoria_saltar, posicion_memoria_condicion)
        #seteo Ip como proxima instruccion
        self.ip += 5 #proxima direccion

      elif opcode == 0xB1: #Es un JMP 177
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
				#self.xp = posicion_memoria
        print('posicion ',posicion_memoria)

        self.Opcode_0xB1(posicion_memoria)

        #seteo Ip como proxima instruccion
        self.ip += 3 #proxima direccion


      elif opcode == 0xC0: #Es una operacion logica 	NOT
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)

        self.Opcode_0xC0(posicion_memoria)

        #seteo Ip como proxima instruccion
        self.ip += 3 #proxima direccion

      elif opcode == 0xC1: #Es una operacion logica		AND
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)

        posicion_memoria_2 = self.getPosicionMemoria(self.ip+2)
        #self.xp = posicion_memoria_2
        print('posicion ',posicion_memoria_2)

        self.Opcode_0xC1(posicion_memoria, posicion_memoria_2)

        #seteo Ip como proxima instruccion
        self.ip += 5 #proxima direccion


      elif opcode == 0xC2: #Es una operacion logica		OR
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)

        posicion_memoria_2 = self.getPosicionMemoria(self.ip+2)
        #self.xp = posicion_memoria_2
        print('posicion ',posicion_memoria_2)

        self.Opcode_0xC2(posicion_memoria, posicion_memoria_2)

        #seteo Ip como proxima instruccion
        self.ip += 5 #proxima direccion


      elif opcode == 0xC3: #Es una operacion logica		XOR
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)

        posicion_memoria_2 = self.getPosicionMemoria(self.ip+2)
        #self.xp = posicion_memoria_2
        print('posicion ',posicion_memoria_2)

        self.Opcode_0xC3(posicion_memoria, posicion_memoria_2)

        #seteo Ip como proxima instruccion
        self.ip += 5 #proxima direccion


      elif opcode == 0xD0: #Es una operacion aritmetica
        #obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)

        posicion_memoria_2 = self.getPosicionMemoria(self.ip+2)#self.xp = posicion_memoria
        #self.xp = posicion_memoria_2
        print('posicion ',posicion_memoria_2)

        self.Opcode_0xD0(posicion_memoria, posicion_memoria_2)

        #seteo Ip como proxima instruccion
        self.ip += 5 #proxima direccion


      elif opcode == 0xD1: #Es una operacion aritmetica
				#obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)

        posicion_memoria_2 = self.getPosicionMemoria(self.ip+2)
        #self.xp = posicion_memoria_2
        print('posicion ',posicion_memoria_2)

        self.Opcode_0xD1(posicion_memoria, posicion_memoria_2)

        #seteo Ip como proxima instruccion
        self.ip += 5 #proxima direccion

      elif opcode == 0xD2: #Es una operacion aritmetica
				#obtengo la posicion de memoria mandando la posicion de ip
        posicion_memoria = self.getPosicionMemoria(self.ip)
        #self.xp = posicion_memoria
        print('posicion ',posicion_memoria)

        posicion_memoria_2 = self.getPosicionMemoria(self.ip+2)
        #self.xp = posicion_memoria_2
        print('posicion ',posicion_memoria_2)

        self.Opcode_0xD2(posicion_memoria, posicion_memoria_2)

        #seteo Ip como proxima instruccion
        self.ip += 5 #proxima direccion

      elif opcode == 0xF0: #Es una operacion de sistema
        print('DUMP MEMORIA')
        self.ejecutar_sistema0() # descarga a memoria
        self.ip +=1
      else:
        print('ERROR NO SE RECONOCE EL OPCODE VALUADO EN %s' %  (opcode) )
        break

  def ejecutar_sistema0(self):
    file_path = 'dump_mem.txt'
    #memory_dump = " \n ".join([str(hex(memory_byte)) for memory_byte in vm.memoria])
    memory_dump = " \n ".join([str(memory_byte) for memory_byte in vm.memoria])
    self.write_text_file(file_path, memory_dump)

  def read_binary_file(self, file_path):
    """Lee un archivo binario y devuelve su contenido como una lista de bytes."""
    try:
      with open(file_path, 'rb') as file:
        data = file.read()
        print(data)
        return list(data)
    except IOError:
      print("Error al leer el archivo binario.")
      return None

  def write_text_file(self, file_path, data):
    """Escribe el contenido de una cadena en un archivo de texto."""
    try:
      with open(file_path, 'w') as file:
        file.write(data)
    except IOError:
        print("Error al escribir el archivo.")