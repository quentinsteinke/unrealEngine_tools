import unreal
import sys

@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass


def main():
    selected_assets = EditorUtils().get_selected_assets()

    name = sys.argv[1]
    print(f"Name here: {name}")


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
            
            

if __name__ == "__main__":
    main()