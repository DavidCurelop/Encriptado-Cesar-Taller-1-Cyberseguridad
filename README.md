# Encriptado César - Taller 1 Ciberseguridad

Este repositorio contiene la implementación del algoritmo de cifrado y descifrado por sustitución **Cifrado César** en Python, junto con la evidencia completa de las pruebas unitarias realizadas.

---

## Archivos del Proyecto

- [`cesar.py`](cesar.py): Contiene las funciones principales:
  - `cifrar(clave, texto)`: Cifra una cadena de texto desplazando las letras según la `clave` especificada. Preserva mayúsculas, minúsculas y caracteres no alfabéticos.
  - `descifrar(clave, texto)`: Descifra el texto utilizando la clave correspondiente.
- [`Tests.py`](Tests.py): Conjunto de pruebas unitarias con reporte detallado de evidencia.

---

## Evidencia de Pruebas Realizadas

A continuación se presenta la evidencia individual para cada caso de prueba verificado en el sistema:

### Tabla Resumen de Pruebas

| ID | Nombre de la Prueba | Texto Original (Input) | Clave ($k$) | Texto Cifrado | Texto Descifrado | Estado |
| :---: | :--- | :--- | :---: | :--- | :--- | :---: |
| **Test 1** | Desplazamiento Básico | `"abc"` | `3` | `"def"` | `"abc"` | PASSED |
| **Test 2** | Desbordamiento del Alfabeto (Wrap-Around) | `"xyz"` | `5` | `"cde"` | `"xyz"` | PASSED |
| **Test 3** | Preservación de Mayúsculas y Minúsculas | `"Hello World"` | `3` | `"Khoor Zruog"` | `"Hello World"` | PASSED |
| **Test 4** | Caracteres Especiales y Números | `"python 3.10 is great, right?!"` | `7` | `"wfaovu 3.10 pz nylha, ypnoa?!"` | `"python 3.10 is great, right?!"` | PASSED |
| **Test 5** | Clave Grande ($k \ge 26$) | `"hello"` | `27` | `"ifmmp"` | `"hello"` | PASSED |

---

### Detalles de Cada Caso de Prueba

1. **Test 1: Desplazamiento Básico**
   - **Propósito**: Verificación del desplazamiento simple de caracteres dentro del rango alfabético sin desbordamiento.
   - **Entrada**: `"abc"` con clave $k = 3$.
   - **Resultado Cifrado**: `"def"`
   - **Resultado Descifrado**: `"abc"`

2. **Test 2: Desbordamiento del Alfabeto (Wrap-Around)**
   - **Propósito**: Validar que al llegar al final del alfabeto ('z'), la rotación continúe desde el inicio ('a').
   - **Entrada**: `"xyz"` con clave $k = 5$.
   - **Resultado Cifrado**: `"cde"`
   - **Resultado Descifrado**: `"xyz"`

3. **Test 3: Preservación de Mayúsculas y Minúsculas**
   - **Propósito**: Garantizar que las letras mayúsculas se cifren como mayúsculas y las minúsculas como minúsculas.
   - **Entrada**: `"Hello World"` con clave $k = 3$.
   - **Resultado Cifrado**: `"Khoor Zruog"`
   - **Resultado Descifrado**: `"Hello World"`

4. **Test 4: Caracteres Especiales y Números (No Alfabéticos)**
   - **Propósito**: Verificar que espacios, números y signos de puntuación se mantengan intactos sin sufrir alteraciones.
   - **Entrada**: `"python 3.10 is great, right?!"` con clave $k = 7$.
   - **Resultado Cifrado**: `"wfaovu 3.10 pz nylha, ypnoa?!"`
   - **Resultado Descifrado**: `"python 3.10 is great, right?!"`

5. **Test 5: Clave Grande ($k \ge 26$)**
   - **Propósito**: Probar el manejo de claves mayores al tamaño del alfabeto ($26$) aplicando la operación módulo ($27 \pmod{26} = 1$).
   - **Entrada**: `"hello"` con clave $k = 27$.
   - **Resultado Cifrado**: `"ifmmp"`
   - **Resultado Descifrado**: `"hello"`

---

## Salida de Consola (Log de Ejecución)

Al ejecutar la suite de pruebas mediante el comando `python Tests.py`, se genera el siguiente reporte en terminal:

```text
==================================================
       EVIDENCIA DE EJECUCIÓN DE PRUEBAS          
==================================================

[PASSED] Test 1: Desplazamiento Básico
         Entrada: 'abc' | Clave: 3
         Cifrado: 'def' | Descifrado: 'abc'

[PASSED] Test 2: Desbordamiento del Alfabeto (Wrap-Around)
         Entrada: 'xyz' | Clave: 5
         Cifrado: 'cde' | Descifrado: 'xyz'

[PASSED] Test 3: Preservación de Mayúsculas y Minúsculas
         Entrada: 'Hello World' | Clave: 3
         Cifrado: 'Khoor Zruog' | Descifrado: 'Hello World'

[PASSED] Test 4: Caracteres Especiales y Números (No Alfabéticos)
         Entrada: 'python 3.10 is great, right?!' | Clave: 7
         Cifrado: 'wfaovu 3.10 pz nylha, ypnoa?!' | Descifrado: 'python 3.10 is great, right?!'

[PASSED] Test 5: Clave Grande (Módulo 26)
         Entrada: 'hello' | Clave: 27
         Cifrado: 'ifmmp' | Descifrado: 'hello'

==================================================
  ¡TODAS LAS PRUEBAS SE EJECUTARON CON ÉXITO!     
==================================================
```
