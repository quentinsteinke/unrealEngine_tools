import unreal
import sys
from utils import rename, apply_material, add_prefix

@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

def testing():
    selected_assets = EditorUtils().get_selected_assets()

    for asset in selected_assets:
        if asset.get_class() == "Object":
            print("-------------------------------")
            print(f"{asset.get_name()} is a Object")
            print("-------------------------------")
        elif asset.get_class() == "Material":
            print("-------------------------------")
            print(f"{asset.get_name()} is a Material")
            print("-------------------------------")
        else:
            print("-------------------------------")
            print(f"{asset.get_name()} is not a Material or an Object")
            print(f"It's class is type {asset}")
            print("-------------------------------")



def main():
    name = str(sys.argv[1])
    addName = str(sys.argv[2])
    prefix = str(sys.argv[3])
    addPrefix = str(sys.argv[4])

    if addName == "true":
        print(f"Name here: {name}")

    if prefix == "true":
        print(f"addPrefix is {addPrefix}")
            

if __name__ == "__main__":
    main()