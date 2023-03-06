#!/usr/bin/env python3
from Logger import Logger

inst = Logger()

inst.debug("String", 21, 98.8776768787, 48, True, False)
inst.error("String", 21, 98.8776768787, 48, True, False)
inst.info("String", 21, 98.8776768787, 48, True, False)
inst.trace("String", 21, 98.8776768787, 48, True, False)


anotherInst = Logger()


anotherInst.debug("String", 21, 98.8776768787, 48, True, False)
anotherInst.error("String", 21, 98.8776768787, 48, True, False)
anotherInst.info("String", 21, 98.8776768787, 48, True, False)
anotherInst.trace("String", 21, 98.8776768787, 48, True, False)