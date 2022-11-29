import pygame
import string

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        action = False

        #Get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                   
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


    
alphabets = [i for i in string.ascii_uppercase]


A1 = pygame.image.load("hangmanonpygame/buttons/A1.png")
B1 = pygame.image.load("hangmanonpygame/buttons/B1.png")
C1 = pygame.image.load("hangmanonpygame/buttons/C1.png")
D1 = pygame.image.load("hangmanonpygame/buttons/D1.png")
E1 = pygame.image.load("hangmanonpygame/buttons/E1.png")
F1 = pygame.image.load("hangmanonpygame/buttons/F1.png")
G1 = pygame.image.load("hangmanonpygame/buttons/G1.png")
H1 = pygame.image.load("hangmanonpygame/buttons/H1.png")
I1 = pygame.image.load("hangmanonpygame/buttons/I1.png")
J1 = pygame.image.load("hangmanonpygame/buttons/J1.png")
K1 = pygame.image.load("hangmanonpygame/buttons/K1.png")
L1 = pygame.image.load("hangmanonpygame/buttons/L1.png")
M1 = pygame.image.load("hangmanonpygame/buttons/M1.png")
N1 = pygame.image.load("hangmanonpygame/buttons/N1.png")
O1 = pygame.image.load("hangmanonpygame/buttons/O1.png")
P1 = pygame.image.load("hangmanonpygame/buttons/P1.png")
Q1 = pygame.image.load("hangmanonpygame/buttons/Q1.png")
R1 = pygame.image.load("hangmanonpygame/buttons/R1.png")
S1 = pygame.image.load("hangmanonpygame/buttons/S1.png")
T1 = pygame.image.load("hangmanonpygame/buttons/T1.png")
U1 = pygame.image.load("hangmanonpygame/buttons/U1.png")
V1 = pygame.image.load("hangmanonpygame/buttons/V1.png")
W1 = pygame.image.load("hangmanonpygame/buttons/W1.png")
X1 = pygame.image.load("hangmanonpygame/buttons/X1.png")
Y1 = pygame.image.load("hangmanonpygame/buttons/Y1.png")
Z1 = pygame.image.load("hangmanonpygame/buttons/Z1.png")

A2 = pygame.image.load("hangmanonpygame/buttons/A2.png")
B2 = pygame.image.load("hangmanonpygame/buttons/B2.png")
C2 = pygame.image.load("hangmanonpygame/buttons/C2.png")
D2 = pygame.image.load("hangmanonpygame/buttons/D2.png")
E2 = pygame.image.load("hangmanonpygame/buttons/E2.png")
F2 = pygame.image.load("hangmanonpygame/buttons/F2.png")
G2 = pygame.image.load("hangmanonpygame/buttons/G2.png")
H2 = pygame.image.load("hangmanonpygame/buttons/H2.png")
I2 = pygame.image.load("hangmanonpygame/buttons/I2.png")
J2 = pygame.image.load("hangmanonpygame/buttons/J2.png")
K2 = pygame.image.load("hangmanonpygame/buttons/K2.png")
L2 = pygame.image.load("hangmanonpygame/buttons/L2.png")
M2 = pygame.image.load("hangmanonpygame/buttons/M2.png")
N2 = pygame.image.load("hangmanonpygame/buttons/N2.png")
O2 = pygame.image.load("hangmanonpygame/buttons/O2.png")
P2 = pygame.image.load("hangmanonpygame/buttons/P2.png")
Q2 = pygame.image.load("hangmanonpygame/buttons/Q2.png")
R2 = pygame.image.load("hangmanonpygame/buttons/R2.png")
S2 = pygame.image.load("hangmanonpygame/buttons/S2.png")
T2 = pygame.image.load("hangmanonpygame/buttons/T2.png")
U2 = pygame.image.load("hangmanonpygame/buttons/U2.png")
V2 = pygame.image.load("hangmanonpygame/buttons/V2.png")
W2 = pygame.image.load("hangmanonpygame/buttons/W2.png")
X2 = pygame.image.load("hangmanonpygame/buttons/X2.png")
Y2 = pygame.image.load("hangmanonpygame/buttons/Y2.png")
Z2 = pygame.image.load("hangmanonpygame/buttons/Z2.png")



