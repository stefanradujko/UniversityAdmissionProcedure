def procitaj_iz_fajla():
    fajl = open('applicant_list_7.txt', 'r')
    lista = []
    for i in fajl:
        lista.append(i.split())
    return lista


def rangiraj_katedre():
    k = ['Mathematics', 'Physics', 'Biotech', 'Chemistry', 'Engineering']
    recnik = dict()
    for i in k:
        broj = 0
        for kan in kandidati:
            if kan[3] == i:
                broj += 1
        recnik[i] = broj
    return sorted(recnik.items(), reverse=True, key=lambda x: x[1])


def vrati_kandidate(broj_zelje, katedra):
    lista_kand_krug = []
    for kan in kandidati:
        if kan[broj_zelje] == katedra:
            lista_kand_krug.append(kan)
    if katedra == 'Physics':
        return sorted(sorted(lista_kand_krug, key=lambda x: (x[0], x[1])), reverse=True,
                      key=lambda x: round((int(x[2]) + int(x[4])) / 2, 2) if round((int(x[2]) + int(x[4])) / 2,
                                                                                   2) > int(x[6]) else int(x[6]))
    elif katedra == 'Chemistry':
        return sorted(sorted(lista_kand_krug, key=lambda x: (x[0], x[1])), reverse=True,
                      key=lambda x: int(x[3]) if int(x[3]) > int(x[6]) else int(x[6]))
    elif katedra == 'Biotech':
        return sorted(sorted(lista_kand_krug, key=lambda x: (x[0], x[1])), reverse=True,
                      key=lambda x: round((int(x[3]) + int(x[2])) / 2, 2) if round((int(x[3]) + int(x[2])) / 2,
                                                                                   2) > int(x[6]) else int(x[6]))
    elif katedra == 'Mathematics':
        return sorted(sorted(lista_kand_krug, key=lambda x: (x[0], x[1])), reverse=True,
                      key=lambda x: int(x[4]) if int(x[4]) > int(x[6]) else int(x[6]))
    else:
        return sorted(sorted(lista_kand_krug, key=lambda x: (x[0], x[1])), reverse=True,
                      key=lambda x: round((int(x[4]) + int(x[5])) / 2, 2) if round((int(x[4]) + int(x[5])) / 2,
                                                                                   2) > int(x[6]) else int(x[6]))


def izbaci_kandidata(kan):
    for k in kandidati:
        if k == kan:
            kandidati.remove(kan)


def izbaci_katedru(kat):
    for k in katedre:
        if k[0] == kat:
            katedre.remove(k)


def dodaj_u_glavni_recnik(gr, r):
    for element in r:
        if element not in gr.keys():
            gr[element] = r[element]

        else:
            gr[element].extend(r[element])
    return gr


def upisi(n):
    recnik_glavni = {}
    broj_ture = 7
    while True:
        for k in katedre:
            broj = n
            lista_kandidata = vrati_kandidate(broj_ture, k[0])
            prazna_lista = []
            recnik_kand_kat = {}
            if broj_ture != 7:
                broj -= len(recnik_glavni[k[0]])
            if len(lista_kandidata) < broj:
                dokle = len(lista_kandidata)
            else:
                dokle = broj
            for i in range(0, dokle):
                prazna_lista.append(lista_kandidata[i])
                izbaci_kandidata(lista_kandidata[i])
            recnik_kand_kat[k[0]] = prazna_lista
            glavni_recnik = dodaj_u_glavni_recnik(recnik_glavni, recnik_kand_kat)
        for pred in glavni_recnik:
            if len(glavni_recnik[pred]) == n:
                izbaci_katedru(pred)
        if len(katedre) == 0 or broj_ture == 9:
            break
        broj_ture += 1
    return glavni_recnik


def ispisi_upisane():
    sortirana_lista = sorted(recnik.keys())
    for key in sortirana_lista:
        f = open(f'{str.lower(key)}.txt', 'w').close()
        print(key)
        for kandidat in recnik[key]:
            fajl = open(f'{str.lower(key)}.txt', 'a')
            if key == 'Physics':
                print(
                    f"{kandidat[0]} {kandidat[1]} {max(round((int(kandidat[2]) + int(kandidat[4])) / 2, 2), int(kandidat[6]))}")
                fajl.write(
                    f"{kandidat[0]} {kandidat[1]} {max(round((int(kandidat[2]) + int(kandidat[4])) / 2, 2), int(kandidat[6]))}\n")
            elif key == 'Chemistry':
                print(f"{kandidat[0]} {kandidat[1]} {max(int(kandidat[3]), int(kandidat[6]))}")
                fajl.write(f"{kandidat[0]} {kandidat[1]} {max(int(kandidat[3]), int(kandidat[6]))}\n")
            elif key == 'Biotech':
                print(
                    f"{kandidat[0]} {kandidat[1]} {max(round((int(kandidat[3]) + int(kandidat[2])) / 2, 2), int(kandidat[6]))}")
                fajl.write(
                    f"{kandidat[0]} {kandidat[1]} {max(round((int(kandidat[3]) + int(kandidat[2])) / 2, 2), int(kandidat[6]))}\n")
            elif key == 'Mathematics':
                print(f"{kandidat[0]} {kandidat[1]} {max(int(kandidat[4]), int(kandidat[6]))}")
                fajl.write(f"{kandidat[0]} {kandidat[1]} {max(int(kandidat[4]), int(kandidat[6]))}\n")
            else:
                print(
                    f"{kandidat[0]} {kandidat[1]} {max(round((int(kandidat[4]) + int(kandidat[5])) / 2, 2), int(kandidat[6]))}")
                fajl.write(
                    f"{kandidat[0]} {kandidat[1]} {max(round((int(kandidat[4]) + int(kandidat[5])) / 2, 2), int(kandidat[6]))}\n")
            fajl.close()
        print('')


def sortiraj_recnik():
    for p in recnik:
        if p == 'Physics':
            recnik[p] = sorted(sorted(recnik[p], key=lambda x: (x[0], x[1])), reverse=True,
                               key=lambda x: round((int(x[2]) + int(x[4])) / 2, 2) if round((int(x[2]) + int(x[4])) / 2,
                                                                                            2) > int(x[6]) else int(x[6]))
        elif p == 'Chemistry':
            recnik[p] = sorted(sorted(recnik[p], key=lambda x: (x[0], x[1])), reverse=True,
                               key=lambda x: int(x[3]) if int(x[3]) > int(x[6]) else int(x[6]))
        elif p == 'Biotech':
            recnik[p] = sorted(sorted(recnik[p], key=lambda x: (x[0], x[1])), reverse=True,
                               key=lambda x: round((int(x[3]) + int(x[2])) / 2, 2) if round((int(x[3]) + int(x[2])) / 2,
                                                                                            2) > int(x[6]) else int(x[6]))
        elif p == 'Mathematics':
            recnik[p] = sorted(sorted(recnik[p], key=lambda x: (x[0], x[1])), reverse=True,
                               key=lambda x: int(x[4]) if int(x[4]) > int(x[6]) else int(x[6]))
        else:
            recnik[p] = sorted(sorted(recnik[p], key=lambda x: (x[0], x[1])), reverse=True,
                               key=lambda x: round((int(x[4]) + int(x[5])) / 2, 2) if round((int(x[4]) + int(x[5])) / 2,
                                                                                            2) > int(x[6]) else int(x[6]))


n = int(input())
kandidati = procitaj_iz_fajla()
katedre = rangiraj_katedre()
recnik = upisi(n)
sortiraj_recnik()
ispisi_upisane()
