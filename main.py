import unreal
import sys
import os
import csv
import math


@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass


############## Variables ##############
selected_assets = EditorUtils().get_selected_assets()
materialList = {}
materialInstanceList = {}

# Unreal Arguments #
run_command = str(sys.argv[1])

if run_command == "material":
    try:
        setMaterial = str(sys.argv[2])
        smartApplyMaterials = str(sys.argv[3])
        materialType = str(sys.argv[4])
        # materialSlot = str(sys.argv[8])
    except IndexError:
        pass


############## Functoins ##############
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
    
    
def strip_prefix(name: str):
    prefixes = ["M", "MI", "SM", "SKM", "T", "BP",]
    sliceNumber = 0
    
    try:
        splitName = name.split("_")
    except AttributeError:
        return name

    if splitName[0] in prefixes:
        sliceNumber = len(splitName[0]) + 1
    else:
        pass
    
    name = name[sliceNumber:]

    return name


def get_all_materials():
    material_asset_list = unreal.AssetRegistryHelpers.get_asset_registry().get_assets_by_class("Material")
    for asset in material_asset_list:
        asset_name = strip_prefix(str(asset.asset_name)).upper()
        asset_path = str(asset.object_path)
        if asset not in materialList: materialList[asset_name] = asset_path

    material_instance_asset_list = unreal.AssetRegistryHelpers.get_asset_registry().get_assets_by_class("MaterialInstanceConstant")
    for asset in material_instance_asset_list:
        asset_name = strip_prefix(str(asset.asset_name)).upper()
        asset_path = str(asset.object_path)
        if asset not in materialInstanceList: materialInstanceList[asset_name] = asset_path


def get_asset_by_name(name: str, searchList: dict):
    asset = (searchList[name.upper()])
    return unreal.load_asset(asset)


# def rename(n: str=None):
#     for asset in selected_assets:
#         if n == None:
#             print(f"Name here: {asset.get_name()}")
#         else:
#             print(f"New name is {n}")


# def add_prefix():
#     for asset in selected_assets:
#         print(f"addPrefix is {prefix + asset.get_name()}")


def get_last_selected():
    last_selected = selected_assets[-1]

    return last_selected


# Apply one material to given slot for all selelcted objects
def set_material(slot):
    material = get_last_selected()

    for asset in selected_assets:
        if "StaticMesh" in str(asset.get_class()):
            asset.set_material(int(slot), material)


# Get material slot names, find matching named materials and apply to slot
def smart_apply_materials():
    get_all_materials()

    if materialType == "true":
        instance = materialInstanceList
    elif materialType == "false":
        instance = materialList

    for asset in selected_assets:
        if "StaticMesh" in str(asset.get_class()):
            sm_component = unreal.StaticMeshComponent()
            sm_component.set_static_mesh(asset)
            materialSlotNames = unreal.StaticMeshComponent.get_material_slot_names(sm_component)
            for x, matname in enumerate(materialSlotNames):
                matname = strip_name(str(matname))
                try:
                    material = get_asset_by_name(str(matname), instance)
                    print(f"found {material}")
                    asset.set_material(int(x), material)
                except KeyError:
                    unreal.log_warning(f"Material '{matname}' not found on {asset.get_full_name()}")


def position_selected_actors():
    selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()
    for actor in selected_actors:
        if actor.get_class() == unreal.StaticMeshActor.static_class():
            sm = actor.static_mesh_component.static_mesh

            sm_path = sm.get_editor_property("asset_import_data").get_first_filename()
            sm_path = sm_path[:-4]
            sm_path = sm_path + ".csv"
            print(sm_path)

            with open(str(sm_path), mode="r") as data_file:
                data_reader = csv.reader(data_file, delimiter=",")
                for x, row in enumerate(data_reader):
                    if x == 0:
                        print("setting location")
                        new_location = unreal.Vector(float(row[0]), float(row[1]), float(row[2]))
                        actor.set_actor_location(new_location, False, False)
                    elif x == 1:
                        print("setting rotation")
                        # new_rotation = unreal.Rotator(float(row[0] * (180/math.pi)), float(row[1] * (180/math.pi)), float(row[2] * (180/math.pi)))
                        # print(new_rotation)
                        # actor.set_actor_rotation(new_rotation, False)
                    elif x == 2:
                        print("setting scale")
                        new_scale = unreal.Vector(float(row[0]), float(row[1]), float(row[2]))
                        actor.set_actor_scale3d(new_scale)
        # actor.set_actor_location()
        

############## Main Function Loop ##############
def main():
    # Renaming Start
    # if addName == "true" and addPrefix == "true":
    #     newname = prefix + name
    #     rename(newname)

    # elif addName == "true":
    #     rename()

    # elif addPrefix == "true":
    #     add_prefix()
    # Renaming End
    
    # Set Material
    if run_command == "material":
        if setMaterial == "true":
            set_material(0)
        
        # Smart Set Material
        if smartApplyMaterials == "true":
            smart_apply_materials()
    
    elif run_command == "position":
        position_selected_actors()
            

if __name__ == "__main__":
    main()