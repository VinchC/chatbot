import customtkinter as ctk

# Configuration de l'interface graphique
app = ctk.CTk()
app.geometry("500x600")
app.title("Mon chatbot")

# Création de l'en-tête
header = ctk.CTkLabel(app, text="Hello", font=("Arial", 18, "bold"))
header.pack(pady=10)

# Création de la zone d'affichage des messages
chat = ctk.CTkTextbox(app, height=400, state="disabled")
chat.tag_config("user", foreground="red")
chat.tag_config("bot", foreground="blue")
chat.pack(pady = 10, padx = 10, fill = "both", expand = True)

# Création du champ de saisie utilisateur
user_input_frame = ctk.CTkFrame(app)
user_input_frame.pack(pady = 10, padx = 10, fill = "x")

user_input = ctk.CTkEntry(user_input_frame, placeholder_text = "Ecrivez votre message...", width = 350)
user_input.pack(side = "left", padx = 5)

send_button = ctk.CTkButton(user_input_frame, text = "Envoyer")
send_button.pack(side = "left")

app.mainloop()