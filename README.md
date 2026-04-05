# 🔐 Agent de Chiffrement Automatisé

## 📌 Présentation du projet
Ce projet consiste à développer un agent automatisé de chiffrement permettant de protéger les données sensibles en surveillant les fichiers et en appliquant un chiffrement en temps réel.

Le système simule un agent intelligent capable de détecter de nouveaux fichiers et de les sécuriser sans intervention humaine.

---

## 🎯 Objectifs
- Protéger les données contre les accès non autorisés  
- Prévenir les fuites de données et limiter les risques liés aux ransomwares  
- Assurer une conformité avec les réglementations (ex : RGPD)  
- Automatiser les mécanismes de sécurité  

---

## ⚙️ Fonctionnalités
- Surveillance des fichiers en temps réel  
- Chiffrement automatique des nouveaux fichiers  
- Prévention du chiffrement multiple (boucles)  
- Solution légère et facilement déployable  

---

## 🔐 Stratégie de sécurité
- **Données au repos :** chiffrement AES via la bibliothèque Fernet  
- **Données en transit :** TLS (approche conceptuelle)  
- **Gestion des clés :** génération dynamique d’une clé de chiffrement  

---

## 🤖 Aspect “IA”
Ce projet simule un agent intelligent en :
- détectant automatiquement les modifications de fichiers  
- prenant des décisions sans intervention humaine  
- appliquant des règles de sécurité prédéfinies  

Même sans machine learning, il s’inscrit dans une logique d’agent autonome.

---

## 🧠 Cas d’utilisation
Ce système peut être utilisé dans :
- les systèmes de santé (conformité, protection des données patients)  
- les systèmes financiers  
- tout environnement manipulant des données sensibles  

---

## 🛠️ Technologies utilisées
- Python  
- Bibliothèque Cryptography  
- Watchdog (surveillance du système de fichiers)  

---

## 📂 Structure du projet
- `agent.py` : Agent principal de chiffrement  
- `test2.py` : Script de test  
- `requirements.txt` : Dépendances du projet  
- `.gitignore` : Fichiers ignorés  

---

## ▶️ Exécution du projet
```bash
pip install -r requirements.txt
python agent.py