A = pygame.transform.scale(A1,  (40, 40))
B = pygame.transform.scale(B1,  (40, 40))
C = pygame.transform.scale(C1,  (40, 40))
D = pygame.transform.scale(D1,  (40, 40))
E = pygame.transform.scale(E1,  (40, 40))
F = pygame.transform.scale(F1,  (40, 40))
G = pygame.transform.scale(G1,  (40, 40))
H = pygame.transform.scale(H1,  (40, 40))
I = pygame.transform.scale(I1,  (40, 40))
J = pygame.transform.scale(J1,  (40, 40))
K = pygame.transform.scale(K1,  (40, 40))
L = pygame.transform.scale(L1,  (40, 40))
M = pygame.transform.scale(M1,  (40, 40))
N = pygame.transform.scale(N1,  (40, 40))
O = pygame.transform.scale(O1,  (40, 40))
P = pygame.transform.scale(P1,  (40, 40))
Q = pygame.transform.scale(Q1,  (40, 40))
R = pygame.transform.scale(R1,  (40, 40))
S = pygame.transform.scale(S1,  (40, 40))
T = pygame.transform.scale(T1,  (40, 40))
U = pygame.transform.scale(U1,  (40, 40))
V = pygame.transform.scale(V1,  (40, 40))
W = pygame.transform.scale(W1,  (40, 40))
X = pygame.transform.scale(X1,  (40, 40))
Y = pygame.transform.scale(Y1,  (40, 40))
Z = pygame.transform.scale(Z1,  (40, 40))


alpha = [
Button(10 ,400, A) ,
Button(55 ,400, B) ,
Button(100,400, C) ,
Button(145,400, D) ,
Button(190,400, E) ,
Button(235,400, F) ,
Button(280,400, G) ,
Button(325,400, H) ,
Button(370,400, I) ,
Button(415,400, J) ,
Button(460,400, K) ,
Button(10 ,450, L) ,
Button(55 ,450, M) ,
Button(100,450, N) ,
Button(145,450, O) ,
Button(190,450, P) ,
Button(235,450, Q) ,
Button(280,450, R) ,
Button(325,450, S) ,
Button(370,450, T) ,
Button(415,450, U) ,
Button(460,450, V) ,
Button(10 ,500, W) ,
Button(55 ,500, X) ,
Button(100,500, Y) ,
Button(145,500, Z) 
]

A2 = pygame.transform.scale(A2,  (40, 40))
B2 = pygame.transform.scale(B2,  (40, 40))
C2 = pygame.transform.scale(C2,  (40, 40))
D2 = pygame.transform.scale(D2,  (40, 40))
E2 = pygame.transform.scale(E2,  (40, 40))
F2 = pygame.transform.scale(F2,  (40, 40))
G2 = pygame.transform.scale(G2,  (40, 40))
H2 = pygame.transform.scale(H2,  (40, 40))
I2 = pygame.transform.scale(I2,  (40, 40))
J2 = pygame.transform.scale(J2,  (40, 40))
K2 = pygame.transform.scale(K2,  (40, 40))
L2 = pygame.transform.scale(L2,  (40, 40))
M2 = pygame.transform.scale(M2,  (40, 40))
N2 = pygame.transform.scale(N2,  (40, 40))
O2 = pygame.transform.scale(O2,  (40, 40))
P2 = pygame.transform.scale(P2,  (40, 40))
Q2 = pygame.transform.scale(Q2,  (40, 40))
R2 = pygame.transform.scale(R2,  (40, 40))
S2 = pygame.transform.scale(S2,  (40, 40))
T2 = pygame.transform.scale(T2,  (40, 40))
U2 = pygame.transform.scale(U2,  (40, 40))
V2 = pygame.transform.scale(V2,  (40, 40))
W2 = pygame.transform.scale(W2,  (40, 40))
X2 = pygame.transform.scale(X2,  (40, 40))
Y2 = pygame.transform.scale(Y2,  (40, 40))
Z2 = pygame.transform.scale(Z2,  (40, 40))


alpha_1 = [
Button(10 ,400, A2) ,
Button(55 ,400, B2) ,
Button(100,400, C2) ,
Button(145,400, D2) ,
Button(190,400, E2) ,
Button(235,400, F2) ,
Button(280,400, G2) ,
Button(325,400, H2) ,
Button(370,400, I2) ,
Button(415,400, J2) ,
Button(460,400, K2) ,
Button(10 ,450, L2) ,
Button(55 ,450, M2) ,
Button(100,450, N2) ,
Button(145,450, O2) ,
Button(190,450, P2) ,
Button(235,450, Q2) ,
Button(280,450, R2) ,
Button(325,450, S2) ,
Button(370,450, T2) ,
Button(415,450, U2) ,
Button(460,450, V2) ,
Button(10 ,500, W2) ,
Button(55 ,500, X2) ,
Button(100,500, Y2) ,
Button(145,500, Z2) 
]