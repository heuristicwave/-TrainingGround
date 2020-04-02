#  Not a loop !!!, Using Modular operation !!!
#  Rock-Scissors-Paper is similar to mod operation (0, 1, 2)

# !! Matching input characters with numbers !!
# find() can also be used instead of index()
ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())

if ML == MR and (ML+2) % 3 in [TL, TR]:
    print("TK")
elif TL == TR and (TL+2) % 3 in [ML, MR]:
    print("MS")
else:
    print('?')
