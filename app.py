import customtkinter as ctk
import random
import json
from datetime import datetime

ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue", "green", "dark-blue"

symptom_database = {
    "cold": {"medicine": ["Paracetamol", "Antihistamines", "Decongestants"], "remedies": ["Drink warm fluids", "Rest", "Honey and ginger tea"], "severity": "Mild"},
    "cough": {"medicine": ["Cough Syrup", "Antihistamines", "Lozenges"], "remedies": ["Honey and lemon tea", "Gargle with salt water", "Steam inhalation"], "severity": "Mild"},
    "fever": {"medicine": ["Paracetamol", "Ibuprofen", "Aspirin"], "remedies": ["Stay hydrated", "Cold compress", "Rest well"], "severity": "Moderate"},
    "chest pain": {"medicine": ["Aspirin", "Nitroglycerin", "Consult doctor"], "remedies": ["Seek medical help immediately"], "severity": "Severe"},
}

def get_suggestions():
    symptoms = symptom_entry.get().lower().split(",")
    symptoms = [symptom.strip() for symptom in symptoms]
    medicines = set()
    remedies = set()
    severity_levels = []
    
    for symptom in symptoms:
        if symptom in symptom_database:
            medicines.update(symptom_database[symptom]["medicine"])
            remedies.update(symptom_database[symptom]["remedies"])
            severity_levels.append(symptom_database[symptom]["severity"])
    
    medicine_text = f"Medicine:\n{", ".join(medicines) if medicines else 'No specific medicine found'}"
    remedy_text = f"Home Remedies:\n{', '.join(remedies) if remedies else 'Try consulting a doctor for better advice'}"
    severity_text = f"Severity Level: {', '.join(set(severity_levels)) if severity_levels else 'Unknown'}"
    
    medicine_result.configure(text=medicine_text)
    remedy_result.configure(text=remedy_text)
    severity_result.configure(text=severity_text)
    
    save_medical_history(symptoms, medicine_text, remedy_text, severity_text)

def save_medical_history(symptoms, medicine, remedies, severity):
    history = {"date": str(datetime.now()), "symptoms": symptoms, "medicine": medicine, "remedies": remedies, "severity": severity}
    try:
        with open("medical_history.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(history)
    with open("medical_history.json", "w") as file:
        json.dump(data, file, indent=4)

def bmi_calculator():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        bmi = weight / (height ** 2)
        bmi_result.configure(text=f"BMI: {bmi:.2f}")
    except ValueError:
        bmi_result.configure(text="Invalid input")

# GUI setup
root = ctk.CTk()
root.title("HEALTH BOT")
root.geometry("750x700")
root.configure(bg="#1E1E2F")

frame = ctk.CTkFrame(root, corner_radius=15, fg_color="#292B3A")
frame.pack(pady=20, padx=20, fill="both", expand=True)

nav_label = ctk.CTkLabel(frame, text="HEALTH BOT", font=("Arial", 28, "bold"), text_color="lightgreen")
nav_label.pack(pady=(30, 10))

description_label = ctk.CTkLabel(frame, text="Enter your symptoms (comma-separated):", font=("Arial", 14), text_color="white")
description_label.pack(pady=5)

symptom_entry = ctk.CTkEntry(frame, width=400, height=45, corner_radius=10, font=("Arial", 14))
symptom_entry.pack(pady=10)

submit_button = ctk.CTkButton(frame, text="Get Diagnosis", command=get_suggestions, corner_radius=10, height=45, font=("Arial", 14, "bold"))
submit_button.pack(pady=20)

medicine_result = ctk.CTkLabel(frame, text="", font=("Arial", 14, "bold"), text_color="lightgreen", wraplength=500, justify="left")
medicine_result.pack(pady=10)

remedy_result = ctk.CTkLabel(frame, text="", font=("Arial", 14, "bold"), text_color="lightblue", wraplength=500, justify="left")
remedy_result.pack(pady=10)

severity_result = ctk.CTkLabel(frame, text="", font=("Arial", 14, "bold"), text_color="red")
severity_result.pack(pady=10)

bmi_label = ctk.CTkLabel(frame, text="Enter weight (kg) and height (cm) for BMI:", font=("Arial", 16), text_color="yellow")
bmi_label.pack(pady=5)

weight_entry = ctk.CTkEntry(frame, width=100, height=30, corner_radius=10)
weight_entry.pack(pady=5)

height_entry = ctk.CTkEntry(frame, width=100, height=30, corner_radius=10)
height_entry.pack(pady=5)

bmi_button = ctk.CTkButton(frame, text="Calculate BMI", font=("Arial", 14, "bold"), command=bmi_calculator, corner_radius=10)
bmi_button.pack(pady=10)

bmi_result = ctk.CTkLabel(frame, text="", font=("Arial", 18, "bold"), text_color="yellow")
bmi_result.pack()

root.mainloop()
