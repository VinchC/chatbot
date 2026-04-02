import customtkinter as ctk

# Configuration de l'interface graphique
app = ctk.CTk()
app.geometry("400x600")
app.title("Mon chatbot")

# Création de l'en-tête
header = ctk.CTkLabel(app, text="Hello", font=("Arial", 18, "bold"))
header.pack(pady=10)

# Création de la zone d'affichage des messages
chat = ctk.CTkTextbox(app, height=400, state="disabled")
chat.tag_config("user", foreground="red")
chat.tag_config("bot", foreground="blue")
chat.pack(pady = 10, padx = 10, fill = "both", expand = True)

app.mainloop()