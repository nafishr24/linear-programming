from isoline import *

maximize(
        a1=2, b1=1, c1=300,   # Batasan 1: 2x + y ≤ 300
        a2=1, b2=2, c2=300,   # Batasan 2: x + 2y ≤ 300
        g=150, h=100,         # Fungsi tujuan: Z = 150x + 100y
        x_max=300, y_max=300  # Batas plot
)