import tkinter

from osrs_highscores import Highscores
from tkinter import *
from tkinter import ttk

# Define Window Properties
root = Tk()
root.title("GimpyTool v0.1")
root.iconbitmap("icons/GIM Icon.png")
root.resizable(False, False)
root.geometry("1280x720")

# Set up the grids
frame1 = ttk.Frame(root, width=240, height=700)
frame1.grid(column=1, row=0, sticky=(N, W, E, S))
frame1.pack(fill="both", expand=True, padx=10, pady=10)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Get list of names for lookup
names = ["Gimpy Tyler", "Tylooor", "Gimpy Fresco", "Gimpy Hodge", "Gimpy DrCat"]

# Define all skill icons
attackIcon = tkinter.PhotoImage(file="icons/Attack_icon.png")
hitpointsIcon = tkinter.PhotoImage(file="icons/Hitpoints_icon.png")
miningIcon = tkinter.PhotoImage(file="icons/Mining_icon.png")
strengthIcon = tkinter.PhotoImage(file="icons/Strength_icon.png")
agilityIcon = tkinter.PhotoImage(file="icons/Agility_icon.png")
smithingIcon = tkinter.PhotoImage(file="icons/Smithing_icon.png")
defenceIcon = tkinter.PhotoImage(file="icons/Defence_icon.png")
herbloreIcon = tkinter.PhotoImage(file="icons/Herblore_icon.png")
fishingIcon = tkinter.PhotoImage(file="icons/Fishing_icon.png")
rangedIcon = tkinter.PhotoImage(file="icons/Ranged_icon.png")
thievingIcon = tkinter.PhotoImage(file="icons/Thieving_icon.png")
cookingIcon = tkinter.PhotoImage(file="icons/Cooking_icon.png")
prayerIcon = tkinter.PhotoImage(file="icons/Prayer_icon.png")
craftingIcon = tkinter.PhotoImage(file="icons/Crafting_icon.png")
firemakingIcon = tkinter.PhotoImage(file="icons/Firemaking_icon.png")
magicIcon = tkinter.PhotoImage(file="icons/Magic_icon.png")
fletchingIcon = tkinter.PhotoImage(file="icons/Fletching_icon.png")
woodcuttingIcon = tkinter.PhotoImage(file="icons/Woodcutting_icon.png")
runecraftIcon = tkinter.PhotoImage(file="icons/Runecraft_icon.png")
slayerIcon = tkinter.PhotoImage(file="icons/Slayer_icon.png")
farmingIcon = tkinter.PhotoImage(file="icons/Farming_icon.png")
constructionIcon = tkinter.PhotoImage(file="icons/Construction_icon.png")
hunterIcon = tkinter.PhotoImage(file="icons/Hunter_icon.png")
totalIcon = tkinter.PhotoImage(file="icons/Skills_icon.png")


# Get the list of levels from HiScores

global p1Stats, p2Stats, p3Stats, p4Stats, p5Stats

def getLevels():

    p1Stats = Highscores(names[0])
    p2Stats = Highscores(names[1])
    p3Stats = Highscores(names[2])
    p4Stats = Highscores(names[3])
    p5Stats = Highscores(names[4])

    drawLabels(p1Stats)


# Draws a button to query the highscores, so the program doesn't immediately grab them and hang on launch
btnFetch = ttk.Button(frame1, text="Fetch Scores", command=lambda: getLevels())
btnFetch.grid(column=1, row=1)


