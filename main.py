import unreal
import sys


@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass


############## Variables ##############
selected_assets = EditorUtils().get_selected_assets()
materialList = {}
materialInstanceList = {}

# Unreal Arguments
name = str(sys.argv[1])
addName = str(sys.argv[2])
prefix = str(sys.argv[3])
addPrefix = str(sys.argv[4])
setMaterial = str(sys.argv[5])
smartApplyMaterials = str(sys.argv[6])
materialType = str(sys.argv[7])
# materialSlot = str(sys.argv[8])


############## Functoins ##############
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


def rename(n: str=None):
    for asset in selected_assets:
        if n == None:
            print(f"Name here: {asset.get_name()}")
        else:
            print(f"New name is {n}")


def add_prefix():
    for asset in selected_assets:
        print(f"addPrefix is {prefix + asset.get_name()}")


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
                matname = strip_prefix(str(matname))
                try:
                    material = get_asset_by_name(str(matname), instance)
                    print(f"found {material}")
                    asset.set_material(int(x), material)
                except KeyError:
                    unreal.log_warning(f"Material '{matname}' not found on {asset.get_full_name()}")
        

############## Main Function Loop ##############
def main():
    # Renaming Start
    if addName == "true" and addPrefix == "true":
        newname = prefix + name
        rename(newname)

    elif addName == "true":
        rename()

    elif addPrefix == "true":
        add_prefix()
    # Renaming End
    
    # Set Material
    if setMaterial == "true":
        set_material(0)
    
    # Smart Set Material
    if smartApplyMaterials == "true":
        smart_apply_materials()
            

if __name__ == "__main__":
    main()