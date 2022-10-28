def strip_name(name: str):
    # Prefix
    prefixes = ["M", "MI", "SM", "SKM", "T", "BP",]
    strRemove = 0
    
    try:
        splitName = name.split("_")
    except AttributeError:
        return name

    if splitName[0] in prefixes:
        strRemove = len(splitName[0]) + 1
    else:
        pass
    
    name = name[strRemove:]

    #Suffix
    try:
        splitName = name.split("_")
    except AttributeError:
        splitName = name

    suffix = []

    # Making list
    suffix_number = 20
    while suffix_number > 0:
        if suffix_number > 9:
            suffix.append(f"0{str(suffix_number)}")
            suffix.append(str(suffix_number))
        else:
            suffix.append(f"00{str(suffix_number)}")
            suffix.append(f"0{str(suffix_number)}")
            suffix.append(str(suffix_number))

        suffix_number -= 1
    
    strRemove = ""
    for x in suffix:
        if x in splitName[-1]:
            strRemove = x
            break
        else:
            pass
    
    name = name.replace(strRemove, "")
    if name[-1] == "_":
        name = name.replace(name[-1], "")
    if name[0] == "_":
        name = name.replace(name[0], "")

    return name


def main():
    names = ["M_lambert1", "MI_other_material7", "MI_thirdThing12", "M_material_Black_005", "nonNumberMat", "material_something_02"]
    namesList = {}
    
    for i, name in enumerate(names):
        namesList[strip_name(name)] = "Asset"
    
    print(namesList)


if __name__ == "__main__":
    main()