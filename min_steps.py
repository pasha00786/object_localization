def coverPoints(self, A, B):
        import math
        min_step = 0
        root_2 = (2**0.5)
        for i in range(len(A) - 1 ):
            dist = ((A[i] - A[i+1])**2 + (B[i] - B[i+1])**2)**0.5
            if dist <= root_2:
                min_step = min_step + 1
            elif (dist % root_2) == 0:
                min_step = min_step + (dist / root_2)
            else:
                min_step = min_step + math.ceil(dist / root_2)
        return min_step