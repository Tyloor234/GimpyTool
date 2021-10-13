import tkinter

from osrs_highscores import Highscores
from tkinter import *
from tkinter import ttk

# Define Window Properties
root = Tk()
root.title("GimpyTool v0.3")
root.iconbitmap("icons/GIM Icon.png")
root.resizable(False, False)
root.geometry("1150x300")

# Set up the grids
frame1 = tkinter.Frame(root)
frame1.grid(column=1, row=1, sticky=(N, W, E, S))
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=1)
frame1['borderwidth'] = 2
frame1['relief'] = 'ridge'

frame2 = tkinter.Frame(root)
frame2.grid(column=2, row=1, sticky=(N, W, E, S))
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=2)
frame2['borderwidth'] = 2
frame2['relief'] = 'ridge'

frame3 = tkinter.Frame(root)
frame3.grid(column=3, row=1, sticky=(N, W, E, S))
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=3)
frame3['borderwidth'] = 2
frame3['relief'] = 'ridge'

frame4 = tkinter.Frame(root)
frame4.grid(column=4, row=1, sticky=(N, W, E, S))
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=4)
frame4['borderwidth'] = 2
frame4['relief'] = 'ridge'

frame5 = tkinter.Frame(root)
frame5.grid(column=5, row=1, sticky=(N, W, E, S))
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=5)
frame5['borderwidth'] = 2
frame5['relief'] = 'ridge'

# Get list of names for lookup
names = ["Gimpy Tyler", "Gimpy Fresco", "Gimpy Hodge", "Gimpy DrCat", "Tylooor"]

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
gimpIcon = tkinter.PhotoImage(file="icons/GIM Icon.png")


# Get the list of levels from HiScores
global p1Stats, p2Stats, p3Stats, p4Stats, p5Stats

def getLevels():

    p1Stats = Highscores(names[0])
    p2Stats = Highscores(names[1])
    p3Stats = Highscores(names[2])
    p4Stats = Highscores(names[3])
    p5Stats = Highscores(names[4])

    drawLabels(p1Stats,frame1,0)
    drawLabels(p2Stats,frame2,1)
    drawLabels(p3Stats,frame3,2)
    drawLabels(p4Stats,frame4,3)
    drawLabels(p5Stats,frame5,4)


# Draws a button to query the highscores, so the program doesn't immediately grab them and hang on launch
btnFetch = ttk.Button(root, text="Fetch Scores", command=lambda: getLevels())
btnFetch.place(bordermode=OUTSIDE, height=30, width=80)


