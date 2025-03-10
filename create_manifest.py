import os
import hashlib
import json

# Funzione per calcolare l'hash SHA1 di un file
def get_file_hash(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            sha1.update(chunk)
    return sha1.hexdigest()

# Directory del repository
repo_dir = 'C:\\Users\\lucaf\\Desktop\\Documenti\\Games\\Minecraft\\cignopack'

# URL base per il repository su GitHub
base_url = 'https://github.com/Trafuil/Cignopack.git'

# Lista per raccogliere tutte le informazioni sui file
file_info = []

# Scorri tutti i file nella repository
for root, dirs, files in os.walk(repo_dir):
    for file in files:
        file_path = os.path.join(root, file)
        
        # Calcola l'hash del file
        file_hash = get_file_hash(file_path)
        
        # Crea l'oggetto del file per il manifest
        relative_path = os.path.relpath(file_path, repo_dir)
        file_url = base_url + relative_path.replace(os.sep, '/')
        
        file_info.append({
            "path": relative_path,
            "hash": file_hash,
            "url": file_url,
            "action": "update"
        })

# Crea il manifest
manifest = {
    "version": "1.0.0",
    "minecraft_version": "1.12.2",
    "files": file_info
}

# Scrivi il file manifest.json
with open(os.path.join(repo_dir, 'manifest.json'), 'w') as f:
    json.dump(manifest, f, indent=4)

print("Manifest JSON creato con successo.")
