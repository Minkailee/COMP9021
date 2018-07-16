# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distint lines,
# two of which having the same slope, the other two having the same slope too.
# The Parallelogram has a method, divides_into_two_parallelograms(), that determines
# where a line, provide as arguments, can split the object into two smaller parallelograms.
#
# Written by Minkai Li z5095946 for COMP9021


from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Line:
    def __init__(self,pt1,pt2):
        if pt1.x==pt2.x and pt1.y==pt2.y:
            print('Cannot create line')
        else:
            self.pt1=Point(pt1.x,pt1.y)
            self.pt2=Point(pt2.x,pt2.y)
            self.k=self._k()
            self.b=self._b()
    def _k(self):
        if not self.pt2.x==self.pt1.x:
            return (self.pt2.y-self.pt1.y)/(self.pt2.x-self.pt1.x)
        return float("inf")
    def _b(self):
        if not self.pt2.x==self.pt1.x:
            return self.pt1.y-self.k*self.pt1.x
        return self.pt1.x
class Parallelogram:
    def __init__(self,l1,l2,l3,l4):
        L=[(l1.k,l1.b),(l2.k,l2.b),(l3.k,l3.b),(l4.k,l4.b)]
        SL=sorted(L,key=lambda t:t[0])
        if not (SL[0][0]==SL[1][0] and SL[1][0]!=SL[2][0] and SL[2][0]==SL[3][0] and SL[0][1]!=SL[1][1] and SL[2][1]!=SL[3][1]):
            print('Cannot create parallelogram')
        else:
            self.l1=Line(l1.pt1,l1.pt2)
            self.l2=Line(l2.pt1,l2.pt2)
            self.l3=Line(l3.pt1,l3.pt2)
            self.l4=Line(l4.pt1,l4.pt2)
            self.KB=SL
    def divides_into_two_parallelograms(self, line):
        if (line.k==self.KB[0][0] and (line.b<max(self.KB[0][1],self.KB[1][1]) and line.b>min(self.KB[0][1],self.KB[1][1]))) or (line.k==self.KB[2][0] and (line.b<max(self.KB[2][1],self.KB[3][1]) and line.b>min(self.KB[2][1],self.KB[3][1]))):
            return True
        return False

    
