# to play a sound file:  
from pyo import *  
sound = Server ( ) .boot ( )  
sound.start  ( )  
sound_file = SFPlayer( " path /to /users /sound.aif ", speed = 1, loop = True ).out ( )  
# for Granulating an audio buffer:  
sound = Server ( ) .boot ( )  
sound_nd = SndTable ( " path /to /users /sound.aif " )  
ev = HannTable ( )   
ps = Phasor ( freq = sound_nd.getRate ( )*.25, ml = sound_nd.getSize ( ) )  
dr = Noise ( mul = .001, add = .1 )  
granulate = Granulator ( sound_nd, ev, [ 1, 1.001 ] , ps, dr, 32, ml = .1 ).out ( )  
# to generate melodies:  
sound = Server ( ) .boot ( )  
sound.start ( )  
wv = SquareTable ( )  
ev = CosTable ( [ ( 0, 0 ) , ( 100 , 1 ) , ( 500 , 0.3 ) , ( 8391 , 0 ) ] )  
mt = Metro ( 0.135 , 12 ).play ( )  
ap = TrigEnv ( mt , table = ev , dr = 1 , ml = .1 )  
pt = TrigXnoiseMidi ( mt , dist = ' loopseg ' , x1 = 20 , scale = 1 , mrange = ( 47, 74 ) )  
out = Osc ( table = wav , freq = pt , ml = ap ).out ( )  