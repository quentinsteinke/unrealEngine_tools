import unreal


@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

def rename():
    print("renaming")


def add_prefix():
    print("adding prefix")


def apply_material():
    print("applying material")