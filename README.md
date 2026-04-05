# Agent de Chiffrement Automatisé

## Sommaire
1. Présentation du projet
2. Objectifs
3. Fonctionnalités
4. Stratégie de sécurité
5. Cas d'utilisation
6. Technologies utilisées
7. Structure du projet
8. Installation et exécution
9. Limites et améliorations possibles
10. Conclusion

---

## 1. Présentation du projet
Ce projet consiste à développer un agent automatisé capable de chiffrer des fichiers sensibles en temps réel.  
Le système détecte automatiquement les nouveaux fichiers dans un dossier spécifique et applique un chiffrement AES sans intervention humaine.

---

## 2. Objectifs
- Protéger les données contre tout accès non autorisé  
- Prévenir les fuites de données et limiter les risques liés aux ransomwares  
- Automatiser les mécanismes de sécurité  
- Respecter les normes et réglementations (ex : RGPD)

---

## 3. Fonctionnalités
- Surveillance des fichiers en temps réel  
- Chiffrement automatique des fichiers nouvellement ajoutés  
- Gestion d’erreurs basique mais sécurisée  
- Prévention du chiffrement multiple sur un même fichier  

---

## 4. Stratégie de sécurité
- Chiffrement AES via la bibliothèque Fernet  
- Gestion de la clé générée dynamiquement et persistante dans un fichier  
- Journaux d’activité pour tracer toutes les actions de l’agent

---

## 5. Cas d'utilisation
- Systèmes de santé (protection des données patients)  
- Systèmes financiers  
- Tout environnement manipulant des données sensibles ou confidentielles  

---

## 6. Technologies utilisées
- Python  
- Cryptography  
- Watchdog (pour la surveillance du système de fichiers)  

---

## 7. Structure du projet
- `agent.py` : code principal de l’agent de chiffrement  
- `test2.py` : script de test  
- `requirements.txt` : dépendances Python  
- `.gitignore` : fichiers à ignorer dans le dépôt Git  
- `README.md` : documentation du projet

---

## 8. Installation et exécution
1. Cloner le dépôt :
```bash
git clone <lien_du_depot>
cd ai-encryption-agent
