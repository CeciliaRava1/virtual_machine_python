# Maquina Virtual

## Overview

This repository contains the implementation of a virtual machine (`MaquinaVirtual`) that simulates basic operations on memory using various opcodes. The virtual machine has a memory space of 65536 addresses and uses two registers: `XP` and `IP`.

## Features

- Memory manipulation with `MOV` operations.
- Conditional and unconditional jumps with `JMP` operations.
- Logical operations: `NOT`, `AND`, `OR`, `XOR`.
- Arithmetic operations: `ADD`, `SUB`, `MOD`.
- Support for loading binary files into memory.

## Class: `MaquinaVirtual`

### Attributes

- `memoria`: A list representing the memory space, initialized to 65536 addresses.
- `xp`: An integer representing the `XP` register, initialized to 1025.
- `ip`: An integer representing the `IP` register, initialized to 100.

### Methods

#### Memory Manipulation

- `Opcode_0xA0(direccion_memoria, valor)`: Moves a constant value to a specific memory address.
- `Opcode_0xA1(direccion_memoria_inicial)`: Moves the content of the `IP` register to a specific memory address.
- `Opcode_0xA2(direccion_memoria_inicial)`: Moves the content of a specific memory address to the `IP` register.
- `Opcode_0xA3(direccion_memoria_origen, direccion_memoria_destino)`: Moves values between memory addresses.
- `Opcode_0xA4(direccion_memoria)`: Moves the value from a memory address to the address contained in `XP`.
- `Opcode_0xA5(direccion_memoria)`: Moves the value from the address contained in `XP` to another memory address.
- `Opcode_0xA6(direccion_memoria)`: Moves the content of `XP` to a memory address.
- `Opcode_0xA7(direccion_memoria)`: Moves the content of a memory address to `XP`.

#### Jump Operations

- `Opcode_0xB0(direccion_memoria_destino, direccion_memoria_condicion)`: Conditional jump to a memory address if the content of another address is 0.
- `Opcode_0xB1(posicion_memoria)`: Unconditional jump to a memory address.

#### Logical Operations

- `Opcode_0xC0(posicion_memoria)`: Logical NOT on a memory address.
- `Opcode_0xC1(posicion_memoria, posicion_memoria_2)`: Logical AND between two memory addresses.
- `Opcode_0xC2(posicion_memoria, posicion_memoria_2)`: Logical OR between two memory addresses.
- `Opcode_0xC3(posicion_memoria, posicion_memoria_2)`: Logical XOR between two memory addresses.

#### Arithmetic Operations

- `Opcode_0xD0(posicion_memoria, posicion_memoria_2)`: Adds the content of two memory addresses.
- `Opcode_0xD1(posicion_memoria, posicion_memoria_2)`: Subtracts the content of two memory addresses.
- `Opcode_0xD2(posicion_memoria, posicion_memoria_2)`: Calculates the modulo of the content of two memory addresses.

#### Additional Methods

- `cargar_archivo(archivo)`: Loads a binary file into memory starting at address 100.
- `getPosicionMemoria(ip)`: Gets a 16-bit memory address from two consecutive memory positions.
- `ejecutar()`: Executes the instructions in memory until a termination opcode is encountered.

## Usage

To use the virtual machine, instantiate the `MaquinaVirtual` class and call the `cargar_archivo` method to load your binary file. Then call the `ejecutar` method to start the execution.

```python
# Example usage
vm = MaquinaVirtual()
vm.cargar_archivo([0xA0, 0x00, 0x01, 0x05, 0xF1])
vm.ejecutar()
