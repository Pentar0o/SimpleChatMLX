# MLX-Chat

Une interface de chat en ligne de commande utilisant MLX pour exécuter des modèles de langage sur Apple Silicon de manière performante et déterministe.

## À propos

MLX-Chat est un outil léger qui permet d'interagir avec des modèles de langage comme Llama 3.2 directement dans votre terminal, en tirant parti de l'accélération matérielle des puces Apple Silicon (M1/M2/M3).

Caractéristiques principales :
- Chargement optimisé des modèles via MLX
- Interface en ligne de commande simple et intuitive
- Formatage des messages compatible avec les modèles d'instruction
- Mesures de performance (vitesse de génération, nombre de tokens)
- Personnalisation du prompt système via un fichier externe

## Prérequis

- Un Mac avec puce Apple Silicon (M1, M2, M3 ou plus récent)
- Python 3.8 ou supérieur
- MLX et les dépendances nécessaires

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/votre-username/mlx-chat.git
cd mlx-chat

# Installer les dépendances
pip3 install -r requirements.txt --break-system-packages
```

Créez un fichier `requirements.txt` contenant :

```
mlx
mlx-lm
termcolor
```

## Utilisation

### Démarrage rapide

```bash
python3 chat.py
```

Par défaut, cela chargera le modèle `mlx-community/Llama-3.2-3B-Instruct-4bit` et utilisera le fichier `System_Prompt.txt` dans le répertoire courant.

### Options avancées

```bash
python3 chat.py --model "mlx-community/modèle-de-votre-choix" --system_prompt_file "chemin/vers/votre/prompt.txt"
```

Options disponibles :
- `--model` : Nom ou chemin du modèle à utiliser (par défaut : "mlx-community/Llama-3.2-3B-Instruct-4bit")
- `--system_prompt_file` : Chemin vers le fichier contenant le prompt système (par défaut : "System_Prompt.txt")

### Exemple de System_Prompt.txt

```
Tu es un assistant IA utile, honnête et inoffensif qui répond toujours de façon concise et précise.
```

## Comment ça marche

1. Le script charge le modèle et le tokenizer spécifiés
2. Il lit le fichier de prompt système
3. Il entre dans une boucle de conversation où :
   - L'utilisateur entre un message
   - Le message est formaté avec l'historique de la conversation
   - Le modèle génère une réponse
   - Des statistiques de performance sont affichées
   - La réponse est ajoutée à l'historique de conversation

Pour quitter, tapez simplement `bye`.

## Performance

Les performances dépendent du modèle utilisé et de votre matériel. À titre indicatif :

- Sur un MacBook Pro M1, le modèle Llama-3.2-3B-Instruct-4bit génère environ 30-50 tokens par seconde
- La première inférence peut prendre plus de temps en raison du chargement du modèle

## Modèles recommandés

MLX-Chat fonctionne avec tous les modèles compatibles avec MLX, notamment :

- `mlx-community/Llama-3.2-3B-Instruct-4bit` (par défaut)
- `mlx-community/Llama-3.2-1B-Instruct-4bit` (plus léger)
- `mlx-community/Llama-3.2-8B-Instruct-4bit` (plus performant)

## Limitations

- Fonctionne uniquement sur les Mac avec Apple Silicon
- La taille du modèle est limitée par la mémoire disponible sur votre appareil
- Le nombre de tokens générés est actuellement fixé à 512 maximum

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

[MIT](LICENSE)
