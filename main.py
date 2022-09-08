import unreal
import sys


@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

@unreal.uclass()
class MeshComp(unreal.MeshComponent):
    pass


selected_assets = EditorUtils().get_selected_assets()

name = str(sys.argv[1])
addName = str(sys.argv[2])
prefix = str(sys.argv[3])
addPrefix = str(sys.argv[4])
setMaterial = str(sys.argv[5])
smartApplyMaterials = str(sys.argv[6])


def testing():
    for asset in selected_assets:
        if asset.get_class() == "Object":
            print(f"{asset.get_name()} is a Object")
        elif asset.get_class() == "Material":
            print(f"{asset.get_name()} is a Material")
        else:
            print(f"{asset.get_name()} is not a Material or an Object")
            print(f"It's class is type {asset}")


def rename():
    print(f"Name here: {name}")


def add_prefix():
    print(f"addPrefix is {prefix}")


def apply_material():
    print("applying material")


# Get last selected asset and return it
def get_material():
    material = selected_assets[-1]

    return material


# Apply one material to slot one of all selelcted objects
def set_material(slot):
    material = get_material()

    for asset in selected_assets:
        if "StaticMesh" in str(asset.get_class()):
            print(asset.get_name())
            # Change material
            asset.set_material(int(slot), material)


# Get material slot names, find matching named materials and apply to slot
def smart_apply_materials():
        for asset in selected_assets:
            sm_component = unreal.StaticMeshComponent()
            sm_component.set_static_mesh(asset)
            materialSlotNames = unreal.StaticMeshComponent.get_material_slot_names(sm_component)
            for name in materialSlotNames:
                material = unreal.AssetRegistry().get_assets_by_package_name(name)
                print(material)
        

############## Main Function Loop ##############
def main():
    if addName == "true":
        rename()

    if addPrefix == "true":
        add_prefix()
    
    if setMaterial == "true":
        set_material()
    
    if smartApplyMaterials == "true":
        smart_apply_materials()
            

if __name__ == "__main__":
    main()