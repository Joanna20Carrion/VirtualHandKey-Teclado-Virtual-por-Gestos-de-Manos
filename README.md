# Teclado Virtual con Mediapipe y OpenCV

Este proyecto implementa un "teclado virtual" que utiliza la biblioteca Mediapipe para el reconocimiento de manos y OpenCV para la visualización en tiempo real. Se detectan gestos específicos basados en el número de dedos levantados en ambas manos y se asignan a letras del abecedario.

## Características

- Detecta el número de dedos levantados en cada mano.
- Asigna letras a combinaciones específicas de dedos levantados en ambas manos.
- Guarda el texto detectado en tiempo real y en un archivo `detected_text.txt`.
- Actualiza el texto detectado cada 3 segundos para evitar detecciones repetidas.
- Muestra el texto en tiempo real y el texto completo en pantalla.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.7 o superior
- OpenCV
- Mediapipe

Puedes instalarlas utilizando pip:

```bash
pip install opencv-python mediapipe
```

## Uso

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de que tu cámara esté conectada y funcionando correctamente.
3. Ejecuta el script principal:

```bash
python teclado_virtual.py
```

4. Usa tus manos frente a la cámara para formar los gestos especificados. Las letras se guardarán automáticamente en el archivo `detected_text.txt` y se mostrarán en tiempo real en la pantalla.

## Gestos Reconocidos

El programa detecta combinaciones de dedos levantados en ambas manos y las asigna a letras según el siguiente diccionario:

```python
{
    (1, 0): "A",
    (2, 0): "B",
    (3, 0): "C",
    (4, 0): "D",
    (0, 1): "E",
    (0, 2): "F",
    (0, 3): "G",
    (0, 4): "H",
    (1, 1): "I",
    (1, 2): "J",
    (1, 3): "K",
    (1, 4): "L",
    (2, 1): "M",
    (2, 2): "N",
    (2, 3): "O",
    (2, 4): "P",
    (3, 1): "Q",
    (3, 2): "R",
    (3, 3): "S",
    (3, 4): "T",
    (4, 1): "U",
    (4, 2): "V",
    (4, 3): "W",
    (4, 4): "X",
    (0, 0): "Y",
    (5, 0): "Z",
}
```

## Archivo de Salida

El texto detectado se guarda en un archivo llamado `detected_text.txt`, que se genera automáticamente al iniciar el programa. Puedes abrir este archivo para ver el texto completo detectado durante la sesión.

## Notas

- El script está diseñado para funcionar con una cámara web conectada a tu computadora.
- Asegúrate de tener buena iluminación para un mejor reconocimiento de las manos.
- Usa gestos claros y mantén las manos dentro del encuadre de la cámara.

## Controles

- Presiona `ESC` para salir del programa.

## Autor

Este proyecto fue desarrollado para explorar el reconocimiento de gestos utilizando Mediapipe y OpenCV.

