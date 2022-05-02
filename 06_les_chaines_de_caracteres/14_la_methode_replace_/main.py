texte = """Bonjour François, désolé je suis en retard.
Bonjour Maxime, il me dit en inspectant sa montre."""

texte = texte.replace("Bonjour ", "").replace(",", ":")
# texte = texte.replace("Bonjour", "Salut")
print(texte)