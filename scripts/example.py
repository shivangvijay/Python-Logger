#!/usr/bin/env python3
from logger import Logger

inst = Logger()   #or you an use Logger.get_instance() for first time also

inst.debug("String", 21, 98.8776768787, 48, True, False)
inst.error("String", 21, 98.8776768787, 48, True, False)
inst.info("String", 21, 98.8776768787, 48, True, False)
inst.trace("String", 21, 98.8776768787, 48, True, False)


sameInst = Logger.get_instance()


sameInst.debug("String", 21, 98.8776768787, 48, True, False)
sameInst.error("String", 21, 98.8776768787, 48, True, False)
sameInst.info("String", 21, 98.8776768787, 48, True, False)
sameInst.trace("String", 21, 98.8776768787, 48, True, False)