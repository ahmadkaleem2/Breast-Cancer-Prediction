import inline as inline
import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split #for training
from sklearn.linear_model import LogisticRegression #for training
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from tkinter import * # for gui
data = pd.read_csv('C:\\Users\\ahmad\\PycharmProjects\\untitled\\DM\\data1.csv', delimiter=",", header=None)

X = data.drop(0,axis=1)
print(X)
y = data[0]
print(y)



X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state= 0)


logmodel = LogisticRegression(max_iter=1000000)

logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)
print(X_test)

print(classification_report(y_test,predictions))



print(confusion_matrix(y_test,predictions))

print(accuracy_score(y_test,predictions))




import tkinter as tk

from tkinter import ttk

window = tk.Tk()

window.title("Breast Cancer Prediction")
window.minsize(1600, 900)


def clickMe():


    pp1 = float( p1.get())
    pp2 = float( p2.get())
    pp3 = float( p3.get())
    pp4 = float( p4.get())
    pp5 = float( p5.get())
    pp6 = float( p6.get())
    pp7 = float( p7.get())
    pp8 = float( p8.get())
    pp9 = float( p9.get())
    pp10 = float( p10.get())
    pp11 = float( p11.get())
    pp12 = float( p12.get())
    pp13 = float( p13.get())
    pp14 = float( p14.get())
    pp15 = float( p15.get())
    pp16 = float( p16.get())
    pp17 = float( p17.get())
    pp18 = float( p18.get())
    pp19 = float( p19.get())
    pp20 = float( p20.get())
    pp21 = float( p21.get())
    pp22 = float( p22.get())
    pp23 = float( p23.get())
    pp24 = float( p24.get())
    pp25 = float( p25.get())
    pp26 = float( p26.get())
    pp27 = float( p27.get())
    pp28 = float( p28.get())
    pp29 = float( p29.get())
    pp30 = float( p30.get())
    t1 = [[pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8,pp9,pp10,pp11,pp12,pp13,pp14,pp15,pp16,pp17,pp18,pp19,pp20,pp21,pp22,pp23,pp24,pp25,pp26,pp27,pp28,pp29,pp30]]

    a = logmodel.predict(t1)
    if(a=='B'):
        print("Benign")
        label1 = ttk.Label(window, text="Diagnosis: Benign")

        label1.grid(column=15, row=0)
    else:
        print("Malignant")
        label1 = ttk.Label(window, text="Diagnosis: Malignant")
        label1.grid(column=15, row=0)




label1 = ttk.Label(window, text="radius_mean")
label1.grid(column=0, row=0)
p1 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p1)
nameEntered.grid(column=1, row=0)

label1 = ttk.Label(window, text="texture_mean")
label1.grid(column=0, row=1)
p2 = tk.StringVar()
nameEntered1 = ttk.Entry(window, width=15, textvariable=p2)
nameEntered1.grid(column=1, row=1)

label = ttk.Label(window, text="perimeter_mean")
label.grid(column=0, row=2)
p3 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p3)
nameEntered.grid(column=1, row=2)

label = ttk.Label(window, text="area_mean")
label.grid(column=0, row=3)
p4 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p4)
nameEntered.grid(column=1, row=3)

label = ttk.Label(window, text="smoothness_mean")
label.grid(column=0, row=4)
p5 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p5)
nameEntered.grid(column=1, row=4)

label = ttk.Label(window, text="compactness_mean")
label.grid(column=0, row=5)
p6 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p6)
nameEntered.grid(column=1, row=5)

label = ttk.Label(window, text="concavity_mean")
label.grid(column=0, row=6)
p7 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p7)
nameEntered.grid(column=1, row=6)

label = ttk.Label(window, text="concave points_mean")
label.grid(column=0, row=7)
p8 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p8)
nameEntered.grid(column=1, row=7)

label = ttk.Label(window, text="symmetry_mean")
label.grid(column=0, row=8)
p9 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p9)
nameEntered.grid(column=1, row=8)

label = ttk.Label(window, text="fractual_dimension_mean")
label.grid(column=0, row=9)
p10 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p10)
nameEntered.grid(column=1, row=9)

label = ttk.Label(window, text="radius_se")
label.grid(column=0, row=10)
p11 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p11)
nameEntered.grid(column=1, row=10)

label = ttk.Label(window, text="texture_se")
label.grid(column=0, row=11)
p12 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p12)
nameEntered.grid(column=1, row=11)

label = ttk.Label(window, text="perimeter_se")
label.grid(column=0, row=12)
p13 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p13)
nameEntered.grid(column=1, row=12)

label = ttk.Label(window, text="area_se")
label.grid(column=0, row=13)
p14 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p14)
nameEntered.grid(column=1, row=13)

label = ttk.Label(window, text="smoothness_se")
label.grid(column=0, row=14)
p15 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p15)
nameEntered.grid(column=1, row=14)

label = ttk.Label(window, text="compactness_se")
label.grid(column=0, row=15)
p16 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p16)
nameEntered.grid(column=1, row=15)

label = ttk.Label(window, text="concavity_se")
label.grid(column=0, row=16)
p17 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p17)
nameEntered.grid(column=1, row=16)

label = ttk.Label(window, text="concave points_se")
label.grid(column=0, row=17)
p18 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p18)
nameEntered.grid(column=1, row=17)

label = ttk.Label(window, text="symmetry_se")
label.grid(column=0, row=18)
p19 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p19)
nameEntered.grid(column=1, row=18)

label = ttk.Label(window, text="fractual_dimension_se")
label.grid(column=0, row=19)
p20 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p20)
nameEntered.grid(column=1, row=19)

label = ttk.Label(window, text="radius_worst")
label.grid(column=0, row=20)
p21 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p21)
nameEntered.grid(column=1, row=20)

label = ttk.Label(window, text="texture_worst")
label.grid(column=0, row=21)
p22 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p22)
nameEntered.grid(column=1, row=21)

label = ttk.Label(window, text="perimeter_worst")
label.grid(column=0, row=22)
p23 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p23)
nameEntered.grid(column=1, row=22)

label = ttk.Label(window, text="area_worst")
label.grid(column=0, row=23)
p24 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p24)
nameEntered.grid(column=1, row=23)

label = ttk.Label(window, text="smoothness_worst")
label.grid(column=0, row=24)
p25 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p25)
nameEntered.grid(column=1, row=24)


label = ttk.Label(window, text="compactness_worst")
label.grid(column=0, row=25)
p26 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p26)
nameEntered.grid(column=1, row=25)

label = ttk.Label(window, text="concavity_worst")
label.grid(column=0, row=26)
p27 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p27)
nameEntered.grid(column=1, row=26)

label = ttk.Label(window, text="concave points_worst")
label.grid(column=0, row=27)
p28 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p28)
nameEntered.grid(column=1, row=27)

label = ttk.Label(window, text="symmetry_worst")
label.grid(column=0, row=28)
p29 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p29)
nameEntered.grid(column=1, row=28)

label = ttk.Label(window, text="fractual_dimension_worst")
label.grid(column=0, row=29)
p30 = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=p30)
nameEntered.grid(column=1, row=29)






button = ttk.Button(window, text="Click Me", command=clickMe)
button.grid(column=0, row=31)

window.mainloop()
























