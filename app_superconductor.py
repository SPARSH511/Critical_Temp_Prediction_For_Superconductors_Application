import tkinter as tk
from tkinter import ttk, messagebox
import pickle as pk
import numpy as np
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras.models import load_model

# For the path of the current directory without the python file of the application
path = os.path.dirname(os.path.realpath(__file__))

class SuperconductorApp:
    def __init__(self, master):
        self.master = master
        master.title("Superconductor Critical Temperature Prediction")
        master.geometry("925x700")  # Start maximized

        # Create a main frame
        main_frame = tk.Frame(master)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Create a canvas
        self.canvas = tk.Canvas(main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Create another frame inside the canvas
        self.second_frame = tk.Frame(self.canvas)

        # Add that new frame to a window in the canvas
        self.canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Center frame
        center_frame = tk.Frame(self.second_frame)
        center_frame.pack(expand=True)

        # App title
        title_label = tk.Label(center_frame, text="Critical Temperature Prediction for Superconductors from Molecular Features", 
                               font=("Arial", 18, "bold"), wraplength=800)
        title_label.pack(pady=20)

        note_label = tk.Label(center_frame, text="The best model for actual test cases is found to be KNN Regressor - so it is recommended.", 
                        font=("Arial", 14, "bold"), wraplength=800)
        note_label.pack(pady=20)

        # Model selection dropdown
        model_frame = tk.Frame(center_frame)
        model_frame.pack(pady=20)

        model_label = tk.Label(model_frame, text="Select ML Model:", font=("Arial", 14))
        model_label.pack(side=tk.LEFT)

        self.models = ["Random Forest Regressor", "XGBoost Regressor", "KNN Regressor", 
                       "Support Vector Regressor", "Linear Regressor", 
                       "Genetic Algorithm Utilized Linear Regressor","ANN Based Regressor"]
        
        self.model_var = tk.StringVar(master)

        self.model_var.set(self.models[0])

        model_dropdown = ttk.Combobox(model_frame, textvariable=self.model_var, values=self.models, state="readonly", font=("Arial", 12))
        model_dropdown.pack(side=tk.LEFT, padx=10)

        # Input fields
        input_frame = tk.Frame(center_frame)
        input_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        left_frame = tk.Frame(input_frame)
        left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=(0, 20))

        right_frame = tk.Frame(input_frame)
        right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=(20, 0))

        self.features = [
            'mean_atomic_mass', 'wtd_mean_atomic_mass', 'wtd_entropy_atomic_mass', 'range_atomic_mass', 
            'wtd_range_atomic_mass', 'mean_fie', 'wtd_mean_fie', 'wtd_entropy_fie', 'wtd_range_fie', 
            'mean_atomic_radius', 'wtd_mean_atomic_radius', 'range_atomic_radius', 'wtd_range_atomic_radius', 
            'mean_Density', 'wtd_entropy_Density', 'range_Density', 'wtd_range_Density', 'mean_ElectronAffinity', 
            'wtd_mean_ElectronAffinity', 'wtd_entropy_ElectronAffinity', 'range_ElectronAffinity', 
            'wtd_range_ElectronAffinity', 'wtd_std_ElectronAffinity', 'mean_FusionHeat', 'range_FusionHeat', 
            'wtd_range_FusionHeat', 'mean_ThermalConductivity', 'wtd_gmean_ThermalConductivity', 
            'entropy_ThermalConductivity', 'wtd_entropy_ThermalConductivity', 'wtd_range_ThermalConductivity', 
            'wtd_std_ThermalConductivity', 'gmean_Valence', 'range_Valence', 'wtd_range_Valence'
        ]

        self.input_vars = []
        for i, feature in enumerate(self.features):
            if i < 18:
                frame = left_frame
            else:
                frame = right_frame
            
            label = tk.Label(frame, text=f"{feature}:", font=("Arial", 12))
            label.grid(row=i % 18, column=0, sticky="w", pady=(0, 10))
            
            var = tk.StringVar()
            entry = tk.Entry(frame, textvariable=var, font=("Arial", 12))
            entry.grid(row=i % 18, column=1, sticky="ew", pady=(0, 10), padx=(10, 0))
            
            self.input_vars.append(var)

        # Declaring the result variable
        self.result_var = tk.StringVar()

        # Predict button
        predict_button = tk.Button(center_frame, text="Predict", command = self.predict_critical_temperature, font=("Arial", 14))
        predict_button.pack(pady=20)

        # Prediction result
        result_label = tk.Label(center_frame, text="Predicted Critical Temperature:", font=("Arial", 14))
        result_label.pack()

        result_entry = tk.Entry(center_frame, textvariable = self.result_var, state='readonly', width=20, font=("Arial", 12))
        result_entry.pack()

        # Add some space after the result
        tk.Label(self.second_frame).pack(pady=15)

        # Configure grid
        left_frame.grid_columnconfigure(1, weight=1)
        right_frame.grid_columnconfigure(1, weight=1)
    
    # Part where the critical temperature is predicted
    def predict_critical_temperature(self):
        model = self.model_var.get()
        inputs = []
        
        for var in self.input_vars:
            try:
                value = float(var.get())
                inputs.append(value)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a numerical value as input.")
                return
            
        # Using the models to predict here and sending the output
        ind = self.models.index(model)

        if ind == 0:
            with open(path+"\\models\\Random_Forest_Regressor_model.pkl", 'rb') as file:  
                mod = pk.load(file)
            self.result_var.set(str(mod.predict(np.array(inputs).reshape(1,-1))[0]))
        elif ind == 1:
            with open(path+"\\models\\XG_Boost_Regressor_model.pkl", 'rb') as file:  
                mod = pk.load(file)
            self.result_var.set(str(mod.predict(np.array(inputs).reshape(1,-1))[0]))
        elif ind == 2:
            with open(path+"\\models\\KNN_Regressor_model.pkl", 'rb') as file:  
                mod = pk.load(file)
            self.result_var.set(str(mod.predict(np.array(inputs).reshape(1,-1))[0]))
        elif ind == 3:
            with open(path+"\\models\\Support_Vector_Regressor_model.pkl", 'rb') as file:  
                mod = pk.load(file)
            self.result_var.set(str(mod.predict(np.array(inputs).reshape(1,-1))[0]))
        elif ind == 4:
            with open(path+"\\models\\Linear_Regression_model.pkl", 'rb') as file:  
                mod = pk.load(file)
            self.result_var.set(str(mod.predict(np.array(inputs).reshape(1,-1))[0]))
        elif ind == 5:
            # Directly using weights obtained after training from the Google Colab Notebook  

            wts = np.array([-2.288883618308785, -2.6940949643349423, 14.37917935720041, 
                            12.214581920894489, -6.584401360461047, 0.8348088797775822, 
                            1.6539544952176761, 6.333968335838223, 4.489256094294288, 
                            5.700502112289965, 2.5228150269933516, 20.60866679896782, 
                            -2.1284944209051866, -7.885470064943143, 5.720249216389284, 
                            2.7036641392195095, -2.037651401201342, -6.225497720327342, 
                            -3.844646281887579, -3.481700474647035, 3.025692552760201, 
                            -3.5100345457443107, 2.549603981009403, -4.868273186606164, 
                            -10.039802418982138, -3.613965703381885, 12.258207492095318, 
                            -3.145943525182687, 5.516131110506464, -4.69744008500502, 
                            12.354430936811234, 26.152386969011328, -12.011223617220088, 
                            -12.624991745198086, -4.8275195808093985])

            features = np.array(inputs)
            res = np.dot(features,wts)
            self.result_var.set(res)
            
        else:
            mod = load_model(path+"\\models\\ANN_Regression_model.h5",compile=False)
            self.result_var.set(str(mod.predict(np.array(inputs).reshape(1,-1))[0][0]))



def main():
    root = tk.Tk()
    app = SuperconductorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


