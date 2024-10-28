# Este código es para controlar en que posición actual esta la ventana
# y que al cambiar a otra ventana, está aparezca en la posición anterior

# Variables para almacenar la posición de la ventana
pos_x = None
pos_y = None

def obtener_posicion(ventana):
    """Obtiene la posición actual de la ventana."""
    global pos_x, pos_y
    pos_x = ventana.x()
    pos_y = ventana.y()

def colocar_ventana(ventana):
    """Coloca la ventana en la última posición almacenada."""
    global pos_x, pos_y
    if pos_x is not None and pos_y is not None:
        ventana.move(pos_x, pos_y)
