                import math

                class Ponto2D:
                    def __init__(self, x, y):
                        self.x = x
                        self.y = y

                class Ponto2DUtils:
                    @staticmethod
                    def distance(P1, P2):
                        return math.sqrt((P2.x - P1.x)**2 + (P2.y - P1.y)**2)

                    @staticmethod
                    def distance_to_origin(P):
                        return math.sqrt(P.x**2 + P.y**2)

                    @staticmethod
                    def quadrant(P):
                        if P.x > 0 and P.y > 0:
                            return 1
                        elif P.x < 0 and P.y > 0:
                            return 2
                        elif P.x < 0 and P.y < 0:
                            return 3
                        elif P.x > 0 and P.y < 0:
                            return 4
                        else:
                            return 0