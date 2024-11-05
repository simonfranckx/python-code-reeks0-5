m=(input('Geef een getal dat minstens 4 cijfers bevat: '))
n=len(m)
som=0
eerstegetal = m[1:n + 1]
eerstegetal= eerstegetal.lstrip('0')
if eerstegetal== '':
    eerstegetal="0"
lengte=len(eerstegetal)
inspringing=n-lengte-1
spaties= " "*inspringing
print(f"  {spaties}{eerstegetal}")
eerst=int(f"{eerstegetal}")
if eerstegetal==0:
    eerst=int(0)
for index in range(1,n):
    getal=m[index]
    positie=m.find(getal,index)
    nieuw1= m[0:positie]
    nieuw2= m[positie+1:n+1]
    nieuw=int(f"{nieuw1}{nieuw2}")
    som+=nieuw
    if index!=n-1:
        print(f"  {nieuw1}{nieuw2}")
    else:
        print(f"+ {nieuw1}{nieuw2}")

print("="*(n+1))
print("",som+eerst)
#end