# Teclado Virtual de Detección de Gestos

Este proyecto utiliza OpenCV y MediaPipe para crear un teclado virtual que detecta gestos realizados con las manos y los traduce a texto. El texto detectado se guarda en un archivo de texto y se muestra en tiempo real en la pantalla.

## Características principales
- Detección de gestos de manos utilizando MediaPipe.
- Traducción de combinaciones de dedos levantados en ambas manos a letras específicas.
- Visualización en tiempo real de los gestos detectados.
- Almacenamiento del texto detectado en un archivo de texto.

## Requisitos
- Python 3.7 o superior
- Cámara web

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/teclado-virtual-gestos.git
   cd teclado-virtual-gestos
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
Ejecuta el script principal:
```bash
python teclado_virtual.py
```

Presiona `ESC` para salir de la aplicación.

## Biblioteca utilizada
| Biblioteca  | Versión | Descripción                                        |
|-------------|---------|----------------------------------------------------|
| OpenCV      | 4.x     | Para capturar imágenes desde la cámara y procesarlas. |
| MediaPipe   | Última  | Para la detección y seguimiento de manos.         |
| Time        | Nativa  | Para controlar los intervalos entre detecciones.  |

## Mapeo de gestos
El proyecto utiliza combinaciones de dedos levantados en ambas manos para representar letras. Estas combinaciones están definidas en el diccionario `gestures` del código. Por ejemplo:

| Dedos mano izquierda | Dedos mano derecha | Letra |
|-----------------------|--------------------|-------|
| 1                     | 0                  | A     |
| 2                     | 0                  | B     |
| 0                     | 1                  | E     |
| ...                   | ...                | ...   |

Para más detalles, consulta el archivo fuente `teclado_virtual.py`.

## Notas
- El script está configurado para un intervalo de 3 segundos entre detecciones del mismo gesto.
- El texto final se guarda en un archivo llamado `detected_text.txt` en el mismo directorio.

## Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, no dudes en enviar un pull request o abrir un issue.

---
¡Gracias por usar este proyecto! 😊
