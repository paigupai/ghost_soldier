from enum import Enum, unique

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

Category_Id = None
Folder_Name = None
#目标
#更换目标，更改此值
TARGET = Target.Makeup
#目标件数
Target_Size = 100

def setup():
    global Category_Id
    global Folder_Name
    global TARGET
    if TARGET == Target.Fashion :
        Category_Id = "2654"
        Folder_Name = "Fashion"
    elif TARGET == Target.Makeup :
        Category_Id = "1712"
        Folder_Name = "Makeup"
    elif TARGET == Target.Skincare:
        Category_Id = "1632"
        Folder_Name = "Skincare"
    elif TARGET == Target.Hair:
        Category_Id = "1671"
        Folder_Name = "Hair"
    elif TARGET == Target.Bath_Body:
        Category_Id = "1686"
        Folder_Name = "Bath_Body"
    elif TARGET == Target.Health:
        Category_Id = "1747"
        Folder_Name = "Health"
    #TODO 
        pass
    
