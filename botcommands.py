from math import sqrt
import random

#sheet for bot commands

#help command(explains commands/question format)


#spell - get spell data
#column organization in sheet - (Name	Level	School	Casting Time	Duration	Range	Area	Attack	Save	Damage/Effect	Ritual	Concentration	Verbal	Somatic	Material	Material*	Details)
def searchspell(spellreq, spelldata):
  om = "Apologies, I am unable to find the spell within the Archives."
  thinking = ["One second.", "Calculating.", "Give me a moment.", "Searching."]

  for spells in spelldata:
    if spells[0] == spellreq:
      om = spellreq + "?  "
      om += random.choice(thinking) + "\n---"
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
      om += "\n" + spells[16]
      om += "\n---"
      return om
  return om

#npc
#bag of holding
