import random
import string

def generate_pronounceable_password(length=8):
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    password = []
    use_consonant = random.choice([True, False])

    for _ in range(length):
        if use_consonant:
            password.append(random.choice(consonants))
        else:
            password.append(random.choice(vowels))
        use_consonant = not use_consonant

    # Opcional: Adiciona um dígito no final para mais segurança
    password.append(str(random.randint(0, 9)))
    return ''.join(password)

if __name__ == "__main__":
    print("=== Gerador de Senhas Pronunciáveis ===")
    try:
        tamanho = int(input("Digite o tamanho da senha (mínimo 4): "))
        if tamanho < 4:
            print("Tamanho muito pequeno. Usando 8.")
            tamanho = 8
    except ValueError:
        print("Entrada inválida. Usando 8.")
        tamanho = 8

    senha = generate_pronounceable_password(tamanho)
    print(f"Sua senha pronunciável: {senha}")
