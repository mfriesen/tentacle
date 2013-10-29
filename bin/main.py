#!/usr/bin/env python

from tentacle.operation_mac import OperationMac
from tentacle.operation import OperationResult

print 'STARTING ----------'
operation = OperationMac()
result = operation.service_stop("Tomcat7")

if result.isSuccess():
    print "SUCCESS"
else:
    print "ERROR"
    print result.stderrdata

print 'ALL DONE'