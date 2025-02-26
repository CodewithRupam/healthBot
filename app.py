import customtkinter as ctk
import random

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("green") 

symptom_database = {
    "cold": {"medicine": ["Paracetamol", "Antihistamines", "Decongestants"], "remedies": ["Drink warm fluids", "Rest", "Honey and ginger tea"]},
    "cough": {"medicine": ["Cough Syrup", "Antihistamines", "Lozenges"], "remedies": ["Honey and lemon tea", "Gargle with salt water", "Steam inhalation"]},
    "headache": {"medicine": ["Ibuprofen", "Acetaminophen", "Aspirin"], "remedies": ["Hydrate well", "Apply peppermint oil", "Rest in a dark room"]},
    "nausea": {"medicine": ["Anti-nausea medication", "Domperidone", "Metoclopramide"], "remedies": ["Ginger tea", "Deep breathing", "Avoid strong odors"]},
    "fever": {"medicine": ["Paracetamol", "Ibuprofen", "Aspirin"], "remedies": ["Stay hydrated", "Cold compress", "Rest well"]},
    "chills": {"medicine": ["Paracetamol", "Ibuprofen", "Warm fluids"], "remedies": ["Warm blankets", "Stay hydrated", "Rest well"]},
    "sore throat": {"medicine": ["Lozenges", "Pain relievers", "Antiseptic spray"], "remedies": ["Gargle with warm salt water", "Drink warm tea", "Use honey and lemon"]},
    "stomach pain": {"medicine": ["Antacids", "Buscopan", "Peppermint oil capsules"], "remedies": ["Drink ginger tea", "Avoid spicy food", "Eat smaller meals"]},
    "diarrhea": {"medicine": ["Loperamide", "ORS (Oral Rehydration Solution)", "Probiotics"], "remedies": ["Drink plenty of fluids", "Eat bananas and rice", "Avoid dairy"]},
    "fatigue": {"medicine": ["Multivitamins", "Iron supplements", "Electrolyte drinks"], "remedies": ["Get enough sleep", "Exercise regularly", "Stay hydrated"]}
}

def get_suggestions():
    symptoms = symptom_entry.get().lower().split(",")
    symptoms = [symptom.strip() for symptom in symptoms]
    medicines = set()
    remedies = set()
    
    for symptom in symptoms:
        if symptom in symptom_database:
            medicines.update(random.sample(symptom_database[symptom]["medicine"], min(3, len(symptom_database[symptom]["medicine"]))))
            remedies.update(random.sample(symptom_database[symptom]["remedies"], min(3, len(symptom_database[symptom]["remedies"]))))
    
    medicine_result.configure(text=f"Medicine:\n{", ".join(medicines) if medicines else 'No specific medicine found'}")
    remedy_result.configure(text=f"Home Remedies:\n{', '.join(remedies) if remedies else 'Try consulting a doctor for better advice'}")

root = ctk.CTk()
root.title("HEALTH BOT")
root.geometry("600x550")
root.configure(bg="#1E1E2F")
root.resizable(False, False)
frame = ctk.CTkFrame(root, corner_radius=15, fg_color="#292B3A")
frame.pack(pady=20, padx=20, fill="both", expand=True)

nav_label = ctk.CTkLabel(frame, text="HEALTH BOT", font=("Arial", 28, "bold"), text_color="white")
nav_label.pack(pady=(30, 10))

description_label = ctk.CTkLabel(frame, text="Enter your symptoms (separate by commas):", font=("Arial", 14), text_color="white")
description_label.pack(pady=5)

symptom_entry = ctk.CTkEntry(frame, width=400, height=45, corner_radius=10, font=("Arial", 14))
symptom_entry.pack(pady=10)

submit_button = ctk.CTkButton(frame, text="Get Diagnosis", command=get_suggestions, corner_radius=10, height=45, font=("Arial", 14, "bold"))
submit_button.pack(pady=20)
description_label2 = ctk.CTkLabel(frame, text="If situation is extreme than try to consult a doctor", font=("Arial", 14), text_color="white")
description_label2.pack(pady=15)
medicine_result = ctk.CTkLabel(frame, text="", font=("Arial", 20, "bold"), text_color="lightgreen", wraplength=500, justify="left")
medicine_result.pack(pady=10)

remedy_result = ctk.CTkLabel(frame, text="", font=("Arial", 18, "bold"), text_color="lightblue", wraplength=500, justify="left")
remedy_result.pack(pady=10)

root.mainloop()
