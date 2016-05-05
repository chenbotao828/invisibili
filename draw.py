# coding=utf-8
from __future__ import division
from model import *
from core import _const, typeTest
import ezdxf

ver = _const()
ver.const = {
    "R12": "AC1009",
    "2000": "AC1015",
    "2004": "AC1018",
    "2007": "AC1021",
    "2010": "AC1024",
    "2013": "AC1027", }


def draw_Models(aModels, cad_ver="AC1015", save_name="new.dxf"):
    '''draw Models, cad_ver can be \"2010\" or \"AC1024\"'''

    typeTest([Models, str, str], aModels, cad_ver, save_name)

    # create dxf obj and modelspace
    if cad_ver in ver.const.keys():
        cad_ver = ver.const[cad_ver]
    dxf = ezdxf.new(cad_ver)
    msp = dxf.modelspace()

    # draw models in Models
    for m in aModels:
        m.draw(msp)
    # save as dxf file
    dxf.saveas(save_name)
