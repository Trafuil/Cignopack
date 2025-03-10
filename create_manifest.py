import os
import hashlib
import json

def calc_md5(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def scan_directory(base_dir, repo_url):
    files = []
    for root, dirs, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename == "manifest.json":
                continue
                
            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, base_dir)
            rel_path = rel_path.replace("\\", "/")  # Normalizza path per Windows
            
            files.append({
                "path": rel_path,
                "hash": calc_md5(full_path),
                "url": f"{repo_url}/{rel_path}",
                "action": "update"
            })
    
    return files

def create_manifest(base_dir, repo_url, minecraft_version, version):
    files = scan_directory(base_dir, repo_url)
    
    manifest = {
        "version": version,
        "minecraft_version": minecraft_version,
        "files": files
    }
    
    with open(os.path.join(base_dir, "manifest.json"), 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"Creato manifest.json con {len(files)} file")

if __name__ == "__main__":
    # Configurazione
    base_dir = "C:\\Users\\lucaf\\Desktop\\Documenti\\Games\\Minecraft\\cignopack"  # Modifica con il percorso della tua modpack
    repo_url = "https://github.com/Trafuil/Cignopack.git"  # Modifica con l'URL del tuo repository
    minecraft_version = "1.12.2"  # Modifica con la versione di Minecraft
    version = "1.0.0"  # Versione della modpack
    
    create_manifest(base_dir, repo_url, minecraft_version, version)