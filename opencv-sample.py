import cv2

# Cargar el archivo de video
video = cv2.VideoCapture("video.mp4")

# Contador de frames
frame_count = 0

# Bucle principal del video
while True:
    # Leer el siguiente frame del video
    success, frame = video.read()

    # Si se llegó al final del video, salir del bucle
    if not success:
        break

    # Incrementar el contador de frames
    frame_count += 1

    # Si el frame actual es un frame que queremos procesar, procesarlo
    if frame_count % 30 == 0:
        # Convertir el frame a escala de grises
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar objetos en el frame
        objects = detect_objects(gray_frame)

        # Dibujar un rectángulo alrededor de cada objeto detectado
        for obj in objects:
            x, y, w, h = obj
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Mostrar el frame procesado en una ventana
        cv2.imshow("Frame", frame)

# Cerrar el video
video.release()
