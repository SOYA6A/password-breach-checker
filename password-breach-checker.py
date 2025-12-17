import requests
import hashlib

def verifier_mot_de_passe(mot_de_passe):
    """
    Vérifie si un mot de passe a été volé.
    """
    # 1. Transformer le mot de passe en code secret (hash)
    hash_mdp = hashlib.sha1(mot_de_passe.encode('utf-8')).hexdigest().upper()
    
    # 2. Prendre les 5 premiers caractères
    debut = hash_mdp[:5]
    fin = hash_mdp[5:]
    
    # 3. Demander au site "Have I Been Pwned"
    url = f"https://api.pwnedpasswords.com/range/{debut}"
    reponse = requests.get(url)
    
    # 4. Chercher notre mot de passe dans la liste
    for ligne in reponse.text.splitlines():
        hash_trouve, nombre = ligne.split(':')
        if hash_trouve == fin:
            return int(nombre)  # Trouvé = dangereux !
    
    return 0  # Pas trouvé = sécurisé !

# Programme principal
print("\n🔐 VÉRIFICATEUR DE MOT DE PASSE")
print("="*40)

mdp = input("\nEntrez un mot de passe à vérifier : ")

print("\n⏳ Vérification en cours...\n")

resultat = verifier_mot_de_passe(mdp)

print("="*40)
if resultat == 0:
    print("✅ BON ! Ce mot de passe est sécurisé.")
    print("Il n'a jamais été volé.")
else:
    print(f"⚠️ DANGER ! Ce mot de passe a été volé {resultat:,} fois !")
    print("🚨 NE L'UTILISEZ PAS !")
print("="*40 + "\n")