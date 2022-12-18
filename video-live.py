import cv2

# Abrir la cámara para la videoconferencia
camera = cv2.VideoCapture(0)

# Bucle principal de la videoconferencia
while True:
    # Leer el siguiente frame de la cámara
    success, frame = camera.read()

    # Si se llegó al final del video, salir del bucle
    if not success:
        break

    # Procesar el frame para detectar las señas
    detected_signs = process_frame(frame)

    # Si se detectaron señas, buscar su traducción y mostrarla en la aplicación
    if detected_signs:
        for sign in detected_signs:
            translation = lookup_sign_translation(sign)
            show_translation(translation)

# Cerrar la cámara
camera.release()
