import argparse
from termcolor import colored
from mlx_lm import generate, load
import time

# Chargement minimal du modèle avec MLX
def load_model_and_tokenizer(model_name: str):
    print(colored("🔄 Chargement du modèle et du tokenizer (MLX)...", "yellow"))
    model, tokenizer = load(model_name)
    return tokenizer, model

# Reprise exacte de ta fonction de formatage du prompt
def format_messages(system_prompt: str, messages: list) -> str:
    prompt = f"<|system|>\n{system_prompt}\n"
    for msg in messages:
        if msg["role"] == "user":
            prompt += f"<|user|>\n{msg['content']}\n"
        else:
            prompt += f"<|assistant|>\n{msg['content']}\n"
    prompt += "<|assistant|>\n"
    return prompt

# Génération avec MLX
def generate_response(tokenizer, model, prompt: str):
    start = time.time()

    response = generate(model, tokenizer, prompt=prompt, max_tokens=512, verbose=False)

    duration_s = time.time() - start

    print(colored(response.strip(), "blue"))
    nb_tokens = len(tokenizer.encode(response))
    speed_tps = nb_tokens / duration_s if duration_s > 0 else 0.0

    return response.strip(), nb_tokens, duration_s, speed_tps

# Boucle principale inchangée
def main(model_name, system_prompt_file):
    tokenizer, model = load_model_and_tokenizer(model_name)
    with open(system_prompt_file, 'r') as f:
        system_prompt = f.read().strip()

    messages = []

    while True:
        user_input = input(colored("Vous : ", "green"))
        if user_input.lower() == 'bye':
            break

        messages.append({"role": "user", "content": user_input})

        full_prompt = format_messages(system_prompt, messages)
        response, nb_tokens, duration_s, speed_tps = generate_response(tokenizer, model, full_prompt)

        print(colored(f"\nNombre de tokens générés : {nb_tokens}", "yellow"))
        print(colored(f"Temps de génération      : {duration_s:.2f} s", "yellow"))
        print(colored(f"Vitesse                  : {speed_tps:.2f} tokens/s\n", "yellow"))

        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat déterministe avec MLX sur Apple Silicon.")
    parser.add_argument("--model", type=str, default="mlx-community/Llama-3.2-3B-Instruct-4bit", help="Nom du modèle à utiliser")
    parser.add_argument("--system_prompt_file", type=str, default="System_Prompt.txt", help="Chemin vers le fichier du prompt système.")

    args = parser.parse_args()
    main(args.model, args.system_prompt_file)
