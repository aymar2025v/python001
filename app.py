import customtkinter as ctk

# Configuración del tema visual
ctk.set_appearance_mode("System")  # Detecta si usas modo oscuro o claro en Windows
ctk.set_default_color_theme("blue")  # Tema de color para los botones

# Crear la ventana principal
ventana = ctk.CTk()
ventana.title("Mi Primer Formulario")
ventana.geometry("400x300")

# Función que se ejecuta al presionar el botón
def al_hacer_clic():
    texto_ingresado = cuadro_texto.get()
    etiqueta_resultado.configure(text=f"¡Hola, {texto_ingresado}! Datos guardados.")

# Crear los elementos de la interfaz (Widgets)
etiqueta = ctk.CTkLabel(ventana, text="Escribe tu nombre:", font=("Arial", 16))
etiqueta.pack(pady=15)

cuadro_texto = ctk.CTkEntry(ventana, placeholder_text="Tu nombre aquí...")
cuadro_texto.pack(pady=10)

boton = ctk.CTkButton(ventana, text="Enviar Formulario", command=al_hacer_clic)
boton.pack(pady=15)

etiqueta_resultado = ctk.CTkLabel(ventana, text="", font=("Arial", 14, "bold"))
etiqueta_resultado.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
