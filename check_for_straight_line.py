#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
#Check if these points make a straight line in the XY plane.



class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0]-coordinates[0][0] != 0:
            m = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
            c = coordinates[0][1] - m*coordinates[0][0]
            
            t = 0
            for i in coordinates:
                if i[1] - m * i[0] - c == 0:
                    t += 1
            if len(coordinates) == t:
                return True 
            if len(coordinates) !=t :
                return False
        else:
            u = 0
            v = coordinates[0][0]
            for i in coordinates:
                if i[0] == v:
                    u += 1
            if len(coordinates) == u :
                return True
            else:
                return False