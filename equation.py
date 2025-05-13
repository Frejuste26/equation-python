from math import *
from fractions import Fraction

def pgcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def fraction_str(num, den):
    if den == 0:
        raise ValueError("Le dénominateur ne peut pas être nul")
    # Conversion des nombres flottants en entiers
    num = int(num) if num.is_integer() else num
    den = int(den) if den.is_integer() else den
    if den < 0:
        num, den = -num, -den
    if num == 0:
        return "0"
    
    d = pgcd(int(num), int(den))
    num, den = int(num) // d, int(den) // d
    
    if den == 1:
        return str(num)
    return f"{num}/{den}"

def print_separator():
    print("="*50)

def print_header(text):
    print_separator()
    print(f"{text:^50}")
    print_separator()

print_header("RÉSOLUTION D'ÉQUATION DU SECOND DEGRÉ")
print("\nForme: ax² + bx + c = 0\n")

try:
    a = float(input("Saisir le coefficient a: "))
    b = float(input("Saisir le coefficient b: "))
    c = float(input("Saisir le coefficient c: "))

    print_header("Résolution de l'équation")
    equation = ""
    if a != 0:
        equation += f"{a:g}x²"
    if b != 0:
        equation += f" {'+' if b > 0 else '-'} {abs(b):g}x"
    if c != 0:
        equation += f" {'+' if c > 0 else '-'} {abs(c):g}"
    equation += " = 0"
    print(f"\n(Eq): {equation}\n")

    if a == 0:
        if b == 0:
            if c == 0:
                print_header("RÉSULTAT")
                print("L'équation est une identité : tous les nombres réels sont solutions.")
            else:
                print_header("RÉSULTAT")
                print("L'équation n'admet pas de solution car", c, "≠ 0")
        else:
            print_header("RÉSULTAT")
            print("L'équation est du premier degré.")
            print(f"\nSolution: x = {fraction_str(-c, b)}")
    else:
        # Calcul du discriminant avec des nombres entiers
        num_delta = int(b**2 - 4*a*c)
        print_header("CALCUL DU DISCRIMINANT")
        print(f"Δ = {fraction_str(num_delta, 1)}")

        print_header("RÉSULTAT")
        if num_delta < 0:
            print("Le discriminant est négatif.")
            print("L'équation n'admet pas de solution réelle.")
        elif num_delta == 0:
            print("Le discriminant est nul.")
            print("L'équation admet une solution double:")
            print(f"\nx = {fraction_str(-b, 2*a)}")
        else:
            # Calcul de la racine carrée du discriminant
            racine_delta = int(sqrt(num_delta))
            print("Le discriminant est positif.")
            print("L'équation admet deux solutions distinctes:")
            print(f"\nx₁ = {fraction_str(-b + racine_delta, 2*a)}")
            print(f"x₂ = {fraction_str(-b - racine_delta, 2*a)}")

except ValueError:
    print_header("ERREUR")
    print("Veuillez entrer des nombres valides.")
except Exception as e:
    print_header("ERREUR")
    print(f"Une erreur inattendue s'est produite: {str(e)}")

 