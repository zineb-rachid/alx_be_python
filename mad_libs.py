adjective=input("insert an adjective:e.g big,old :")
verb=input("insert a verb:e.g saw ,run to : ")
noun=input ("insert a noun : e.g tree building : ")
if adjective=="big"  :
    ligne2=(f"and sudently i {verb} a {adjective}")
elif adjective=="old":
    ligne2=(f"and sudently i {verb} an {adjective}")
else :
     ligne2=(f"and sudently i {verb} an/a {adjective}")

story=f"""
i was walking the other day on the park 
{ligne2}
multi colered {noun} and it was very fastinating 
"""

print ("\nAnd here is your mad lib story:")
print(story)

    