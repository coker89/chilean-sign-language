import cv2

# Abrir el video
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

    # Si el frame actual es un frame que contiene una seña, guardar la imagen
    if frame_count % 30 == 0:
        cv2.imwrite("frame_{}.jpg".format(frame_count), frame)

# Cerrar el video
video.release()
