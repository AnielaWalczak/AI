import random
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

from krata import *

def drzewo_decyzyjne():
    columns = ['plec', 'wiek', 'czas_w_pom', 'temp_w_pom', 'poziom_kurzu', 'poziom_oswietlenia', 'niebezp_towary', 'decyzja']
    df = pd.read_csv("dataset.csv", header=0, sep=";", names=columns)
    x = df[['plec', 'wiek', 'czas_w_pom', 'temp_w_pom', 'poziom_kurzu', 'poziom_oswietlenia', 'niebezp_towary']]
    y = df.decyzja
    #df.info()
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    clf = DecisionTreeClassifier()
    clf = clf.fit(x, y)
    # print("Dokładność: ", metrics.accuracy_score(y_test, y_pred))
    return clf

def decyzja_osoba(osoba: PoleKraty, clf: DecisionTreeClassifier):
    z=[]
    z.extend(random.choices([1,2], weights=[1,2], k=1)) #1 kobieta, 2 mężczyzna
    z.extend(random.choices([1, 2], weights=[4,1], k=1)) # 1 dorosły, 2 osoba starsza
    z.extend(random.choices([1, 2, 3], weights=[2, 5, 3], k=1)) # jak długo przebywa w pomieszczeniu, 3 to nadłużej
    if osoba.kolumna > 21:
        z.append(0)  # zimne pomieszczenie
    else:
        z.append(1)  # normalne pomieszczenie
    z.extend(random.choices([1, 2], weights=[7, 3], k=1)) # poziom kurzu, 2 to największy/najbardziej niebezpieczny
    z.extend(random.choices([1, 2], weights=[4, 6], k=1)) # poziom oświetlenia, 2 to najlepsze oświetlenie
    if (0<=osoba.wiersz or osoba.wiersz<=13) and (17<=osoba.kolumna or osoba.kolumna<=19): #obok szafki z niebezpiecznymi towarami
        z.append(1)
    else:
        z.append(0)
    columns = ['plec', 'wiek', 'czas_w_pom', 'temp_w_pom', 'poziom_kurzu', 'poziom_oswietlenia', 'niebezp_towary']
    z1 = pd.DataFrame([z],columns=columns)
    z_pred = clf.predict(z1)
    #print(z)
    #print(z_pred)
    return (z_pred)