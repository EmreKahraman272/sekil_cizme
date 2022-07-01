
import turtle

def ucgen_çizme(b,re,k):
    turtle.pencolor(re)
    turtle.pensize(k)
    for i in range(3):
        turtle.forward(b)
        turtle.left(120)
    turtle.done()



def dikdortgen_cizme(re,k,d,f):
    turtle.color(re)
    turtle.pensize(k)
    turtle.forward(d)
    turtle.left(90)
    turtle.forward(f)
    turtle.left(90)
    turtle.forward(d)
    turtle.left(90)
    turtle.forward(f)
    turtle.left(90)
    turtle.done()


def daire_çizme(r,k,re):
    turtle.color(re)
    turtle.pensize(k)
    return turtle.circle(r)




def kare_cizme(n,re,k):
    for i in range(4):
        turtle.color(re)
        turtle.pensize(k)
        turtle.forward(n)
        turtle.right(90)

    turtle.done()


renkler = ['red', 'blue', 'green', 'yellow']
print(renkler)
re = str(input("Renk seçiniz."))
k = str(input("Kalınlık seçiniz." ))
secim = str(input("Ne çizmek istersiniz ?"))

if (secim == "daire"):
    r = int(input("Yarı çapı kaç olsun ?"))
    daire_çizme(r,k,re)
if (secim == "dikdörtgen"):
    d = int(input("Uzun kenar ne kadar uzun olsun ?"))
    f = int(input("Kısa kenar ne kadar uzun olsun ?"))
    dikdortgen_cizme(re,k,d,f)
if (secim == "ücgen"):
    b = int(input("Kenar uzunluğu ne kadar olsun ?"))
    ucgen_çizme(b,re,k)

if (secim == "kare"):
    n = int(input("Kenar uzunluğu ne kadar olsun ?"))
    kare_cizme(n,re,k)