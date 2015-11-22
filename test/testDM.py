from soapy import confParse, aoSimLib, DM, WFS
import unittest
import numpy


class TestDM(unittest.TestCase):
    
    def testa_initDM(self):
        
        config = confParse.Configurator("../conf/sh_8x8.py")
        config.loadSimParams()
        
        mask = aoSimLib.circle(config.sim.pupilSize/2., config.sim.simSize)

        wfs = WFS.ShackHartmann(config.sim, config.wfss[0], config.atmos, config.lgss[0], mask)
        dm = DM.DM(config.sim, config.dms[0], [wfs], mask)
    

    def testb_initPiezo(self):
        
        config = confParse.Configurator("../conf/sh_8x8.py")
        config.loadSimParams()
        
        mask = aoSimLib.circle(config.sim.pupilSize/2., config.sim.simSize)

        wfs = WFS.ShackHartmann(config.sim, config.wfss[0], config.atmos, config.lgss[0], mask)
        self.dm = DM.Piezo(config.sim, config.dms[0], [wfs], mask)
    
    def testc_iMatPizeo(self):
        config = confParse.Configurator("../conf/sh_8x8.py")
        config.loadSimParams()
        
        mask = aoSimLib.circle(config.sim.pupilSize/2., config.sim.simSize)

        wfs = WFS.ShackHartmann(config.sim, config.wfss[0], config.atmos, config.lgss[0], mask)
        dm = DM.Piezo(config.sim, config.dms[0], [wfs], mask)
    
        dm.makeIMat()

    def testd_initGauss(self):

        config = confParse.Configurator("../conf/sh_8x8.py")
        config.loadSimParams()
        
        mask = aoSimLib.circle(config.sim.pupilSize/2., config.sim.simSize)

        wfs = WFS.ShackHartmann(config.sim, config.wfss[0], config.atmos, config.lgss[0], mask)
        dm = DM.GaussStack(config.sim, config.dms[0], [wfs], mask)

    def teste_iMatGauss(self):

        config = confParse.Configurator("../conf/sh_8x8.py")
        config.loadSimParams()
        
        mask = aoSimLib.circle(config.sim.pupilSize/2., config.sim.simSize)

        wfs = WFS.ShackHartmann(config.sim, config.wfss[0], config.atmos, config.lgss[0], mask)
        dm = DM.GaussStack(config.sim, config.dms[0], [wfs], mask)
        dm.makeIMat()

    def testf_initTT(self):

        config = confParse.Configurator("../conf/sh_8x8.py")
        config.loadSimParams()
        
        mask = aoSimLib.circle(config.sim.pupilSize/2., config.sim.simSize)

        wfs = WFS.ShackHartmann(config.sim, config.wfss[0], config.atmos, config.lgss[0], mask)
        dm = DM.TT(config.sim, config.dms[0], [wfs], mask)

    def testg_iMatTT(self):

        config = confParse.Configurator("../conf/sh_8x8.py")
        config.loadSimParams()
        
        mask = aoSimLib.circle(config.sim.pupilSize/2., config.sim.simSize)

        wfs = WFS.ShackHartmann(config.sim, config.wfss[0], config.atmos, config.lgss[0], mask)
        dm = DM.TT(config.sim, config.dms[0], [wfs], mask)
        dm.makeIMat()

