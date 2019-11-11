class HeapNode:
    def __init__(self, point, segment, state, optional_segment=None):
        self.point = point
        self.segment = segment
        self.state = state  # 0 - start of segment, 1 - end of segment, 2 - intersection
        self.optional_segment = optional_segment

    def __repr__(self):
        if self.state == 2:
            return 'Intersection: ' + str(self.point) + str(self.segment) + str(self.optional_segment)
        elif self.state == 1:
            return 'End of the point: ' + str(self.point) + '  ' + str(self.segment)
        else:
            return 'Beginning of the point: ' + str(self.point) + '  ' + str(self.segment)

    def __lt__(self, other):
        if self.point.x == other.point.x:
            return self.point.y > other.point.y
        else:
            return self.point.x < other.point.x
