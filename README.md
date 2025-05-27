# Détecteur de phishing par e-mail
Mini-projet en Python pour **analyser un e-mail et détecter s'il est potentiellement suspect** à l'aide d'une liste de mots-clés liés au phishing.

---

## Objectif
- Analyser le contenu d’un e-mail texte
- Repérer des mots typiques d’arnaques (phishing)
- Calculer un score de suspicion (%) et afficher une alerte si nécessaire

---

## Fonctionnement
- Une liste de mots-clés est définie (ex : "mot de passe", "sécurité", "urgent")
- Le programme compare ces mots au texte de l’e-mail
- Plus il y a de mots suspects, plus le score augmente
- Une alerte s’affiche si le score dépasse 50%

---

## Exemple de code
```python
email_test = """Bonjour, votre compte a été bloqué pour des raisons de sécurité.
Veuillez cliquer ici pour réinitialiser votre mot de passe."""

Sortie attendue
- Score de suspicion : 50.0 %
⚠️ Ce message semble suspect (potentiel phishing).
