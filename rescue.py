import random
import pandas as pd
import pydotplus
from sklearn.tree import DecisionTreeClassifier
from krata import *
from sklearn import metrics, tree

def drzewo_decyzyjne():
    columns = ['plec', 'wiek', 'czas_w_pom', 'temp_w_pom', 'poziom_kurzu', 'poziom_oswietlenia', 'niebezp_towary', 'decyzja']
    df = pd.read_csv("dataset.csv", header=0, sep=";", names=columns)
    kolumny_x=['plec', 'wiek', 'czas_w_pom', 'temp_w_pom', 'poziom_kurzu', 'poziom_oswietlenia', 'niebezp_towary']
    x = df[kolumny_x]
    y = df.decyzja
    #df.info()
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    clf = DecisionTreeClassifier()
    clf = clf.fit(x, y)
    # print("Dokładność: ", metrics.accuracy_score(y_test, y_pred))

  #  dot_data = tree.export_graphviz(clf, out_file=None, feature_names=kolumny_x, class_names=['0', '1'])
   # graph = pydotplus.graph_from_dot_data(dot_data)
    #graph.write_png('drzewo.png')

    return clf

def decyzja_osoba(osoba: PoleKraty, clf: DecisionTreeClassifier):
    z=[]
    z.extend(random.choices([1,2], weights=[1,2], k=1)) #1 kobieta, 2 mężczyzna
    z.append(random.randint(18, 75)) #od 55 osoba starsza
    z.append(random.randint(1, 60)) # jak długo przebywa w pomieszczeniu, od 40 min długo, od 20 min średnio, do 20 min krótko
    if osoba.kolumna > 21:
        z.append(0)  # zimne pomieszczenie
    else:
        z.append(1)  # normalne pomieszczenie
    z.append(random.randint(20, 100)) # poziom kurzu
    z.append(random.randint(20, 100)) # poziom oświetlenia
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