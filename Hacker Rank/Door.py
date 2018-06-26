R=int(input())
C=int(input())
for i in xrange(0,R/2): 
    print ('.|.'*i).ljust((C-2)/2,'-')+'.|.'+('.|.'*i).rjust((C-2)/2,'-')
print 'WELCOME'.center(C,'-')
for i in reversed(xrange(0,R/2)): 
    print ('.|.'*i).ljust((C-2)/2,'-')+'.|.'+('.|.'*i).rjust((C-2)/2,'-')
