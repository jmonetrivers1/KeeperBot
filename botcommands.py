from math import sqrt
import random

#sheet for bot commands

#help command(explains commands/question format)
#for some randomization in replies
def randomreply():
  thinking = ["One second.", "Calculating.", "Give me a moment.", "Searching."]
  om = ""
  om = random.choice(thinking)
  return om

#spell - get spell data and return as string
#column organization in  google sheet - (Name	Level	School	Casting Time	Duration	Range	Area	Attack	Save	Damage/Effect	Ritual	Concentration	Verbal	Somatic	Material	Material*	Details)
def searchspell(spellreq, spelldata):
  om = "Apologies, I am unable to find the spell within the Archives."

  for spells in spelldata:
    if spells[0] == spellreq:
      om = spellreq + "?  "
      om += randomreply() + "\n---\n"
      if spells[1] == "0":
        om += "Cantrip"
      else:
        om += "Spell Level: " + spells[1]
      om += "\n" + spells[3]
      if spells[10] != "":
        om += "     (Ritual)"
      om += "\nRange: " + spells[5]
      if spells[11] != "":
        om += "\nConcentration: Y"
      else:
        om += "\nConcentration: N"  
      om += "\nComponents: "
      if spells[12] != "":
        om += "V"
      if spells[13] != "":
        om += "S"
      if spells[14] != "":
        om += "M"
        if spells[15]!= "":
          om += " (" +spells[15]+")"
          om.replace("((","(") # replace dup parenthesis from google sheet.data
          om.replace("))",")")

      om += "\nDuration: " + spells[4]
      om += "\nDamage/Effect: " + spells[9]
      om += "\nSchool: " + spells[2]
      if spells[6] != "":
        om += "\nArea: "+spells[6]
      if spells[7] != "":
        om += "\nAttack: "+spells[7] + " Attack"
      if spells[8] != "":
        om += "\nSave: "+spells[8]
      om += "\n/n" + spells[16]
      om += "\n---"
      return om
  return om



  
#function to calculate hypotenuse distance (for elevated combat)
def calchyp(temp):
  temp = temp.split()
  answer = ""
  if len(temp) != 3:
    answer ="I've been asked refuse non-offical requests.\nIf you wish to request hypotenuse calculations, the correct request is '!hyp height(int) verticalDistance(int)' ."  
    return answer
  a = int(temp[1])
  b = int(temp[2])
  c = sqrt(a**2 + b**2) 
  answer = "The hypotenuse? " + randomreply() + "...\nApproxiamtely " + str(int(c)) + " feet."   
  return answer

#function to calculate spell same damage (full, halved, quartered, eigthed)
def calcdmg(temp):
  temp = temp.split()
  answer = ""
  if len(temp) != 2:
    answer = "Improper requests are automatically denied.\nIf you wish to request save damage calculations, the correct request is '!dmg damage(int)' ."
    return answer
  damage = int(temp[1])
  half= int(damage/2)
  quarter = int(damage/4)
  eight = int(damage/8)
  answer = "A save based spell? " + randomreply() + "\nDamage:"  + str(damage) + "\tHalved: " + str(half) + "\tA Quarter: " + str(quarter) + "\tAn Eighth: " + str(eight)
  return answer
#npc
#bag of holding
