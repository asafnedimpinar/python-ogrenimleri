from turtle import *

shape('turtle')
pensize(4)
color('blue')
speed(2)

w = Screen()
w.setup(width=800, height=700)

yazma_modu = False  # Yazma modu başlangıçta kapalı

def solaDon():
    left(10)

def sagaDon():
    right(10)

def ileri():
    forward(10)

def geri():
    backward(10)

def yazma():
    global yazma_modu
    yazma_modu = True

def yaz():
    global yazma_modu
    yazma_modu = False

def hareket(event=None):
    if yazma_modu:
        pencolor('red')  # Yazma modunda ise kalem rengini kırmızı yap
        write('Yazma Modu', font=('Arial', 14, 'normal'))  # Ekrana 'Yazma Modu' yazısı yaz
    else:
        pencolor('blue')  # Yaz modunda ise kalem rengini mavi yap

    # Herhangi bir tuşa basıldığında hareket fonksiyonu çalışsın
    if event:
        w.onkeypress(None, event.char)
    listen()  # Tuş dinleme tekrar başlatılır

w.onkeypress(solaDon, 'a')
w.onkeypress(sagaDon, 'd')
w.onkeypress(ileri, 'w')
w.onkeypress(geri, 's')
w.onkeypress(yazma, 'f')
w.onkeypress(yaz, 'g')

listen()
w.listen()
w.onkeypress(hareket)  # Herhangi bir tuşa basıldığında hareket fonksiyonu çalışsın
w.mainloop()