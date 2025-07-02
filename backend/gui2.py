import customtkinter as ctk

ctk.set_appearance_mode("system")  # tema automático!
#ctk.set_default_color_theme("blue")  # você pode mudar para "green", "dark-blue", etc.

root = ctk.CTk()
root.title("Configuração dinâmica!")
root.geometry("640x480")

ctk.CTkLabel(root, text="Olha eu me adaptando ao seu sistema!").pack(pady=20)

root.mainloop()
