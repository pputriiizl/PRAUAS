#Python Expression
print('hasil dari ekspresi berikut')
print(15 % 5)
print(12 +3*5==75)
print("PML"+"15523")
print("100"+str(234))
print(((11%3)+2) != 8/2)


p=11; q=5; r=4
print (((p-r) == (r+q) ))
print ((((p%3)+q)!=(r%2)))
print (((q-3)==(p%2+q)))
print (((r+q)!=((p*2)%2)))
print (((((q%3)+p)>(r%2))))
print ((((r+p))<=(q*5)))
print(' ')

#1
print ("Honey" + "Boo"*3)
print(' ')

#2     
capitals = {}
capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['Engalnd'] = 'London'
capitals['Germany'] = 'Berlin'
print (capitals['Germany'])
print (' ')

#3
a = "23"
b=9
print(a+str(b))
print(' ')

#4
letters = ["a", "b", "o", "c", "p"]
print (letters[1])
print (letters[len(letters)-2])
print (letters + ["x"])
print (letters)
print (' ')

#5
print (' '.join('h a n d s'.split()))
print (' ')

#7
def pembagi_indeks(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return  -1
vals = [100,66,55,64,41,35,18,64]
hasil = pembagi_indeks(vals, 5)
print(hasil)
print(' ')

#8
def mystery(n, m):
    p = 0
    e = 0
    while p < n:
        p += 1

    while e < m:
        e += m

    return p


print(mystery(4,3))



