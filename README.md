# Critical Temperature Prediction for Superconductors

This is a Tkinter-based Python application that lets a user enter the values of 35 selected molecular features of a superconductor and predict its critical temperature. Users can choose from the following models for prediction:

- Random Forest Regressor
- XGBoost Regressor
- KNN Regressor
- Support Vector Regressor
- Linear Regressor
- Genetic Algorithm Utilized Linear Regressor
- ANN Based Regressor

## Features

The application uses the following 35 features for prediction:

### Molecular Parameters Used  

| **Variable**               | **Units**                               | **Description**                                                 |
|----------------------------|-----------------------------------------|-----------------------------------------------------------------|
| Atomic Mass                | atomic mass units (AMU)                 | Total proton and neutron rest masses                            |
| First Ionization Energy    | kilo-Joules per mole (kJ/mol)           | Energy required to remove a valence electron                    |
| Atomic Radius              | picometer (pm)                          | Calculated atomic radius                                        |
| Density                    | kilograms per meters cubed (kg/m³)      | Density at standard temperature and pressure                    |
| Electron Affinity          | kilo-Joules per mole (kJ/mol)           | Energy required to add an electron to a neutral atom            |
| Fusion Heat                | kilo-Joules per mole (kJ/mol)           | Energy to change from solid to liquid without temperature change|
| Thermal Conductivity       | watts per meter-Kelvin (W/(m x K))      | Thermal conductivity coefficient κ                              |
| Valence                    | no units                                | Typical number of chemical bonds formed by the element          |
------------------------------------------------------------------------------------------------------------------------------------------


### Feature & Description  

| **Feature**                  | **Formula**                            | **Sample Value**|
|------------------------------|----------------------------------------|-----------------|
| Mean                         | μ = (t₁ + t₂) / 2                      | 35.4            |
| Weighted mean                | ν = (p₁t₁ + p₂t₂)                      | 44.42           |
| Geometric mean               | (t₁t₂)¹/²                              | 33.22           |
| Weighted geometric mean      | (t₁)p¹(t₂)p²                           | 43.22           |
| Entropy                      | -w₁ln(w₁) - w₂ln(w₂)                   | 0.62            |
| Weighted entropy             | -A ln(A) - B ln(B)                     | 0.23            |
| Range                        | t₁ - t₂ (t₁ > t₂)                      | 26              |
| Weighted range               | p₁t₁ - p₂t₂                            | 37.81           |
| Standard deviation           | [(1/2)((t₁-μ)²+(t₂-μ)²)]¹/²            | 12.1            |
| Weighted standard deviation  | [p₁(t₁-ν)²+p₂(t₂-ν)²)]¹/²              | 8.78            |
-------------------------------------------------------------------------------------------

### Key to the Actual 35 Parameter Inputs in the Model  

| **Term**                      | **Expanded Name**                                   |
|-------------------------------|-----------------------------------------------------|
| mean_atomic_mass              | Mean Atomic Mass                                    |
| wtd_mean_atomic_mass          | Weighted Mean Atomic Mass                           |
| wtd_entropy_atomic_mass       | Weighted Entropy of Atomic Mass                     |
| range_atomic_mass             | Range of Atomic Mass                                |
| wtd_range_atomic_mass         | Weighted Range of Atomic Mass                       |
| mean_fie                      | Mean First Ionization Energy                        |
| wtd_mean_fie                  | Weighted Mean First Ionization Energy               |
| wtd_entropy_fie               | Weighted Entropy of First Ionization Energy         |
| wtd_range_fie                 | Weighted Range of First Ionization Energy           |
| mean_atomic_radius            | Mean Atomic Radius                                  |
| wtd_mean_atomic_radius        | Weighted Mean Atomic Radius                         |
| range_atomic_radius           | Range of Atomic Radius                              |
| wtd_range_atomic_radius       | Weighted Range of Atomic Radius                     |
| mean_Density                  | Mean Density                                        |
| wtd_entropy_Density           | Weighted Entropy of Density                         |
| range_Density                 | Range of Density                                    |
| wtd_range_Density             | Weighted Range of Density                           |
| mean_ElectronAffinity         | Mean Electron Affinity                              |
| wtd_mean_ElectronAffinity     | Weighted Mean Electron Affinity                     |
| wtd_entropy_ElectronAffinity  | Weighted Entropy of Electron Affinity               |
| range_ElectronAffinity        | Range of Electron Affinity                          |
| wtd_range_ElectronAffinity    | Weighted Range of Electron Affinity                 |
| wtd_std_ElectronAffinity      | Weighted Standard Deviation of Electron Affinity    |
| mean_FusionHeat               | Mean Fusion Heat                                    |
| range_FusionHeat              | Range of Fusion Heat                                |
| wtd_range_FusionHeat          | Weighted Range of Fusion Heat                       |
| mean_ThermalConductivity      | Mean Thermal Conductivity                           |
| wtd_gmean_ThermalConductivity | Weighted Geometric Mean of Thermal Conductivity     |
| entropy_ThermalConductivity   | Entropy of Thermal Conductivity                     |
| wtd_entropy_ThermalConductivity| Weighted Entropy of Thermal Conductivity           |
| wtd_range_ThermalConductivity | Weighted Range of Thermal Conductivity              |
| wtd_std_ThermalConductivity   | Weighted Standard Deviation of Thermal Conductivity |
| gmean_Valence                 | Geometric Mean of Valence                           |
| range_Valence                 | Range of Valence                                    |
| wtd_range_Valence             | Weighted Range of Valence                           |
---------------------------------------------------------------------------------------


## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/SPARSH511/Critical_Temp_Prediction_For_Superconductors_Application.git
   cd Critical_Temp_Prediction_For_Superconductors_Application

2. **Install Dependencies:**

   Ensure you have Python installed on your system. You can use pip to install the necessary dependencies:
   ```sh
   pip install -r requirements.txt

## Usage

To run the application, execute the following command in your terminal:
  ```sh
  python app_superconductor.py


