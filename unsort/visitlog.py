# Visit 2.11.0 log file
ScriptVersion = "2.11.0"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
visit.ShowAllWindows()
OpenDatabase("fldDat.vti", 0)
# The UpdateDBPluginInfo RPC is not supported in the VisIt module so it will not be logged.
metadata = GetMetaData("fldDat.vti", -1)
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("dBz", "(2.671608e-01)*B[2]")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("dBz", "(2.671608e-01)*B[2]")
DefineVectorExpression("VecCut", "{-xRe,-yRe,-zRe}")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("dBz", "(2.671608e-01)*B[2]")
DefineVectorExpression("VecCut", "{-xRe,-yRe,-zRe}")
DefineScalarExpression("Bx", "eBx+dBx")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("dBz", "(2.671608e-01)*B[2]")
DefineVectorExpression("VecCut", "{-xRe,-yRe,-zRe}")
DefineScalarExpression("Bx", "eBx+dBx")
DefineScalarExpression("By", "eBy+dBy")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("dBz", "(2.671608e-01)*B[2]")
DefineVectorExpression("VecCut", "{-xRe,-yRe,-zRe}")
DefineScalarExpression("Bx", "eBx+dBx")
DefineScalarExpression("By", "eBy+dBy")
DefineScalarExpression("Bz", "eBz+dBz")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("dBz", "(2.671608e-01)*B[2]")
DefineVectorExpression("VecCut", "{-xRe,-yRe,-zRe}")
DefineScalarExpression("Bx", "eBx+dBx")
DefineScalarExpression("By", "eBy+dBy")
DefineScalarExpression("Bz", "eBz+dBz")
DefineVectorExpression("Bfld", "if( ge(RadAll,2.2), {Bx,By,Bz} , VecCut )")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("dBz", "(2.671608e-01)*B[2]")
DefineVectorExpression("VecCut", "{-xRe,-yRe,-zRe}")
DefineScalarExpression("Bx", "eBx+dBx")
DefineScalarExpression("By", "eBy+dBy")
DefineScalarExpression("Bz", "eBz+dBz")
DefineVectorExpression("Bfld", "if( ge(RadAll,2.2), {Bx,By,Bz} , VecCut )")
DefineScalarExpression("Bmag", "sqrt(Bx*Bx+By*By+Bz*Bz)")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("dBz", "(2.671608e-01)*B[2]")
DefineVectorExpression("VecCut", "{-xRe,-yRe,-zRe}")
DefineScalarExpression("Bx", "eBx+dBx")
DefineScalarExpression("By", "eBy+dBy")
DefineScalarExpression("Bz", "eBz+dBz")
DefineVectorExpression("Bfld", "if( ge(RadAll,2.2), {Bx,By,Bz} , VecCut )")
DefineScalarExpression("Bmag", "sqrt(Bx*Bx+By*By+Bz*Bz)")
DefineVectorExpression("Efld", "(8.009213e+12)*E")
DefineScalarExpression("RadAll", "polar_radius(mesh)")
DefineScalarExpression("Radius", "if( ge(RadAll, 2.1), RadAll, 2.1)")
DefineScalarExpression("xRe", "coord(mesh)[0]")
DefineScalarExpression("yRe", "coord(mesh)[1]")
DefineScalarExpression("zRe", "coord(mesh)[2]")
DefineScalarExpression("rm5", "Radius^(-5.0)")
DefineScalarExpression("eBx", "3*xRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBy", "3*yRe*zRe*(-3.110000e+04)*rm5")
DefineScalarExpression("eBz", "(3.0*zRe*zRe - Radius*Radius)*(-3.110000e+04)*rm5")
DefineScalarExpression("dBx", "(2.671608e-01)*B[0]")
DefineScalarExpression("dBy", "(2.671608e-01)*B[1]")
DefineScalarExpression("dBz", "(2.671608e-01)*B[2]")
DefineVectorExpression("VecCut", "{-xRe,-yRe,-zRe}")
DefineScalarExpression("Bx", "eBx+dBx")
DefineScalarExpression("By", "eBy+dBy")
DefineScalarExpression("Bz", "eBz+dBz")
DefineVectorExpression("Bfld", "if( ge(RadAll,2.2), {Bx,By,Bz} , VecCut )")
DefineScalarExpression("Bmag", "sqrt(Bx*Bx+By*By+Bz*Bz)")
DefineVectorExpression("Efld", "(8.009213e+12)*E")
DefineVectorExpression("V", "if( ge(Bmag,1.0e-8), (4.698903e+01)*cross(Efld,Bfld)/dot(Bfld,Bfld) , {0,0,0} )")
SetWindowArea(1200, 1024 ,0, 0)
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 1
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis [Re]"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 1
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis [Re]"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 0
AnnotationAtts.axes3D.xAxis.title.visible = 0
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 0
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 0
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
SetAnimationTimeout(1)
ActivateDatabase("fldDat.vti")
AddPlot("Pseudocolor", "dBz", 1, 1)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
PseudocolorAtts.minFlag = 1
PseudocolorAtts.min = -25
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = 25
PseudocolorAtts.centering = PseudocolorAtts.Zonal  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "RdGy"
PseudocolorAtts.invertColorTable = 1
PseudocolorAtts.opacityType = PseudocolorAtts.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 0.75
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 4
PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeResolution = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.tubeRadiusVarEnabled = 0
PseudocolorAtts.tubeRadiusVar = ""
PseudocolorAtts.tubeRadiusVarRatio = 10
PseudocolorAtts.endPointType = PseudocolorAtts.None  # None, Heads, Tails, Both
PseudocolorAtts.endPointStyle = PseudocolorAtts.Spheres  # Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 0.125
PseudocolorAtts.endPointRadiusBBox = 0.05
PseudocolorAtts.endPointResolution = 10
PseudocolorAtts.endPointRatio = 5
PseudocolorAtts.endPointRadiusVarEnabled = 0
PseudocolorAtts.endPointRadiusVar = ""
PseudocolorAtts.endPointRadiusVarRatio = 10
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 1
PseudocolorAtts.lightingFlag = 0
PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
PseudocolorAtts.pointColor = (0, 0, 0, 0)
SetPlotOptions(PseudocolorAtts)
AddOperator("Slice", 1)
SliceAtts = SliceAttributes()
SliceAtts.originType = SliceAtts.Percent  # Point, Intercept, Percent, Zone, Node
SliceAtts.originPoint = (0, 0, 0)
SliceAtts.originIntercept = 0
SliceAtts.originPercent = 50
SliceAtts.originZone = 0
SliceAtts.originNode = 0
SliceAtts.normal = (0, 0, 1)
SliceAtts.axisType = SliceAtts.ZAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
SliceAtts.upAxis = (0, 1, 0)
SliceAtts.project2d = 0
SliceAtts.interactive = 1
SliceAtts.flip = 0
SliceAtts.originZoneDomain = 0
SliceAtts.originNodeDomain = 0
SliceAtts.meshName = "mesh"
SliceAtts.theta = 0
SliceAtts.phi = 90
SetOperatorOptions(SliceAtts, 1)
ActivateDatabase("fldDat.vti")
AddPlot("Pseudocolor", "dBz", 1, 1)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
PseudocolorAtts.minFlag = 1
PseudocolorAtts.min = -25
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = 25
PseudocolorAtts.centering = PseudocolorAtts.Zonal  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "RdGy"
PseudocolorAtts.invertColorTable = 1
PseudocolorAtts.opacityType = PseudocolorAtts.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 0.25
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 4
PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeResolution = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.tubeRadiusVarEnabled = 0
PseudocolorAtts.tubeRadiusVar = ""
PseudocolorAtts.tubeRadiusVarRatio = 10
PseudocolorAtts.endPointType = PseudocolorAtts.None  # None, Heads, Tails, Both
PseudocolorAtts.endPointStyle = PseudocolorAtts.Spheres  # Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 0.125
PseudocolorAtts.endPointRadiusBBox = 0.05
PseudocolorAtts.endPointResolution = 10
PseudocolorAtts.endPointRatio = 5
PseudocolorAtts.endPointRadiusVarEnabled = 0
PseudocolorAtts.endPointRadiusVar = ""
PseudocolorAtts.endPointRadiusVarRatio = 10
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 0
PseudocolorAtts.lightingFlag = 0
PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
PseudocolorAtts.pointColor = (0, 0, 0, 0)
SetPlotOptions(PseudocolorAtts)
AddOperator("Slice", 1)
SliceAtts = SliceAttributes()
SliceAtts.originType = SliceAtts.Percent  # Point, Intercept, Percent, Zone, Node
SliceAtts.originPoint = (0, 0, 0)
SliceAtts.originIntercept = 0
SliceAtts.originPercent = 50
SliceAtts.originZone = 0
SliceAtts.originNode = 0
SliceAtts.normal = (0, -1, 0)
SliceAtts.axisType = SliceAtts.ThetaPhi  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
SliceAtts.upAxis = (0, 0, 1)
SliceAtts.project2d = 0
SliceAtts.interactive = 1
SliceAtts.flip = 0
SliceAtts.originZoneDomain = 0
SliceAtts.originNodeDomain = 0
SliceAtts.meshName = "mesh"
SliceAtts.theta = 0
SliceAtts.phi = 0
SetOperatorOptions(SliceAtts, 1)
AddPlot("Contour", "RadAll", 1, 1)
ContourAtts = ContourAttributes()
ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(0).position = 0
ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(29).position = 1
ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
ContourAtts.defaultPalette.equalSpacingFlag = 1
ContourAtts.defaultPalette.discreteFlag = 1
ContourAtts.defaultPalette.categoryName = "Standard"
ContourAtts.changedColors = ()
ContourAtts.colorType = ContourAtts.ColorByMultipleColors  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "Default"
ContourAtts.invertColorTable = 0
ContourAtts.legendFlag = 0
ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
ContourAtts.lineWidth = 0
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
ContourAtts.contourNLevels = 10
ContourAtts.contourValue = (2.2)
ContourAtts.contourPercent = ()
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.minFlag = 0
ContourAtts.maxFlag = 0
ContourAtts.min = 0
ContourAtts.max = 1
ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
ContourAtts.wireframe = 0
SetPlotOptions(ContourAtts)
ActivateDatabase("fldDat.vti")
ActivateDatabase("fldDat.vti")
AddPlot("Pseudocolor", "operators/IntegralCurve/Bfld", 1, 1)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
PseudocolorAtts.minFlag = 0
PseudocolorAtts.min = 0
PseudocolorAtts.maxFlag = 0
PseudocolorAtts.max = 1
PseudocolorAtts.centering = PseudocolorAtts.Zonal  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "Cool"
PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 1
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 4
PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
PseudocolorAtts.lineType = PseudocolorAtts.Tube  # Line, Tube, Ribbon
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeResolution = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.tubeRadiusVarEnabled = 0
PseudocolorAtts.tubeRadiusVar = ""
PseudocolorAtts.tubeRadiusVarRatio = 10
PseudocolorAtts.endPointType = PseudocolorAtts.None  # None, Heads, Tails, Both
PseudocolorAtts.endPointStyle = PseudocolorAtts.Spheres  # Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 0.125
PseudocolorAtts.endPointRadiusBBox = 0.05
PseudocolorAtts.endPointResolution = 10
PseudocolorAtts.endPointRatio = 5
PseudocolorAtts.endPointRadiusVarEnabled = 0
PseudocolorAtts.endPointRadiusVar = ""
PseudocolorAtts.endPointRadiusVarRatio = 10
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 0
PseudocolorAtts.lightingFlag = 1
PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
PseudocolorAtts.pointColor = (0, 0, 0, 0)
SetPlotOptions(PseudocolorAtts)
IntegralCurveAtts = IntegralCurveAttributes()
IntegralCurveAtts.sourceType = IntegralCurveAtts.PointList  # SpecifiedPoint, PointList, SpecifiedLine, Circle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection, FieldData
IntegralCurveAtts.pointSource = (0, 0, 0)
IntegralCurveAtts.lineStart = (0, 0, 0)
IntegralCurveAtts.lineEnd = (1, 0, 0)
IntegralCurveAtts.planeOrigin = (0, 0, 0)
IntegralCurveAtts.planeNormal = (0, 0, 1)
IntegralCurveAtts.planeUpAxis = (0, 1, 0)
IntegralCurveAtts.radius = 1
IntegralCurveAtts.sphereOrigin = (0, 0, 0)
IntegralCurveAtts.boxExtents = (0, 1, 0, 1, 0, 1)
IntegralCurveAtts.useWholeBox = 1
IntegralCurveAtts.pointList = (2.5, 0, -6, 2.5, 0, -3.6, 2.5, 0, -1.2, 2.5, 0, 1.2, 2.5, 0, 3.6, 2.5, 0, 6, 4.28571, 0, -6, 4.28571, 0, -3.6, 4.28571, 0, -1.2, 4.28571, 0, 1.2, 4.28571, 0, 3.6, 4.28571, 0, 6, 6.07143, 0, -6, 6.07143, 0, -3.6, 6.07143, 0, -1.2, 6.07143, 0, 1.2, 6.07143, 0, 3.6, 6.07143, 0, 6, 7.85714, 0, -6, 7.85714, 0, -3.6, 7.85714, 0, -1.2, 7.85714, 0, 1.2, 7.85714, 0, 3.6, 7.85714, 0, 6, 9.64286, 0, -6, 9.64286, 0, -3.6, 9.64286, 0, -1.2, 9.64286, 0, 1.2, 9.64286, 0, 3.6, 9.64286, 0, 6, 11.4286, 0, -6, 11.4286, 0, -3.6, 11.4286, 0, -1.2, 11.4286, 0, 1.2, 11.4286, 0, 3.6, 11.4286, 0, 6, 13.2143, 0, -6, 13.2143, 0, -3.6, 13.2143, 0, -1.2, 13.2143, 0, 1.2, 13.2143, 0, 3.6, 13.2143, 0, 6, 15, 0, -6, 15, 0, -3.6, 15, 0, -1.2, 15, 0, 1.2, 15, 0, 3.6, 15, 0, 6)
IntegralCurveAtts.fieldData = ()
IntegralCurveAtts.sampleDensity0 = 2
IntegralCurveAtts.sampleDensity1 = 2
IntegralCurveAtts.sampleDensity2 = 2
IntegralCurveAtts.dataValue = IntegralCurveAtts.SeedPointID  # Solid, SeedPointID, Speed, Vorticity, ArcLength, TimeAbsolute, TimeRelative, AverageDistanceFromSeed, CorrelationDistance, Difference, Variable
IntegralCurveAtts.dataVariable = ""
IntegralCurveAtts.integrationDirection = IntegralCurveAtts.Both  # Forward, Backward, Both, ForwardDirectionless, BackwardDirectionless, BothDirectionless
IntegralCurveAtts.maxSteps = 4000
IntegralCurveAtts.terminateByDistance = 0
IntegralCurveAtts.termDistance = 10
IntegralCurveAtts.terminateByTime = 0
IntegralCurveAtts.termTime = 10
IntegralCurveAtts.maxStepLength = 0.0001
IntegralCurveAtts.limitMaximumTimestep = 0
IntegralCurveAtts.maxTimeStep = 0.1
IntegralCurveAtts.relTol = 0.0001
IntegralCurveAtts.absTolSizeType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
IntegralCurveAtts.absTolAbsolute = 1e-06
IntegralCurveAtts.absTolBBox = 1e-06
IntegralCurveAtts.fieldType = IntegralCurveAtts.Default  # Default, FlashField, M3DC12DField, M3DC13DField, Nek5000Field, NektarPPField, NIMRODField
IntegralCurveAtts.fieldConstant = 1
IntegralCurveAtts.velocitySource = (0, 0, 0)
IntegralCurveAtts.integrationType = IntegralCurveAtts.AdamsBashforth  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
IntegralCurveAtts.parallelizationAlgorithmType = IntegralCurveAtts.VisItSelects  # LoadOnDemand, ParallelStaticDomains, MasterSlave, VisItSelects
IntegralCurveAtts.maxProcessCount = 10
IntegralCurveAtts.maxDomainCacheSize = 3
IntegralCurveAtts.workGroupSize = 32
IntegralCurveAtts.pathlines = 0
IntegralCurveAtts.pathlinesOverrideStartingTimeFlag = 0
IntegralCurveAtts.pathlinesOverrideStartingTime = 0
IntegralCurveAtts.pathlinesPeriod = 0
IntegralCurveAtts.pathlinesCMFE = IntegralCurveAtts.POS_CMFE  # CONN_CMFE, POS_CMFE
IntegralCurveAtts.displayGeometry = IntegralCurveAtts.Lines  # Lines, Tubes, Ribbons
IntegralCurveAtts.cleanupMethod = IntegralCurveAtts.Merge  # NoCleanup, Merge, Before, After
IntegralCurveAtts.cleanupThreshold = 0.01
IntegralCurveAtts.cropBeginFlag = 0
IntegralCurveAtts.cropBegin = 0
IntegralCurveAtts.cropEndFlag = 0
IntegralCurveAtts.cropEnd = 0
IntegralCurveAtts.cropValue = IntegralCurveAtts.Time  # Distance, Time, StepNumber
IntegralCurveAtts.sampleDistance0 = 10
IntegralCurveAtts.sampleDistance1 = 10
IntegralCurveAtts.sampleDistance2 = 10
IntegralCurveAtts.fillInterior = 1
IntegralCurveAtts.randomSamples = 0
IntegralCurveAtts.randomSeed = 0
IntegralCurveAtts.numberOfRandomSamples = 1
IntegralCurveAtts.issueAdvectionWarnings = 1
IntegralCurveAtts.issueBoundaryWarnings = 1
IntegralCurveAtts.issueTerminationWarnings = 1
IntegralCurveAtts.issueStepsizeWarnings = 1
IntegralCurveAtts.issueStiffnessWarnings = 1
IntegralCurveAtts.issueCriticalPointsWarnings = 1
IntegralCurveAtts.criticalPointThreshold = 0.001
IntegralCurveAtts.correlationDistanceAngTol = 5
IntegralCurveAtts.correlationDistanceMinDistAbsolute = 1
IntegralCurveAtts.correlationDistanceMinDistBBox = 0.005
IntegralCurveAtts.correlationDistanceMinDistType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
IntegralCurveAtts.selection = ""
SetOperatorOptions(IntegralCurveAtts, 1)
DrawPlots()
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0, -0.5, 0.866025)
View3DAtts.focus = (-1.025, 0, 0)
View3DAtts.viewUp = (0, 0.866025, 0.5)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 25.6496
View3DAtts.nearPlane = -51.2993
View3DAtts.farPlane = 51.2993
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (-1.025, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0, -0.5, 0.866025)
View3DAtts.focus = (-1.025, 0, 0)
View3DAtts.viewUp = (0, 0.866025, 0.5)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 25.6496
View3DAtts.nearPlane = -51.2993
View3DAtts.farPlane = 51.2993
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (-1.025, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0, -0.866025, 0.5)
View3DAtts.focus = (-1.025, 0, 0)
View3DAtts.viewUp = (0, 0.5, 0.866025)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 25.6496
View3DAtts.nearPlane = -51.2993
View3DAtts.farPlane = 51.2993
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (-1.025, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0, -0.866025, 0.5)
View3DAtts.focus = (-1.025, 0, 0)
View3DAtts.viewUp = (0, 0.5, 0.866025)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 25.6496
View3DAtts.nearPlane = -51.2993
View3DAtts.farPlane = 51.2993
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (-1.025, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0, -0.866025, 0.5)
View3DAtts.focus = (-1.025, 0, 0)
View3DAtts.viewUp = (0, 0.5, 0.866025)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 25.6496
View3DAtts.nearPlane = -51.2993
View3DAtts.farPlane = 51.2993
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.5
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (-1.025, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0, -0.866025, 0.5)
View3DAtts.focus = (-1.025, 0, 0)
View3DAtts.viewUp = (0, 0.5, 0.866025)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 25.6496
View3DAtts.nearPlane = -51.2993
View3DAtts.farPlane = 51.2993
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.5
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (-1.025, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "tmpVid"
SaveWindowAtts.fileName = "visit"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1200
SaveWindowAtts.height = 1024
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 100
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
