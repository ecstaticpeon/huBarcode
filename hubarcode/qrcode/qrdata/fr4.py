import cPickle

frame_data = cPickle.loads("""(lp1
(lp2
I1
aI1
aI1
aI1
aI1
aI1
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI1
aI1
aI1
aI1
aI1
aI1
aa(lp3
I1
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI1
aa(lp4
I1
aI0
aI1
aI1
aI1
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI1
aI1
aI1
aI0
aI1
aa(lp5
I1
aI0
aI1
aI1
aI1
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI1
aI1
aI1
aI0
aI1
aa(lp6
I1
aI0
aI1
aI1
aI1
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI1
aI1
aI1
aI0
aI1
aa(lp7
I1
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI1
aa(lp8
I1
aI1
aI1
aI1
aI1
aI1
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI1
aI1
aI1
aI1
aI1
aI1
aa(lp9
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp10
I0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp11
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp12
I0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp13
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp14
I0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp15
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp16
I0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp17
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp18
I0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp19
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp20
I0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp21
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp22
I0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp23
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp24
I0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp25
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp26
I0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI1
aI1
aI1
aI1
aI0
aI0
aI0
aI0
aa(lp27
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aa(lp28
I1
aI1
aI1
aI1
aI1
aI1
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI0
aI0
aI0
aa(lp29
I1
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aa(lp30
I1
aI0
aI1
aI1
aI1
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI1
aI1
aI1
aI1
aI1
aI0
aI0
aI0
aI0
aa(lp31
I1
aI0
aI1
aI1
aI1
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp32
I1
aI0
aI1
aI1
aI1
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp33
I1
aI0
aI0
aI0
aI0
aI0
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp34
I1
aI1
aI1
aI1
aI1
aI1
aI1
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp35
a.""")
