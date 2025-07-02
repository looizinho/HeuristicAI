import customtkinter as ctk

def salvar_config():
    usuario = entry_usuario.get()
    porta = entry_porta.get()
    ctk.CTkMessagebox.show_info("Configuração", f"Usuário: {usuario}\nPorta: {porta}")

ctk.set_appearance_mode("dark")  # dark/light/system
ctk.set_default_color_theme("blue")  # ou green, dark-blue...

root = ctk.CTk()
root.title("Configurações do MockAI")
root.geometry("350x200")

ctk.CTkLabel(root, text="Usuário:").pack(pady=6)
entry_usuario = ctk.CTkEntry(root)
entry_usuario.pack(pady=4)

ctk.CTkLabel(root, text="Porta:").pack(pady=6)
entry_porta = ctk.CTkEntry(root)
entry_porta.pack(pady=4)

ctk.CTkButton(root, text="Salvar", command=salvar_config).pack(pady=10)

root.mainloop()
