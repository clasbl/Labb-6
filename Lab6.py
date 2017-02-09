import timeit
class Låt:
    def __init__(self, trackid, låtid, artistnamn, titel):
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.titel = titel

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn


def linsokl(listan, nyckel):
#Linsok tagen från föreläsning 3
    for x in listan:
        if x.artistnamn == nyckel:
            return True
    return False

def linsok(listan, nyckel):
#Linsok tagen från föreläsning 3
    for x in listan:
        if x == nyckel:
            return True
    return False

def binsok(listan, nyckel):
#Tagen från föreläsning 3
    vanster = 0
    hoger = len(listan)-1
    found = False

    while vanster <= hoger and not found:
        mitten = (vanster + hoger)//2
        if listan[mitten].artistnamn == nyckel:
            found = True
        else:
            if nyckel < listan[mitten].artistnamn:
                hoger = mitten-1
            else:
                vanster = mitten+1
    return found


#quicksort, qsort och partitionera tagen från föreläsning 7
def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)

def qsort(data, i, j):
    pivotindex = (i+j)//2
    data[pivotindex], data[j] = data[j], data[pivotindex]
    k = partitionera(data, i-1, j, data[j])
    data[k], data[j] = data[j], data[k]
    if k-i > 1:
        qsort(data, i, k-1)
    if j-k > 1:
        qsort(data, k+1, j)

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h: 
            break
    data[v], data[h] = data[h], data[v]
    return v
def urvalssortera(data):
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i+1,n):
            if data[j] < data[minst]:
                minst = j
        data[minst],data[i] = data[i], data[minst]

def listMaker():
    låtlista = []
    låtdict = {}
    with open("unique_tracks.txt", "r", encoding = "utf-8") as fil:
        for rad in fil:
            rad.strip('\n')
            låten = rad.split('<SEP>')
            
            låtobj = Låt(låten[0].lower(), låten[1],låten[2],låten[3])
            låtlista.append(låtobj)
            if låtobj.artistnamn.lower() in låtdict:
                låtdict[låtobj.artistnamn.lower()].append([låtobj.trackid, låtobj.låtid, låtobj.titel])

            else:
                låtdict[låtobj.artistnamn.lower()]= [låtobj.trackid, låtobj.låtid, låtobj.titel]
    return låtlista, låtdict

def main():
    låtlista, låtdict = listMaker()
    n = len(låtlista)
    print("Antal element =", n)

    sista = låtlista[n-1]
    testartist = sista.artistnamn
    linjtid = timeit.timeit(stmt = lambda: linsokl(låtlista, testartist), number = 1)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

#    urvalsorttid = timeit.timeit(stmt = lambda: urvalssortera(låtlista), number = 1)
#    print("Urvalssökningen tog", round(urvalsorttid, 4) , "sekunder")

    sorttid = timeit.timeit(stmt = lambda: quicksort(låtlista), number = 1)
    print('quicksort tog', round(sorttid, 4) , 'sekunder')

    Bintid = timeit.timeit(stmt = lambda: binsok(låtlista, testartist), number = 1)
    print('Binsok tog', round(Bintid, 4) , 'sekunder')

    linjtid = timeit.timeit(stmt = lambda: linsok(låtdict, testartist), number = 1)
    print("Linjärsökningen av dictionaryn tog", round(linjtid, 4) , "sekunder")


main()

