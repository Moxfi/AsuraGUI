#AsuraCalc ft GUI by Riku "Mox" Ketonen
#2007

from tkinter import *
import sys

#Define subkomennot
def laske():
    try: #Napataan GUI:n fieldeistä numerot
        Element = float(Entry.get(elem))
        FoLV = int(Entry.get(foskill))
        PpsLV = int(Entry.get(ppskill))
        AsuraLV = int(Entry.get(asurskill))
        WeaponATK = int(Entry.get(weapon))
        BaseATK = int(Entry.get(base))
        SP = int(Entry.get(sp))
        Cards = float(Entry.get(card))

		#Rajoitetaan "AsuraLV"
        if AsuraLV > 5 or PpsLV > 5 or FoLV > 5:
            test = Label(text = "Haxor").grid(row = 8, column = 0, sticky = W)
        
		#Koko laskurin toiminta
        else:
            Asura = ((WeaponATK + BaseATK) * (8 + SP / 10 ) + 250 \
                 + (AsuraLV * 150)) * Cards
            Entry.delete(asur, 0, 20)
            Entry.insert(asur, 0, Asura)

            AsuraN = ((WeaponATK + BaseATK) * (8 + SP / 10 ) + 250 \
                 + (AsuraLV * 150)) * 1
            Entry.delete(asurn, 0, 20)
            Entry.insert(asurn, 0, AsuraN)

            Pps = ((WeaponATK + BaseATK)*(2 + PpsLV)) * Cards * Element
            Entry.delete(ppstrike, 0, 20)
            Entry.insert(ppstrike, 0, Pps)

            PpsN = ((WeaponATK + BaseATK)*(2 + PpsLV))
            Entry.delete(ppsn, 0, 20)
            Entry.insert(ppsn, 0, PpsN)

            PpsC = ((WeaponATK + BaseATK)*(2 + PpsLV)) * Cards
            Entry.delete(ppsc, 0, 20)
            Entry.insert(ppsc, 0, PpsC)

            PpsE = ((WeaponATK + BaseATK)*(2 + PpsLV)) * Element
            Entry.delete(ppse, 0, 20)
            Entry.insert(ppse, 0, PpsE)           

            Fo = ((1.25 + (FoLV * 0.25)) * (WeaponATK + BaseATK)) * Element * Cards * FoLV
            Entry.delete(foffensive, 0, 20)
            Entry.insert(foffensive, 0, Fo)

            FoN = ((1.25 + (FoLV * 0.25)) * (WeaponATK + BaseATK))* FoLV
            Entry.delete(fon, 0, 20)
            Entry.insert(fon, 0, FoN)

            FoC = ((1.25 + (FoLV * 0.25)) * (WeaponATK + BaseATK)) * Cards *FoLV
            Entry.delete(foc, 0, 20)
            Entry.insert(foc, 0, FoC)

            FoE = ((1.25 + (FoLV * 0.25)) * (WeaponATK + BaseATK)) * Element * FoLV
            Entry.delete(foe, 0, 20)
            Entry.insert(foe, 0, FoE)

	#Exception, jos kentissä väärä arvo
    except(TypeError, ValueError):
        test = Label(text = "Error").grid(row = 10, column = 0, sticky = W)
        
def lopeta():
    root.destroy()
    sys.exit(0)

#Käyttöliittymä
#Asetetaan fieldit/tekstit/jne käyttämällä row/column arvoja
root = Tk()
root.title("Cool Champ App :3")
root.geometry("382x240")

weapontext = Label(text = " Weapon ATK").grid(row = 0, column = 0, sticky = W)
weapon = Entry(width = 10)
weapon.grid(row = 0, column = 1, sticky = W)

basetext = Label(text = " Base ATK").grid(row = 1, column = 0, sticky = W)
base = Entry(width = 10)
base.grid(row = 1, column = 1, sticky = W)

cardtext = Label(text = " Card").grid(row = 0, column = 3, sticky = W)
card = Entry(width = 10)
card.grid(row = 0, column = 4, sticky = W)

elemtext = Label(text = " Elem").grid(row = 1, column = 3, sticky = W)
elem = Entry(width = 10)
elem.grid(row = 1, column = 4, sticky = W)

sptext = Label(text = " Sp").grid(row = 0, column = 5, sticky = W)
sp = Entry(width = 10)
sp.grid(row = 0, column = 6, sticky = W)

asurskilltext = Label(text = " Asura LV").grid(row = 5, column = 0, sticky = W)
asurskill = Entry(width = 10)
asurskill.grid(row = 5, column = 1, sticky = W)

ppskilltext = Label(text = " PPS LV").grid(row = 5, column = 3, sticky = W)
ppskill = Entry(width = 10)
ppskill.grid(row = 5, column = 4, sticky = W)

foskilltext = Label(text = " TSS LV").grid(row = 5, column = 5, sticky = W)
foskill = Entry(width = 10)
foskill.grid(row = 5, column = 6, sticky = W)

#GUI:n ylareunaan kiva kuva!
Image1 = PhotoImage(file = "bannertuned.gif")
banner1 = Label(image = Image1).grid(row=6, column=0, columnspan=8, \
           sticky=W+E, padx=0, pady=0)

asurntext = Label(text = " Asura N").grid(row = 7, column = 0, sticky = W)
asurn = Entry(width = 10)
asurn.grid(row = 7, column = 1, sticky = W)

asurtext = Label(text = " Asura C").grid(row = 8, column = 0, sticky = W)
asur = Entry(width = 10)
asur.grid(row = 8, column = 1, sticky = W)

ppsntext = Label(text = " PPS N").grid(row = 7, column = 3, sticky = W)
ppsn = Entry(width = 10)
ppsn.grid(row = 7, column = 4,sticky = W)

ppsctext = Label(text = " PPS C").grid(row = 8, column = 3, sticky = W)
ppsc = Entry(width = 10)
ppsc.grid(row = 8, column = 4,sticky = W)

ppsetext = Label(text = " PPS E").grid(row = 9, column = 3, sticky = W)
ppse = Entry(width = 10)
ppse.grid(row = 9, column = 4,sticky = W)

ppstext = Label(text = " PPS EC").grid(row = 10, column = 3, sticky = W)
ppstrike = Entry(width = 10)
ppstrike.grid(row = 10, column = 4,sticky = W)

fontext = Label(text = " TSS N").grid(row = 7, column = 5, sticky = W)
fon = Entry(width = 10)
fon.grid(row = 7, column = 6,sticky = W)

foctext = Label(text = " TSS C").grid(row = 8, column = 5, sticky = W)
foc = Entry(width = 10)
foc.grid(row = 8, column = 6,sticky = W)

foe = Label(text = " TSS E").grid(row = 9, column = 5, sticky = W)
foe = Entry(width = 10)
foe.grid(row = 9, column = 6,sticky = W)

foffensivetext = Label(text = " TSS EC").grid(row = 10, column = 5, sticky = W)
foffensive = Entry(width = 10)
foffensive.grid(row = 10, column = 6,sticky = W)

#GUI:n napit
button1 = Button(text = "Calculate", command = laske, width = 10).grid(row = 13, column = 4, sticky = W)
button2 = Button(text = "Exit", command = lopeta, width = 10).grid(row = 13, column = 0, sticky = W)

#Alareunaan kiva kuva
Image2 = PhotoImage(file = "bannertuned2.gif")
banner2 = Label(image = Image2).grid(row=14, column=0, columnspan=8, \
           sticky=W+E, padx=0, pady=0)

#Start!
root.mainloop()


