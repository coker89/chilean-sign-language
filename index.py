# Importar la librería para mostrar imágenes
import pygame

# Inicializar pygame
pygame.init()

# Definir el tamaño de la ventana
window_size = (800, 600)

# Crear la ventana
window = pygame.display.set_mode(window_size)

# Definir las señas y las imágenes correspondientes
signs = {
    "hello": "hello.jpg",
    "goodbye": "goodbye.jpg",
    "thank you": "thank_you.jpg",
    "sorry": "sorry.jpg",
    "yes": "yes.jpg",
    "no": "no.jpg"
}

# Cargar las imágenes en memoria
sign_images = {}
for sign, image_file in signs.items():
    sign_images[sign] = pygame.image.load(image_file)

# Crear una lista con las señas que se van a mostrar en la aplicación
sign_list = ["hello", "goodbye", "thank you", "sorry", "yes", "no"]

# Inicializar el índice de la seña actual
current_sign_index = 0

# Bucle principal de la aplicación
while True:
    # Obtener la seña actual
    current_sign = sign_list[current_sign_index]

    # Mostrar la seña en la ventana
    window.blit(sign_images[current_sign], (0, 0))
    pygame.display.flip()

    # Esperar a que el usuario presione una tecla
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Si se presiona la tecla derecha, ir a la siguiente seña
            if event.key == pygame.K_RIGHT:
                current_sign_index += 1
                if current_sign_index >= len(sign_list):
                    current_sign_index = 0
            # Si se presiona la tecla izquierda, ir a la seña anterior
            elif event.key == pygame.K_LEFT:
                current_sign_index -= 1
                if current_sign_index < 0:
                    current_sign_index = len(sign_list) - 1
            # Si se presiona cualquier otra tecla, salir de la aplicación
            else:
                pygame.quit()
                sys.exit()


                