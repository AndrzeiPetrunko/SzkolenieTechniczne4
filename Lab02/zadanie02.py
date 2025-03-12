K1 = type('K1', (), {'attr' : 10})
k1 = K1()

K2 = type('K2', (K1,), {
    'attr' : 20,
    'attr_minus_ten' : lambda x: x.attr - 10,
    'attr_plus_ten' : lambda x: x.attr + 10
})
k2 = K2()

K3 = type('K3', (K2,), {'attr' : 30})
k3 = K3()