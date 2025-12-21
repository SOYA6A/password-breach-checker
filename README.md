# Password Breach Checker
Un outil Python simple qui vérifie si un mot de passe a été compromis dans des data breaches en utilisant l'API Have I Been Pwned.
## Pourquoi ce projet ?
En apprenant la cybersécurité, j'ai découvert que des millions de mots de passe sont volés chaque année lors de piratages de sites web. Ce projet permet de vérifier rapidement si un mot de passe figure dans ces bases de données compromises.

## Comment ça fonctionne ?
Le programme utilise l'API [Have I Been Pwned](https://haveibeenpwned.com/) qui contient plus de 613 millions de mots de passe compromis issus de diverses data breaches (Facebook, LinkedIn, Adobe, etc.).

### Sécurité
Le mot de passe n'est jamais envoyé en clair. Le programme utilise la technique k-anonymity :
1. Hash du mot de passe en SHA-1
2. Envoi des 5 premiers caractères uniquement à l'API
3. Vérification locale du hash complet

## Installation
```bash
git clone https://github.com/SOYA6A/password-breach-checker.git
cd password-breach-checker

# Installer les dépendances
pip3 install requests

# Lancer le programme
python3 password-breach-checker.py
```
## Utilisation
```bash
python3 password-breach-checker.py
```
Le programme demande un mot de passe à vérifier et affiche :
- Si le mot de passe a été compromis
- Le nombre de fois qu'il apparaît dans les data breaches

### Exemple
```
🔐 VÉRIFICATEUR DE MOT DE PASSE
========================================
Entrez un mot de passe à vérifier : password
⏳ Vérification en cours...
========================================
⚠️ DANGER ! Ce mot de passe a été volé 9,545,824 fois !
🚨 NE L'UTILISEZ PAS !
========================================
```
<img width="1380" height="429" alt="Screenshot 2025-12-19 at 23 20 41" src="https://github.com/user-attachments/assets/5dbdf4b8-fbea-42e1-bb2a-9594548dd28c" />

## Ce que j'ai appris

- Utilisation d'API REST avec Python
- Technique k-anonymity pour préserver la vie privée
- L'importance des mots de passe forts
- Les risques liés aux data breaches
