#De Casteljau’s algorithm
import math
def quadratic_bezier_sum(t, w):
    t2 = t * t
    mt = 1-t
    mt2 = mt * mt
    return w[0]*mt2 + w[1]*2*mt*t + w[2]*t2
def draw_quadratic_bez(p1, p2, p3, t_step): #takes the 3 points of bezier and the step by which t is incremented
    t = 0
    arr = []
    while (t < 1):
        x = quadratic_bezier_sum(t, (p1[0], p2[0], p3[0]))
        y = quadratic_bezier_sum(t, (p1[1], p2[1], p3[1]))
        G_CodeFile = open('BezierLines3.nc','a')
        G_CodeFile.write("G1 X"+str(x) + " Y" + str(y)+" \n")
        G_CodeFile.close()
        t += t_step # 1000 iterations. If you want the curve to be really
                       # fine grained, consider "t += 0.0001" for ten thousand iterations.
open('BezierLines.nc', 'w').close()
draw_quadratic_bez((35.3, 20.5),(22.5, 5.1),(31.3, -0.1), 0.02) #1/0.02 = 50 actions