# Method to draw labels to a grid, should ideally get used 5 times without having to re-query HS
def drawLabels(person):
    labelName1 = ttk.Label(frame1, text=names[0])
    labelName1.grid(column=2, row=2)

    labelAttack1 = ttk.Label(frame1, text=person.attack.level)
    labelAttack1.grid(column=1, row=3)
    labelAttack1["compound"] = tkinter.LEFT
    labelAttack1["image"] = attackIcon

    labelHitpoints1 = ttk.Label(frame1, text=person.hitpoints.level)
    labelHitpoints1.grid(column=2, row=3)
    labelHitpoints1["compound"] = tkinter.LEFT
    labelHitpoints1["image"] = hitpointsIcon

    labelMining1 = ttk.Label(frame1, text=person.mining.level)
    labelMining1.grid(column=3, row=3)
    labelMining1["compound"] = tkinter.LEFT
    labelMining1["image"] = miningIcon

    labelStrength1 = ttk.Label(frame1, text=person.strength.level)
    labelStrength1.grid(column=1, row=4)
    labelStrength1["compound"] = tkinter.LEFT
    labelStrength1["image"] = strengthIcon

    labelAgility1 = ttk.Label(frame1, text=person.agility.level)
    labelAgility1.grid(column=2, row=4)
    labelAgility1["compound"] = tkinter.LEFT
    labelAgility1["image"] = agilityIcon

    labelSmithing1 = ttk.Label(frame1, text=person.smithing.level)
    labelSmithing1.grid(column=3, row=4)
    labelSmithing1["compound"] = tkinter.LEFT
    labelSmithing1["image"] = smithingIcon

    labelDefence1 = ttk.Label(frame1, text=person.defence.level)
    labelDefence1.grid(column=1, row=5)
    labelDefence1["compound"] = tkinter.LEFT
    labelDefence1["image"] = defenceIcon

    labelHerblore1 = ttk.Label(frame1, text=person.herblore.level)
    labelHerblore1.grid(column=2, row=5)
    labelHerblore1["compound"] = tkinter.LEFT
    labelHerblore1["image"] = herbloreIcon

    labelFishing1 = ttk.Label(frame1, text=person.fishing.level)
    labelFishing1.grid(column=3, row=5)
    labelFishing1["compound"] = tkinter.LEFT
    labelFishing1["image"] = fishingIcon

    labelRanged1 = ttk.Label(frame1, text=person.ranged.level)
    labelRanged1.grid(column=1, row=6)
    labelRanged1["compound"] = tkinter.LEFT
    labelRanged1["image"] = rangedIcon

    labelThieving1 = ttk.Label(frame1, text=person.hitpoints.level)
    labelThieving1.grid(column=2, row=6)
    labelThieving1["compound"] = tkinter.LEFT
    labelThieving1["image"] = thievingIcon

    labelCooking1 = ttk.Label(frame1, text=person.cooking.level)
    labelCooking1.grid(column=3, row=6)
    labelCooking1["compound"] = tkinter.LEFT
    labelCooking1["image"] = cookingIcon

    labelPrayer1 = ttk.Label(frame1, text=person.prayer.level)
    labelPrayer1.grid(column=1, row=7)
    labelPrayer1["compound"] = tkinter.LEFT
    labelPrayer1["image"] = prayerIcon

    labelCrafting1 = ttk.Label(frame1, text=person.crafting.level)
    labelCrafting1.grid(column=2, row=7)
    labelCrafting1["compound"] = tkinter.LEFT
    labelCrafting1["image"] = craftingIcon

    labelFiremaking1 = ttk.Label(frame1, text=person.firemaking.level)
    labelFiremaking1.grid(column=3, row=7)
    labelFiremaking1["compound"] = tkinter.LEFT
    labelFiremaking1["image"] = firemakingIcon

    labelMagic1 = ttk.Label(frame1, text=person.magic.level)
    labelMagic1.grid(column=1, row=8)
    labelMagic1["compound"] = tkinter.LEFT
    labelMagic1["image"] = magicIcon

    labelFletching1 = ttk.Label(frame1, text=person.fletching.level)
    labelFletching1.grid(column=2, row=8)
    labelFletching1["compound"] = tkinter.LEFT
    labelFletching1["image"] = fletchingIcon

    labelWoodcutting1 = ttk.Label(frame1, text=person.woodcutting.level)
    labelWoodcutting1.grid(column=3, row=8)
    labelWoodcutting1["compound"] = tkinter.LEFT
    labelWoodcutting1["image"] = woodcuttingIcon

    labelRunecraft1 = ttk.Label(frame1, text=person.runecraft.level)
    labelRunecraft1.grid(column=1, row=9)
    labelRunecraft1["compound"] = tkinter.LEFT
    labelRunecraft1["image"] = runecraftIcon

    labelSlayer1 = ttk.Label(frame1, text=person.slayer.level)
    labelSlayer1.grid(column=2, row=9)
    labelSlayer1["compound"] = tkinter.LEFT
    labelSlayer1["image"] = slayerIcon

    labelFarming1 = ttk.Label(frame1, text=person.farming.level)
    labelFarming1.grid(column=3, row=9)
    labelFarming1["compound"] = tkinter.LEFT
    labelFarming1["image"] = farmingIcon

    labelConstruction1 = ttk.Label(frame1, text=person.construction.level)
    labelConstruction1.grid(column=1, row=10)
    labelConstruction1["compound"] = tkinter.LEFT
    labelConstruction1["image"] = constructionIcon

    labelHunter1 = ttk.Label(frame1, text=person.hunter.level)
    labelHunter1.grid(column=2, row=10)
    labelHunter1["compound"] = tkinter.LEFT
    labelHunter1["image"] = hunterIcon

    labelTotal1 = ttk.Label(frame1, text=person.overall.level)
    labelTotal1.grid(column=3, row=10)
    labelTotal1["compound"] = tkinter.LEFT
    labelTotal1["image"] = totalIcon


# Run the loop
root.mainloop()










