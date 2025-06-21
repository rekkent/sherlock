import os

# Variációk a felhasználónévre
usernames = [
"karkusdora",
"karkus.dora",
"dora.karkus",
"karkus_dora",
"dora_karkus",
"dori.k",
"k.dora",
"karkus123",
"karkusd",
"dora1990", # ha ismered a születési évét, állítsd be
]

# Összeállítjuk a parancsot
for username in usernames:
print(f"🔍 Keresés: {username}")
os.system(f"python3 sherlock {username} --output results_{username}.txt")
