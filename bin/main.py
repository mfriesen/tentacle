#!/usr/bin/env python

from tentacle import *

print 'STARTING ----------'
operation = OperationLinux()
operation.service_stop("Tomcat7")
print 'ALL DONE'