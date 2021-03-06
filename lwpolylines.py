import ezdxf
dwg = ezdxf.new('AC1015')
msp = dwg.modelspace()

# point format = (x, y, [start_width, [end_width, [bulge]]])
# set start_width, end_width to 0 to be ignored (x, y, 0, 0, bulge).

points = [(0, 0,), (3, 0, .1, .2, 1.5), (6, 0, .1, .05), (9, 0)]
msp.add_lwpolyline(points)
msp.add_arc((0, 0), 10, 30, 90)
print isinstance(msp, ezdxf.modern.layouts.Layout)
# print dwg.entitydb._database

# ezdxf.drawing.modelspace().foo=foo
# from ezdxf import *
# ezdxf.GraphicsFactory().foo=foo
# dwg.saveas("lwpolyline5.dxf")
