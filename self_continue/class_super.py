class Animal( ):

    def __init__(self, name):
        self.name = name

    def walk( self ):
        print( "걷는다" )

    def eat( self ):
        print( "먹는다" )

    def greet( self ):
        print( "{}이(가) 인사한다".format(self.name) )

class Human( Animal ):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

    def shake( self ):
        print( "{}을 흔들면서".format(self.hand) )

    def greet( self ):
        self.shake()
        super().greet()

person = Human('사람','오른손')
person.greet()