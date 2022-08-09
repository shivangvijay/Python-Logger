#!/usr/bin/env python3
from logger import Logger

inst = Logger.get_instance()

inst.debug("heelo", "leelo", 21, 98.8776768787, True, False)
inst.error("heelo", "leelo", 21, 98.8776768787, True, False)
inst.info("heelo", "leelo", 21, 98.8776768787, True, False)
inst.trace("heelo", "leelo", 21, 98.8776768787, True, False)


anotherInst = Logger.get_instance()


anotherInst.debug("heelo", "leelo", 21, 98.8776768787, True, False)
anotherInst.error("heelo", "leelo", 21, 98.8776768787, True, False)
anotherInst.info("heelo", "leelo", 21, 98.8776768787, True, False)
anotherInst.trace("heelo", "leelo", 21, 98.8776768787, True, False)