# Method to draw labels to a grid, should ideally get used 5 times without having to re-query HS
def drawLabels(person, frame, index):
    labelName = ttk.Label(frame, text=names[index])
    labelName.grid(column=2, row=2)
    labelName["compound"] = tkinter.LEFT
    labelName["image"] = gimpIcon

    lblWidth = 6

    labelAttack = ttk.Label(frame, text=person.attack.level, width=lblWidth)
    labelAttack.grid(column=1, row=3)
    labelAttack["compound"] = tkinter.LEFT
    labelAttack["image"] = attackIcon

    labelHitpoints = ttk.Label(frame, text=person.hitpoints.level, width=lblWidth)
    labelHitpoints.grid(column=2, row=3)
    labelHitpoints["compound"] = tkinter.LEFT
    labelHitpoints["image"] = hitpointsIcon

    labelMining = ttk.Label(frame, text=person.mining.level, width=lblWidth)
    labelMining.grid(column=3, row=3)
    labelMining["compound"] = tkinter.LEFT
    labelMining["image"] = miningIcon

    labelStrength = ttk.Label(frame, text=person.strength.level, width=lblWidth)
    labelStrength.grid(column=1, row=4)
    labelStrength["compound"] = tkinter.LEFT
    labelStrength["image"] = strengthIcon

    labelAgility = ttk.Label(frame, text=person.agility.level, width=lblWidth)
    labelAgility.grid(column=2, row=4)
    labelAgility["compound"] = tkinter.LEFT
    labelAgility["image"] = agilityIcon

    labelSmithing = ttk.Label(frame, text=person.smithing.level, width=lblWidth)
    labelSmithing.grid(column=3, row=4)
    labelSmithing["compound"] = tkinter.LEFT
    labelSmithing["image"] = smithingIcon

    labelDefence = ttk.Label(frame, text=person.defence.level, width=lblWidth)
    labelDefence.grid(column=1, row=5)
    labelDefence["compound"] = tkinter.LEFT
    labelDefence["image"] = defenceIcon

    labelHerblore = ttk.Label(frame, text=person.herblore.level, width=lblWidth)
    labelHerblore.grid(column=2, row=5)
    labelHerblore["compound"] = tkinter.LEFT
    labelHerblore["image"] = herbloreIcon

    labelFishing = ttk.Label(frame, text=person.fishing.level, width=lblWidth)
    labelFishing.grid(column=3, row=5)
    labelFishing["compound"] = tkinter.LEFT
    labelFishing["image"] = fishingIcon

    labelRanged = ttk.Label(frame, text=person.ranged.level, width=lblWidth)
    labelRanged.grid(column=1, row=6)
    labelRanged["compound"] = tkinter.LEFT
    labelRanged["image"] = rangedIcon

    labelThieving = ttk.Label(frame, text=person.hitpoints.level, width=lblWidth)
    labelThieving.grid(column=2, row=6)
    labelThieving["compound"] = tkinter.LEFT
    labelThieving["image"] = thievingIcon

    labelCooking = ttk.Label(frame, text=person.cooking.level, width=lblWidth)
    labelCooking.grid(column=3, row=6)
    labelCooking["compound"] = tkinter.LEFT
    labelCooking["image"] = cookingIcon

    labelPrayer = ttk.Label(frame, text=person.prayer.level, width=lblWidth)
    labelPrayer.grid(column=1, row=7)
    labelPrayer["compound"] = tkinter.LEFT
    labelPrayer["image"] = prayerIcon

    labelCrafting = ttk.Label(frame, text=person.crafting.level, width=lblWidth)
    labelCrafting.grid(column=2, row=7)
    labelCrafting["compound"] = tkinter.LEFT
    labelCrafting["image"] = craftingIcon

    labelFiremaking = ttk.Label(frame, text=person.firemaking.level, width=lblWidth)
    labelFiremaking.grid(column=3, row=7)
    labelFiremaking["compound"] = tkinter.LEFT
    labelFiremaking["image"] = firemakingIcon

    labelMagic = ttk.Label(frame, text=person.magic.level, width=lblWidth)
    labelMagic.grid(column=1, row=8)
    labelMagic["compound"] = tkinter.LEFT
    labelMagic["image"] = magicIcon

    labelFletching = ttk.Label(frame, text=person.fletching.level, width=lblWidth)
    labelFletching.grid(column=2, row=8)
    labelFletching["compound"] = tkinter.LEFT
    labelFletching["image"] = fletchingIcon

    labelWoodcutting = ttk.Label(frame, text=person.woodcutting.level, width=lblWidth)
    labelWoodcutting.grid(column=3, row=8)
    labelWoodcutting["compound"] = tkinter.LEFT
    labelWoodcutting["image"] = woodcuttingIcon

    labelRunecraft = ttk.Label(frame, text=person.runecraft.level, width=lblWidth)
    labelRunecraft.grid(column=1, row=9)
    labelRunecraft["compound"] = tkinter.LEFT
    labelRunecraft["image"] = runecraftIcon

    labelSlayer = ttk.Label(frame, text=person.slayer.level, width=lblWidth)
    labelSlayer.grid(column=2, row=9)
    labelSlayer["compound"] = tkinter.LEFT
    labelSlayer["image"] = slayerIcon

    labelFarming = ttk.Label(frame, text=person.farming.level, width=lblWidth)
    labelFarming.grid(column=3, row=9)
    labelFarming["compound"] = tkinter.LEFT
    labelFarming["image"] = farmingIcon

    labelConstruction = ttk.Label(frame, text=person.construction.level, width=lblWidth)
    labelConstruction.grid(column=1, row=10)
    labelConstruction["compound"] = tkinter.LEFT
    labelConstruction["image"] = constructionIcon

    labelHunter = ttk.Label(frame, text=person.hunter.level, width=lblWidth)
    labelHunter.grid(column=2, row=10)
    labelHunter["compound"] = tkinter.LEFT
    labelHunter["image"] = hunterIcon

    labelTotal = ttk.Label(frame, text=person.overall.level, width=lblWidth)
    labelTotal.grid(column=3, row=10)
    labelTotal["compound"] = tkinter.LEFT
    labelTotal["image"] = totalIcon

    for child in frame.winfo_children():
        child.grid_configure(padx=1, pady=1)


# Run the loop
root.mainloop()










