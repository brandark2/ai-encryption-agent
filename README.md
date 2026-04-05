# Agent de Chiffrement Automatisé

## Présentation du projet
Ce projet consiste à développer un agent automatisé de chiffrement permettant de protéger les données sensibles en surveillant les fichiers et en appliquant un chiffrement en temps réel.

Le système détecte les nouveaux fichiers et les sécurise automatiquement, sans intervention humaine.

---

## Objectifs
- Protéger les données contre les accès non autorisés  
- Prévenir les fuites de données et limiter les risques liés aux ransomwares  
- Assurer la conformité avec les réglementations en vigueur (ex : RGPD)  
- Automatiser les processus de sécurité  

---

## Fonctionnalités
- Surveillance des fichiers en temps réel  
- Chiffrement automatique des nouveaux fichiers  
- Prévention du chiffrement multiple sur un même fichier  
- Solution légère et facilement déployable  

---

## Stratégie de sécurité
- Données au repos : chiffrement AES via la bibliothèque Fernet  
- Données en transit : TLS (approche conceptuelle)  
- Gestion des clés : génération dynamique et persistante de la clé de chiffrement  

---

## Cas d’utilisation
- Systèmes de santé (protection des données patients)  
- Systèmes financiers  
- Tout environnement manipulant des données sensibles  

---

## Technologies utilisées
- Python  
- Bibliothèque Cryptography  
- Watchdog (surveillance du système de fichiers)  

---

## Structure du projet
- `agent.py` : Agent principal de chiffrement  
- `test2.py` : Script de test  
- `requirements.txt` : Dépendances du projet  
- `.gitignore` : Fichiers ignorés  

---

## Exécution du projet
```bash
pip install -r requirements.txt
python agent.py
