import subprocess

# Lecture du fichier wifi.txt
with open("wifi.txt", "r") as file:
    wifi_profiles = file.read().splitlines()

# Obtention des clés de sécurité pour chaque profil
for profile in wifi_profiles:
    if ":" in profile:
        profile_name = profile.split(":")[1].strip()
        command = f"netsh wlan show profile name=\"{profile_name}\" key=clear"
        try:
            profile_output = subprocess.check_output(command, shell=True)
            profile_output = profile_output.decode("cp1252", errors="ignore")  # Utilisation de l'encodage cp1252
            # Écriture des informations dans un fichier
            with open("wifi_info.txt", "a") as output_file:
                output_file.write(f"Nom du profil : {profile_name}\n")
                output_file.write(profile_output + "\n\n")
        except subprocess.CalledProcessError:
            print(f"Erreur lors de l'exécution de la commande pour le profil {profile_name}")
    else:
        print(f"Le format du profil {profile} est incorrect. Vérifie le fichier wifi.txt.")

print("Les informations des profils Wi-Fi ont été enregistrées dans le fichier wifi_info.txt.")
