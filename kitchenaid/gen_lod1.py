from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("kitchenaid_LOD1.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)


def createBox(path, x, y, z, sx, sy, sz):
    cubePrim = UsdGeom.Cube.Define(stage, path)
    cubeXform = UsdGeom.Xformable(cubePrim)
    cubeXform.AddTranslateOp().Set((x, y, z))
    cubeXform.AddScaleOp().Set((sx * 0.5, sy * 0.5, sz * 0.5))
    return cubePrim


def createCylinder(path, x, y, z, sx, sy, sz):
    cylPrim = UsdGeom.Cylinder.Define(stage, path)
    cylXform = UsdGeom.Xformable(cylPrim)
    cylXform.AddTranslateOp().Set((x, y, z))
    cylXform.AddScaleOp().Set((sx * 0.5, sy * 0.5, sz * 0.5))
    return cylPrim


createBox("/base", 0, 0, 0.015, 0.2, 0.3, 0.03)
createBox("/top", 0, 0, 0.3, 0.2, 0.3, 0.11)
createBox("/body", 0, 0.07, 0.15, 0.15, 0.1, 0.25)
createCylinder("/bowl", 0, -0.08, 0.13, 0.3, 0.3, 0.2)


stage.Save()
