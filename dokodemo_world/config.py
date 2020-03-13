from enum import Enum, unique

Category_Id = None
Folder_Name = None

class Target( Enum ):
    Fashion = 0
    Makeup = 1
    Skincare = 2
    Hair = 3
    Bath_Body = 4
    Health = 5
    Kids_Family = 6
    Sports_Outdoors = 7
    Food_Drink = 8
    Home = 9
    Men = 10
    Electronics = 11
    Culture = 12

def setup(target):
    global Category_Id
    global Folder_Name
    if target == Target.Fashion :
        Category_Id = "2654"
        Folder_Name = "Fashion"
    elif target == Target.Makeup :
        Category_Id = "1712"
        Folder_Name = "Makeup"
    elif target == Target.Skincare:
        Category_Id = "1632"
        Folder_Name = "Skincare"
    elif target == Target.Hair:
        Category_Id = "1671"
        Folder_Name = "Hair"
    elif target == Target.Bath_Body:
        Category_Id = "1686"
        Folder_Name = "Bath_Body"
    elif target == Target.Health:
        Category_Id = "1747"
        Folder_Name = "Health"
    #TODO 
        pass
    
