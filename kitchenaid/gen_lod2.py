from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("kitchenaid_LOD2.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)


def createBox(path, x, y, z, sx, sy, sz):
    cubePrim = UsdGeom.Cube.Define(stage, path)
    cubeXform = UsdGeom.Xformable(cubePrim)
    cubeXform.AddTranslateOp().Set((x, y, z))
    cubeXform.AddScaleOp().Set((sx * 0.5, sy * 0.5, sz * 0.5))
    return cubePrim


createBox("/mixer", 0, 0, 0.175, 0.2, 0.3, 0.35)

stage.Save()
