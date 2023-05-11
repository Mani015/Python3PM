
# adding the global + local


G1 = 100
print('Global v:',G1)

def ADDTIION():
    L1 = 200
    print('local v:',L1)
    print()
    print('Global v:',G1)
    x = G1 + L1
    print('adding global and local:',x)
ADDTIION()
print("GLobal v:",G1)
# Global v: 100
# local v: 200
#
# Global v: 100
# adding global and local: 300
# GLobal v: 100
