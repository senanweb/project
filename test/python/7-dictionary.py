tooles = {"salawe": 1, "nadom": 3, "sinan": 1}
print(tooles)
# ========================
samara = {"salawe": ["saed", "hatam", "nadom"], "nadom": [
    "wasan", "arkan", "sinan"], "sinan": ["omar"]}
print(samara)
# ========================= Add
samara["sinan"] = ["omar", "Etemad"]
print(samara)
# ========================= update
samara.update({"arkan": ["nuna"]})
print(samara)
