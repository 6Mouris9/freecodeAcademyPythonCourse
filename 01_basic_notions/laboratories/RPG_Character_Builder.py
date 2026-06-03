def create_character(name, strength, intelligence, charisma):
    # valida nome
    if not isinstance(name, str):
        return "The character name should be a string."
    
    if name == "":
        return "The character should have a name."
    
    if len(name) > 10:
        return "The character name is too long."
    
    if " " in name:
        return "The character name should not contain spaces."
    
    # valida stats tipo
    if not all(isinstance(stat, int) for stat in [strength, intelligence, charisma]):
        return "All stats should be integers."
    
    # valida valores mínimos
    if any(stat < 1 for stat in [strength, intelligence, charisma]):
        return "All stats should be no less than 1."
    
    # valida valores máximos
    if any(stat > 4 for stat in [strength, intelligence, charisma]):
        return "All stats should be no more than 4."
    
    # soma dos pontos
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points."
    
    # função auxiliar para gerar linha
    def build_line(label, value):
        full = "●" * value
        empty = "○" * (10 - value)
        return f"{label} {full}{empty}"
    
    # montagem final
    result = (
        f"{name}\n"
        f"{build_line('STR', strength)}\n"
        f"{build_line('INT', intelligence)}\n"
        f"{build_line('CHA', charisma)}"
    )
    
    return result

print(create_character('ren', 4, 2, 1))