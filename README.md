# Encriptado César - Taller 1 Ciberseguridad

Este repositorio contiene la implementación del algoritmo de cifrado y descifrado por sustitución **Cifrado César** en Python, junto con su suite de pruebas unitarias.

## Archivos del Proyecto

- [`cesar.py`](cesar.py): Contiene las funciones principales:
  - `cifrar(clave, texto)`: Cifra una cadena de texto desplazando las letras según la `clave` especificada. Preserva mayúsculas, minúsculas y caracteres especiales.
  - `descifrar(clave, texto)`: Descifra el texto utilizando la clave correspondiente.
- [`Tests.py`](Tests.py): Conjunto de pruebas unitarias que verifican el funcionamiento correcto del cifrado y descifrado ante diferentes casos de uso.

## Ejecución de Pruebas

Para ejecutar la suite de pruebas unitarias:

```bash
python Tests.py
```

## Resultados de los Tests Ejecutados

Resultados obtenidos al ejecutar `python Tests.py`:

```text
Running Caesar Cipher Tests...
------------------------------
Test 1 Passed: Basic Shift
Test 2 Passed: Alphabet Wrap-Around
Test 3 Passed: Case Preservation
Test 4 Passed: Non-Alphabet Characters
Test 5 Passed: Large Key Modulo
------------------------------
All tests passed successfully!
```
