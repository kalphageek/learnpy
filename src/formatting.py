gu = 'seoch'
dong = 'yangjae'
bunji = 123

#case1
print('%s %s %d'% (gu, dong, bunji))

#case2
print('{} {} {}'.format(gu, dong, bunji))

#case3
print('{2} {0} {1}'.format(gu, dong, bunji))

#case4
print('{gu} {dong} {bunji}'.format(gu='seocho', dong='yangjae', bunji=123))
#print('{gu} {dong} {bunji}'.format(gu, dong, bunji)) -->error

#case5
juso = {'gu':'seocho', 'dong':'yangjae', 'bunji':123}
print('{0[gu]} {0[dong]} {0[bunji]}'.format(juso))