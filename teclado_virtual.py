import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Diccionario de gestos y letras asignadas para las combinaciones de dos manos
gestures = {
    (1, 0): "A",   # Mano izquierda 1 dedo levantado, Mano derecha 0 dedos levantados
    (2, 0): "B",   # Mano izquierda 2 dedos levantados, Mano derecha 0 dedos levantados
    (3, 0): "C",   # Mano izquierda 3 dedos levantados, Mano derecha 0 dedos levantados
    (4, 0): "D",   # Mano izquierda 4 dedos levantados, Mano derecha 0 dedos levantados
    (0, 1): "E",   # Mano izquierda 0 dedos levantados, Mano derecha 1 dedos levantados
    (0, 2): "F",   # Mano izquierda 0 dedos levantados, Mano derecha 2 dedos levantados
    (0, 3): "G",   # Mano izquierda 0 dedos levantados, Mano derecha 3 dedos levantados
    (0, 4): "H",   # Mano izquierda 0 dedos levantados, Mano derecha 0 dedos levantados
    (1, 1): "I",   # Mano izquierda 1 dedos levantados, Mano derecha 1 dedos levantados
    (1, 2): "J",   # Mano izquierda 1 dedos levantados, Mano derecha 2 dedos levantados
    (1, 3): "K",   # Mano izquierda 1 dedos levantados, Mano derecha 3 dedos levantados
    (1, 4): "L",   # Mano izquierda 1 dedos levantados, Mano derecha 4 dedos levantados
    (2, 1): "M",   # Mano izquierda 2 dedos levantados, Mano derecha 1 dedos levantados
    (2, 2): "N",   # Mano izquierda 2 dedos levantados, Mano derecha 2 dedos levantados
    (2, 3): "O",   # Mano izquierda 2 dedos levantados, Mano derecha 3 dedos levantados
    (2, 4): "P",   # Mano izquierda 2 dedos levantados, Mano derecha 4 dedos levantados
    (3, 1): "Q",   # Mano izquierda 3 dedos levantados, Mano derecha 1 dedos levantados
    (3, 2): "R",   # Mano izquierda 3 dedos levantados, Mano derecha 2 dedos levantados
    (3, 3): "S",   # Mano izquierda 3 dedos levantados, Mano derecha 3 dedos levantados
    (3, 4): "T",   # Mano izquierda 3 dedos levantados, Mano derecha 4 dedos levantados
    (4, 1): "U",   # Mano izquierda 4 dedos levantados, Mano derecha 1 dedos levantados
    (4, 2): "V",   # Mano izquierda 4 dedos levantados, Mano derecha 2 dedos levantados
    (4, 3): "W",   # Mano izquierda 4 dedos levantados, Mano derecha 3 dedos levantados
    (4, 4): "X",   # Mano izquierda 4 dedos levantados, Mano derecha 4 dedos levantados
    (0, 0): "Y",   # Mano izquierda 0 dedos levantados, Mano derecha 0 dedos levantados
    (5, 0): "Z",   # Mano izquierda 5 dedos levantados, Mano derecha 0 dedos levantados
}

detected_text = ""
detected_in_real_time = ""

# Abrir archivo para guardar el texto
with open("detected_text.txt", "w") as file:
    file.write("Texto detectado:\n")

cap = cv2.VideoCapture(0)
last_detection_time = time.time()  # Temporizador para controlar el intervalo de 3 segundos

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    left_hand_fingers_up = None
    right_hand_fingers_up = None

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Identificar cuál es la mano izquierda y cuál es la derecha
            is_left = handedness.classification[0].label == 'Left'

            # Calcular número de dedos levantados para cada mano
            landmarks = hand_landmarks.landmark
            fingers_up = sum(landmarks[i].y < landmarks[i - 2].y for i in [8, 12, 16, 20])  # Dedos levantados

            # Asignar la cantidad de dedos levantados a la mano izquierda o derecha
            if is_left:
                left_hand_fingers_up = fingers_up
            else:
                right_hand_fingers_up = fingers_up

            # Dibujar los landmarks de la mano
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Verificar si ambas manos están detectadas y si tienen el número correcto de dedos levantados
        if left_hand_fingers_up is not None and right_hand_fingers_up is not None:
            gesture = (left_hand_fingers_up, right_hand_fingers_up)
            if gesture in gestures:
                # Comprobar si han pasado 3 segundos desde la última detección
                current_time = time.time()
                if current_time - last_detection_time >= 3:
                    detected_text += gestures[gesture]  # Agregar la letra correspondiente
                    # Guardar el texto en el archivo
                    with open("detected_text.txt", "a") as file:
                        file.write(gestures[gesture])
                    # Actualizar el temporizador
                    last_detection_time = current_time

                # Actualizar texto en tiempo real
                detected_in_real_time = gestures[gesture]

    # Crear un fondo blanco para el texto detectado en tiempo real
    cv2.rectangle(image, (10, 10), (600, 60), (255, 255, 255), -1)
    # Mostrar el gesto detectado en la pantalla (texto en tiempo real)
    cv2.putText(image, f"Detectado en tiempo real: {detected_in_real_time}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, lineType=cv2.LINE_AA)

    # Crear un fondo blanco para el texto final
    cv2.rectangle(image, (10, 70), (600, 120), (255, 255, 255), -1)
    # Mostrar el texto completo (texto final)
    cv2.putText(image, f"Texto: {detected_text}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, lineType=cv2.LINE_AA)

    # Mostrar la imagen
    cv2.imshow("Teclado Virtual", image)

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows() 