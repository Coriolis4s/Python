##
# This module experiments with the metaclass architecture. X is a 
# metaclass that derives from type.
##

class X(type):
    
    def __new__(metacls, name, base, dict):
        print "class x"
        def outer(func):
            def inner(params):
                print "shell: {}".format(params)
            return inner
        #print dict
        @outer
        def shell(x):
            #print "shell: {}".format(x)
            return None
        shell(name)
        return type.__new__(metacls, name, base, {"myattr":"return 2"})
        
    def __call__(*args):
        print "class called"
        return type.__call__(*args)

class A(object):

    def __init__(self, x=None):
        self.x = x
        
    def printx(self):
        print self.x
        
class B(A):

    __metaclass__ = X
    
    def __init__(self, y):
        self.y = y
        super(B, self).__init__()

    def printx(self):
        super(B, self).printx()
        print "B ", self.y


if __name__=='__main__':
    '''
    a = A(15)
    a.printx()
    '''
    b = B(6)
    type(b)
    b.printx()
    print hasattr(b, 'myattr')
    print "b.myattr: ", b.myattr
    print "B.__mro__: ", B.__mro__
