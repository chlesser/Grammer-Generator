import random
def generate_dragon_name():
    Nouns = [("Hel", "Hell"), ("Drol", "Dragon"), ("Eli", "Elf"), ("Gol", "Giant"), ("Rol", "Thing"), ("Tal", "Hilt"), ("Tel", "Fist"), 
    ("Hul", "Home"), ("Nil", "Night"), ("Sil", "Sleep"), ("Ful", "Force"),
    ("Hal", "Hate"), ("Mel", "Mercy"), ("Etil", "Eternity"), ("Skil", "Sky"),
    ("Bural", "Barrier"), ("Fil", "Fire"), ("Korl", "Knowledge"), ("Val", "Valley")]
    SuffixNouns = [("Hel", "Hell"), ("Gol", "Giants"),("Tel", "Fists"), 
    ("Hul", "Homes"), ("Nil", "Nights"), ("Sil", "Sleep"), ("Ful", "Force"),
    ("Hal", "Hate"), ("Mel", "Mercy"), ("Etil", "Eternity"), ("Skil", "Sky"),
    ("Bural", "Barriers"), ("Fil", "Fire"), ("Korl", "Knowledge"), ("Val", "Valleys")]
    AdjSuffixes = [("Vesh", "Terrible"), ("Vash", "Great"), ("Prish", "First"), ("Fesh", "False"), ("Thash", "Thankful"), ("Stosh", "Stone"), ("Nash", "Near"), ("Kash", "Quick"), ("Wesh", "Western")]
    AdvSuffixes = [("Duth", "Dies"), ("Kruth", "Kills"),("Thoth", "Burns"), ("Veyth", "Lives"), ("Casth", "Crushes"), ("Gavth", "Gives"), ("Feth", "Fails"), ("Fasth", "Falls"), ("Kosth", "Knows"), ("Troth", "Thinks"), ("Droth", "Desires"), ("Hovth", "Helps"), ("Krosth", "Stands"), ("Foth", "Feeds")]
    for i in range(5):
        nucleus = ""
        nucleusTranslation = ""
        nameSuffix = ""
        nameSuffixTranslation = ""
        fullName = ""
        fullNameTranslation = ""

        # Generates the noun
        randInt = random.randint(0, len(Nouns)-1)
        nucleus= Nouns[randInt][0]
        nucleusTranslation = Nouns[randInt][1]
        
        # Generates the suffix/prefix
        switch = random.randint(0, len(Nouns) + len(AdjSuffixes) + len(AdvSuffixes) -3)
        if(switch < len(Nouns)):
            randInt = random.randint(0, len(SuffixNouns)-1)
            nameSuffix= SuffixNouns[randInt][0]
            nameSuffixTranslation = SuffixNouns[randInt][1]
            fullName = nucleus + "'" + nameSuffix
            fullNameTranslation = "The " + nucleusTranslation + " of " + nameSuffixTranslation
        elif(switch < len(Nouns) + len(AdjSuffixes)):
            randInt = random.randint(0, len(AdjSuffixes)-1)
            nameSuffix = AdjSuffixes[randInt][0]
            nameSuffixTranslation = AdjSuffixes[randInt][1]
            fullName = nucleus + "'" + nameSuffix
            fullNameTranslation = "The " + nameSuffixTranslation + " " + nucleusTranslation
        else:
            randInt = random.randint(0, len(AdvSuffixes)-1)
            nameSuffix = AdvSuffixes[randInt][0]
            nameSuffixTranslation = AdvSuffixes[randInt][1]
            fullName = nucleus + "'" + nameSuffix
            fullNameTranslation = "The " + nucleusTranslation + " that " + nameSuffixTranslation
        
        print(fullName + ", " + fullNameTranslation)
    getInput()

def generate_hobgoblin_name():
    FFirstHalf = ["Gra", "Bra", "Glo", "Dro", "Tho", "Kra", "Sha", "Pla", "Cla", "Fra", "Za", "Da", "Haf"]
    SSecondHalf = ["gor", "mot", "han", "ruk", "zan", "lok", "dur", "fen", "gar", "tor", "mir", "nok", "vak"]
    LFirstHalf = ["Steel", "Iron", "Stone", "Dark", "Fire", "Blood", "Shadow", "Storm", "Beast", "Bear", "Fang", "Grim", "Ash"]
    LSecondHalf = ["helm", "bane", "strike", "fang", "claw", "heart", "foot", "blade", "hide", "tooth", "back", "eye", "fist"]
    for i in range(5):
        firstprimary = ""
        firstsecondary = ""
        secondprimary = ""
        secondsecondary = ""
        fullName = ""

        # Generates the names
        firstprimary = FFirstHalf[random.randint(0, len(FFirstHalf)-1)]
        firstsecondary = SSecondHalf[random.randint(0, len(SSecondHalf)-1)]
        secondprimary = LFirstHalf[random.randint(0, len(LFirstHalf)-1)]
        secondsecondary = LSecondHalf[random.randint(0, len(LSecondHalf)-1)]

        fullName = firstprimary + firstsecondary + " " + secondprimary + secondsecondary
        print(fullName)
    getInput()
def generate_elf_name():
    FFirstHalf = ["Gala", "Baye", "Liro", "Reya", "Yala", "Wela", "Gawe", "Owa", "Vela"]
    SSecondHalf = ["no", "wo", "se", "ro", "lo", "la", "-", "'", "ro"]
    SThirdHalf = ["el", "pol", "raw","vor", "ma", "dow", "li", "jis", "gon", "'ond"]
    LFirstHalf = ["Awen", "Prun", "Lar", "Wyur", "Qway", "Lea", "Pral", "Wyst", "Hiy"]
    LSecondHalf = ["el", "pol", "raw","vor", "ma", "dow", "li", "jis", "gon", "'ond"]
    for i in range(5):
        firstprimary = ""
        firstsecondary = ""
        secondprimary = ""
        secondsecondary = ""
        fullName = ""

        # Generates the names
        firstprimary = FFirstHalf[random.randint(0, len(FFirstHalf)-1)]
        firstsecondary = SSecondHalf[random.randint(0, len(SSecondHalf)-1)]
        firsttertiary = SThirdHalf[random.randint(0, len(SThirdHalf)-1)]
        secondprimary = LFirstHalf[random.randint(0, len(LFirstHalf)-1)]
        secondsecondary = LSecondHalf[random.randint(0, len(LSecondHalf)-1)]

        fullName = firstprimary + firstsecondary + firsttertiary + " " + secondprimary + secondsecondary
        print(fullName)
    getInput()

def getInput():
    print("1. Dragon, 2. Hobgoblin, 3. Elf")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        generate_dragon_name()
    elif choice == '2':
        generate_hobgoblin_name()
    elif choice == '3':
        generate_elf_name()
    else:
        print("Invalid choice.")
        getInput()
def main():
    print("Welcome to the Custom Fantasy Name Generator! This tool creates names for the world of Torr.")
    print("What kind of name would you like to generate? Type just 1 letter.")
    getInput()
main()