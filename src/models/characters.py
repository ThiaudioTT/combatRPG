class Character:

    # Constructor
    def __init__(self, name, health, proficiency, strength, dexterity,
                constitution, intelligence, wisdom, passive_wisdom, charisma, armor_class, initiative):
        # All the modifiers are here
        self.name = name
        self.health = health
        self.proficiency = proficiency
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.passive_wisdom = passive_wisdom
        self.charisma = charisma
        self.armor_class = armor_class
        self.initiative = initiative
