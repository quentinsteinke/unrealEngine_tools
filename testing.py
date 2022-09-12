dictionaryList = {}

namesList = ["MI_Material_Instance", "M_Material_02", "MS_Notsomething_Iwant_removed"]
values = ["This is a material instance", "This is just a material", "Something I don't want removed"]


def strip_prefix(name: str):
    splitName = name.split("_")
    sliceNumber = 0

    if splitName[0] == "M":
        sliceNumber = len(splitName[0]) + 1
    elif splitName[0] == "MI":
        sliceNumber = len(splitName[0]) + 1
    else:
        pass
    
    name = name[sliceNumber:]

    return name


for x, name in enumerate(namesList):
    name = strip_prefix(name)
    print(name)

def breakingout():
    this = 20
    print("something")
    if this > 1:
        return "something"
    
    print("notthis")

breakingout()

    # dictionaryList[name] = values[x]

# for i in dictionaryList:
#     print(f"{i}: {dictionaryList[i]}")