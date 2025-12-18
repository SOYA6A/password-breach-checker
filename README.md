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
