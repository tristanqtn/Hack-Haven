```python
from pwn import *
import re

# Définir la table d'efficacité des types
effectiveness = {
    "Normal": {
        "Normal": 1,
        "Feu": 1,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 1,
        "Glace": 1,
        "Combat": 1,
        "Poison": 1,
        "Sol": 1,
        "Vol": 1,
        "Psy": 1,
        "Insecte": 1,
        "Roche": 0.5,
        "Spectre": 0,
        "Dragon": 1,
        "Ténèbres": 1,
        "Acier": 0.5,
        "Fée": 1
    },
    "Feu": {
        "Normal": 1,
        "Feu": 0.5,
        "Eau": 0.5,
        "Électrik": 1,
        "Plante": 2,
        "Glace": 2,
        "Combat": 1,
        "Poison": 1,
        "Sol": 1,
        "Vol": 1,
        "Psy": 1,
        "Insecte": 2,
        "Roche": 0.5,
        "Spectre": 1,
        "Dragon": 0.5,
        "Ténèbres": 1,
        "Acier": 2,
        "Fée": 1
    },
    "Eau": {
        "Normal": 1,
        "Feu": 2,
        "Eau": 0.5,
        "Électrik": 1,
        "Plante": 0.5,
        "Glace": 1,
        "Combat": 1,
        "Poison": 1,
        "Sol": 2,
        "Vol": 1,
        "Psy": 1,
        "Insecte": 1,
        "Roche": 2,
        "Spectre": 1,
        "Dragon": 0.5,
        "Ténèbres": 1,
        "Acier": 1,
        "Fée": 1
    },
    "Électrik": {
        "Normal": 1,
        "Feu": 1,
        "Eau": 2,
        "Électrik": 0.5,
        "Plante": 0.5,
        "Glace": 1,
        "Combat": 1,
        "Poison": 1,
        "Sol": 0,
        "Vol": 2,
        "Psy": 1,
        "Insecte": 1,
        "Roche": 1,
        "Spectre": 1,
        "Dragon": 0.5,
        "Ténèbres": 1,
        "Acier": 1,
        "Fée": 1
    },
    "Plante": {
        "Normal": 1,
        "Feu": 0.5,
        "Eau": 2,
        "Électrik": 1,
        "Plante": 0.5,
        "Glace": 1,
        "Combat": 1,
        "Poison": 0.5,
        "Sol": 2,
        "Vol": 0.5,
        "Psy": 1,
        "Insecte": 0.5,
        "Roche": 2,
        "Spectre": 1,
        "Dragon": 0.5,
        "Ténèbres": 1,
        "Acier": 0.5,
        "Fée": 1
    },
    "Glace": {
        "Normal": 1,
        "Feu": 0.5,
        "Eau": 0.5,
        "Électrik": 1,
        "Plante": 2,
        "Glace": 0.5,
        "Combat": 1,
        "Poison": 1,
        "Sol": 2,
        "Vol": 2,
        "Psy": 1,
        "Insecte": 1,
        "Roche": 1,
        "Spectre": 1,
        "Dragon": 2,
        "Ténèbres": 1,
        "Acier": 0.5,
        "Fée": 1
    },
    "Combat": {
        "Normal": 2,
        "Feu": 1,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 1,
        "Glace": 2,
        "Combat": 1,
        "Poison": 0.5,
        "Sol": 1,
        "Vol": 0.5,
        "Psy": 0.5,
        "Insecte": 0.5,
        "Roche": 2,
        "Spectre": 0,
        "Dragon": 1,
        "Ténèbres": 2,
        "Acier": 2,
        "Fée": 0.5
    },
    "Poison": {
        "Normal": 1,
        "Feu": 1,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 2,
        "Glace": 1,
        "Combat": 1,
        "Poison": 0.5,
        "Sol": 0.5,
        "Vol": 1,
        "Psy": 1,
        "Insecte": 1,
        "Roche": 0.5,
        "Spectre": 0.5,
        "Dragon": 1,
        "Ténèbres": 1,
        "Acier": 0,
        "Fée": 2
    },
    "Sol": {
        "Normal": 1,
        "Feu": 2,
        "Eau": 1,
        "Électrik": 2,
        "Plante": 0.5,
        "Glace": 1,
        "Combat": 1,
        "Poison": 2,
        "Sol": 1,
        "Vol": 0,
        "Psy": 1,
        "Insecte": 0.5,
        "Roche": 2,
        "Spectre": 1,
        "Dragon": 1,
        "Ténèbres": 1,
        "Acier": 2,
        "Fée": 1
    },
    "Vol": {
        "Normal": 1,
        "Feu": 1,
        "Eau": 1,
        "Électrik": 0.5,
        "Plante": 2,
        "Glace": 1,
        "Combat": 2,
        "Poison": 1,
        "Sol": 1,
        "Vol": 1,
        "Psy": 1,
        "Insecte": 2,
        "Roche": 0.5,
        "Spectre": 1,
        "Dragon": 1,
        "Ténèbres": 1,
        "Acier": 0.5,
        "Fée": 1
    },
    "Psy": {
        "Normal": 1,
        "Feu": 1,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 1,
        "Glace": 1,
        "Combat": 2,
        "Poison": 2,
        "Sol": 1,
        "Vol": 1,
        "Psy": 0.5,
        "Insecte": 1,
        "Roche": 1,
        "Spectre": 1,
        "Dragon": 1,
        "Ténèbres": 0,
        "Acier": 0.5,
        "Fée": 1
    },
    "Insecte": {
        "Normal": 1,
        "Feu": 0.5,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 2,
        "Glace": 1,
        "Combat": 0.5,
        "Poison": 0.5,
        "Sol": 1,
        "Vol": 0.5,
        "Psy": 2,
        "Insecte": 1,
        "Roche": 1,
        "Spectre": 0.5,
        "Dragon": 1,
        "Ténèbres": 2,
        "Acier": 0.5,
        "Fée": 0.5
    },
    "Roche": {
        "Normal": 1,
        "Feu": 2,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 1,
        "Glace": 2,
        "Combat": 0.5,
        "Poison": 1,
        "Sol": 0.5,
        "Vol": 2,
        "Psy": 1,
        "Insecte": 2,
        "Roche": 1,
        "Spectre": 1,
        "Dragon": 1,
        "Ténèbres": 1,
        "Acier": 0.5,
        "Fée": 1
    },
    "Spectre": {
        "Normal": 0,
        "Feu": 1,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 1,
        "Glace": 1,
        "Combat": 1,
        "Poison": 1,
        "Sol": 1,
        "Vol": 1,
        "Psy": 2,
        "Insecte": 1,
        "Roche": 1,
        "Spectre": 2,
        "Dragon": 1,
        "Ténèbres": 0.5,
        "Acier": 1,
        "Fée": 1
    },
"Fée": {
            "Normal": 1,
        "Feu": 0.5,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 1,
        "Glace": 1,
        "Combat": 2,
        "Poison": 0.5,
        "Sol": 1,
        "Vol": 1,
        "Psy": 1,
        "Insecte": 1,
        "Roche": 1,
        "Spectre": 1,
        "Dragon": 2,
        "Ténèbres": 2,
        "Acier": 0.5,
        "Fée": 1
},

    "Dragon": {
        "Normal": 1,
        "Feu": 1,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 1,
        "Glace": 1,
        "Combat": 1,
        "Poison": 1,
        "Sol": 1,
        "Vol": 1,
        "Psy": 1,
        "Insecte": 1,
        "Roche": 1,
        "Spectre": 1,
        "Dragon": 2,
        "Ténèbres": 1,
        "Acier": 0.5,
        "Fée": 0
    },
    "Ténèbres": {
        "Normal": 1,
        "Feu": 1,
        "Eau": 1,
        "Électrik": 1,
        "Plante": 1,
        "Glace": 1,
        "Combat": 0.5,
        "Poison": 1,
        "Sol": 1,
        "Vol": 1,
        "Psy": 2,
        "Insecte": 1,
        "Roche": 1,
        "Spectre": 2,
        "Dragon": 1,
        "Ténèbres": 0.5,
        "Acier": 1,
        "Fée": 0.5
    },
    "Acier": {
        "Normal": 1,
        "Feu": 0.5,
        "Eau": 0.5,
        "Électrik": 0.5,
        "Plante": 1,
        "Glace": 2,
        "Combat": 1,
        "Poison": 1,
        "Sol": 1,
        "Vol": 1,
        "Psy": 1,
        "Insecte": 1,
        "Roche": 2,
        "Spectre": 1,
        "Dragon": 1,
        "Ténèbres": 1,
        "Acier": 0.5,
        "Fée": 2
    }
}

def clean_line(line):
    # Supprimer les caractères de formatage (ex : couleurs)
    return re.sub(r'\x1b\[[0-9;]*m', '', line).strip()

def get_effectiveness(attack_type, pokemon_types):
    # Récupérer le multiplicateur de dégâts en fonction des types
    effectiveness_values = [effectiveness.get(attack_type, {}).get(pokemon_type, 1) for pokemon_type in pokemon_types]
    total_effectiveness = 1
    for value in effectiveness_values:
        total_effectiveness *= value
    return total_effectiveness

def main():
    # Connexion au service
    conn = remote('challenges.hackademint.org', 30432)
    
    while True:
        try:
            # Lire la ligne d'entrée
            line = conn.recvline().decode()
            cleaned_line = clean_line(line)
            print(f"Received line: {cleaned_line}")  # Débogage

            if 'Type de l\'attaque :' in cleaned_line:
                attack_type = cleaned_line.split(': ')[1]
                
                # Lire la ligne suivante pour obtenir le type du Pokémon
                pokemon_type_line = conn.recvline().decode()
                cleaned_pokemon_type_line = clean_line(pokemon_type_line)
                print(f"Received line: {cleaned_pokemon_type_line}")  # Débogage
                
                if 'Type du Pokémon :' in cleaned_pokemon_type_line:
                    pokemon_types = cleaned_pokemon_type_line.split(': ')[1].split('-')
                    
                    # Calculer le multiplicateur de dégâts
                    multiplier = get_effectiveness(attack_type, pokemon_types)
                    
                    # Envoyer la réponse
                    conn.sendline(f'{multiplier}')
                    
                    # Vérifiez la réponse pour des erreurs
                    response = conn.recvline().decode()
                    cleaned_response = clean_line(response)
                    print(f"Server response: {cleaned_response}")  # Débogage

                    if 'Continue !' in cleaned_response:
                        print(f"Réponse correcte : {cleaned_response}")
                    elif 'Trop lent !' in cleaned_response:
                        print("Trop lent, vous devez répondre plus vite.")
                        break
                    elif 'Resultat attendu:' in cleaned_response:
                        print(f"Erreur: {cleaned_response}")
                        break
                else:
                    print(f"Format de ligne inattendu : {cleaned_pokemon_type_line}")
            else:
                print(f"Format de ligne inattendu : {cleaned_line}")

        except EOFError:
            print("Le serveur a fermé la connexion.")
            break

    conn.close()

if __name__ == "__main__":
    main()

```