phishing_keywords = ["urgent","mot de passe","cliquer ici","votre compte","bloqué","sécurité","gagner de l'argent","offre spéciale","gratuit","vérifiez"]

def analyser_email(texte):
    compteur = 0
    for mot in phishing_keywords:
        if mot.lower() in texte.lower():
            compteur += 1
    score = (compteur / len(phishing_keywords)) * 100
    return score

email_test = """Bonjour, votre compte a été bloqué pour des raisons de sécurité.
Veuillez cliquer ici pour réinitialiser votre mot de passe."""

resultat = analyser_email(email_test)
print("Score de suspicion :", round(resultat, 1), "%")

if resultat >= 50:
    print("⚠️ Ce message semble suspect (potentiel phishing).")
else:
    print("✅ Ce message ne semble pas dangereux.")
