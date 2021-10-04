import pandas as pd

df = pd.read_csv("Project130.csv")
radius = df["Radius"].tolist()
mass = df["Mass"].tolist()
radius_in_m = []
for i in radius:
    radi = i*6.957e+8
    radius_in_m.append(radi)
mass_in_kg = []
for i in mass:
    mas = i*1.989e+30
    mass_in_kg.append(mas)
G = 6.67e-11
Gravity = []
for i in range(0,len(radius_in_m)):
    gravity = (mass_in_kg[i]*G/radius_in_m[i]**2)
    Gravity.append(gravity)
print(Gravity)
df["Gravity"] = Gravity
df.to_csv("project_131.csv")


