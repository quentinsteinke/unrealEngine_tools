import unreal
import sys


@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

@unreal.uclass()
class MeshComp(unreal.MeshComponent):
    pass


############## Variables ##############
selected_assets = EditorUtils().get_selected_assets()

name = str(sys.argv[1])
addName = str(sys.argv[2])
prefix = str(sys.argv[3])
addPrefix = str(sys.argv[4])
setMaterial = str(sys.argv[5])
smartApplyMaterials = str(sys.argv[6])
# materialPath = str(sys.argv[7])


############## Functoins ##############
materialList = {}
def get_all_materials():
    asset_list = unreal.AssetRegistryHelpers.get_asset_registry().get_assets_by_class("Material")
    for asset in asset_list:
        asset_name = str(asset.asset_name)
        asset_path = str(asset.object_path)
        if asset in materialList:
            pass
        else:
            materialList[asset_name] = asset_path


def get_asset_by_name(name: str, searchList: dict):
    asset = (searchList[name])
    print(f"returning asset {unreal.load_asset(asset)}")
    return unreal.load_asset(asset)


def testing():
    for asset in selected_assets:
        if asset.get_class() == "Object":
            print(f"{asset.get_name()} is a Object")
        elif asset.get_class() == "Material":
            print(f"{asset.get_name()} is a Material")
        else:
            print(f"{asset.get_name()} is not a Material or an Object")
            print(f"It's class is type {asset}")


def rename(n: str=None):
    for asset in selected_assets:
        if n == None:
            print(f"Name here: {name}")
        else:
            print(f"New name is {n}")


def add_prefix():
    for asset in selected_assets:
        print(f"addPrefix is {prefix + asset.get_name()}")


# Get last selected asset and return it
def get_last_selected():
    last_selected = selected_assets[-1]

    return last_selected


# Apply one material to slot one of all selelcted objects
def set_material(slot):
    material = get_last_selected()

    for asset in selected_assets:
        if "StaticMesh" in str(asset.get_class()):
            print(asset.get_name())
            # Change material
            asset.set_material(int(slot), material)


# Get material slot names, find matching named materials and apply to slot
def smart_apply_materials():
    get_all_materials()
    for asset in selected_assets:
        if "StaticMesh" in str(asset.get_class()):
            sm_component = unreal.StaticMeshComponent()
            sm_component.set_static_mesh(asset)
            materialSlotNames = unreal.StaticMeshComponent.get_material_slot_names(sm_component)
            for x, matname in enumerate(materialSlotNames):
                try:
                    material = get_asset_by_name(str(matname), materialList)
                    print(f"found {material}")
                    asset.set_material(int(x), material)
                except KeyError:
                    print(f"Material '{matname}' not found on {asset.get_full_name()}")
        

############## Main Function Loop ##############
def main():
    if addName == "true" and addPrefix == "true":
        newname = prefix + name
        rename(newname)

    elif addName == "true":
        rename()

    elif addPrefix == "true":
        add_prefix()
    
    if setMaterial == "true":
        set_material(0)
    
    if smartApplyMaterials == "true":
        smart_apply_materials()
            

if __name__ == "__main__":
    main()