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
    suffix_number = 99
    while suffix_number > 0:
        if suffix_number > 9:
            suffix.append(f"0{str(suffix_number)}")
            suffix.append(str(suffix_number))
        else:
            suffix.append(f"00{str(suffix_number)}")
            suffix.append(f"0{str(suffix_number)}")
            suffix.append(str(suffix_number))

        suffix_number -= 1
    
    for x in suffix:
        if x in splitName[-1]:
            name = name[: len(x)*-1]
            break
        else:
            pass
    
    if name[-1] == "_":
        name = name[:-1]

    return name


print(strip_name("M_Something_interesting_050"))