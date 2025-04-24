import os
import subprocess
import sys

VENV_DIR = ".venv"

def create_virtualenv():
    if not os.path.isdir(VENV_DIR):
        print("🔧 Création de l'environnement virtuel dans '.venv'...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
        print("✅ Environnement virtuel créé.")
    else:
        print("✅ Environnement virtuel déjà présent, rien à faire.")

def show_activation_instructions():
    print("\n📢 Pour activer l'environnement virtuel :\n")
    if os.name == 'nt':
        print(r"    .venv\Scripts\activate")
    else:
        print("    source .venv/bin/activate")

def create_requirements_file():
    if not os.path.exists("requirements.txt"):
        with open("requirements.txt", "w") as f:
            f.write("")
        print("📄 Fichier requirements.txt créé.")
    else:
        print("📄 Fichier requirements.txt déjà présent.")

def install_dependencies():
    with open("requirements.txt", "r") as f:
        deps = [line.strip() for line in f if line.strip()]
    if deps:
        print("📦 Installation des dépendances...")
        subprocess.run([os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "pip"), "install", "-r", "requirements.txt"])
        print("✅ Dépendances installées.")
    else:
        print("📦 Aucune dépendance à installer (requirements.txt vide).")

def ensure_venv_in_gitignore():
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            lines = f.read().splitlines()
    else:
        lines = []

    if VENV_DIR + "/" not in lines:
        with open(".gitignore", "a") as f:
            f.write(f"\n{VENV_DIR}/\n")
        print(f"🛡️ Ajout de '{VENV_DIR}/' à .gitignore.")
    else:
        print(f"🛡️ '{VENV_DIR}/' est déjà dans .gitignore.")

if __name__ == "__main__":
    create_virtualenv()
    ensure_venv_in_gitignore()
    create_requirements_file()
    install_dependencies()
    show_activation_instructions()
    print("\n🔚 Fin de l'initialisation du projet.")