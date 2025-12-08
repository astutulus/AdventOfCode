# A coordinate in 3D space (expects a string: "1,2,3\n")
class Point:

    unconnected: set = set()

    def __init__(self, data: str):
        coords = data.strip().split(',')
        self.x = int(coords[0])
        self.y = int(coords[1])
        self.z = int(coords[2])
        Point.unconnected.add(self)

    def connect(self):
        if self in Point.unconnected:
            Point.unconnected.remove(self)

    @classmethod
    def all_connected(cls) -> bool:
        return len(cls.unconnected) == 0

    # Define equals, to enable comparison
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x == other.x and
                self.y == other.y and
                self.z == other.z)
    
    # Make hashable so that it can be put in a set
    def __hash__(self):
        # Combine hashes of attributes
        return hash((self.x, self.y, self.z))


# A distance between two coordinates (with a record of which!)
class Edge:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.length: float = self.pythagoras(p=self.p1, q=self.p2)

    # Define less-than, to make a list of edges sortable by length
    def __lt__(self, other):
        if not isinstance(other, Edge):
            return NotImplemented
        return self.length < other.length
    
    # Revision: https://www.bbc.co.uk/bitesize/guides/zq8x8mn/revision/5
    @classmethod
    def pythagoras(cls, p: Point, q: Point) -> float:
        # Flat triangle
        a_sq = pow(p.x - q.x, 2)
        b_sq = pow(p.y - q.y, 2)
        c_sq = a_sq + b_sq
        # Upright triangle
        z_sq = pow(p.z - q.z, 2)
        return pow(c_sq + z_sq, (1/2))
    
    def connect_juntions(self):
        self.p1.connect()
        self.p2.connect()


def solve(filepath: str):
    points: list[Point] = []
    edges: list[Edge] = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            new_point = Point(data=line)
            for point in points:
                edges.append(Edge(p1=point, p2=new_point))
            points.append(new_point)

    # Get the shortest to the front
    edges.sort()

    # Make the ten shortest into circuits
    list_of_circuit_sets: list[set[Point]] = []

    # --------------------------------------------------
    # Run through all edges, adding 'juntions' to set(s)
    # --------------------------------------------------
    for edge in edges:
        j1: Point = edge.p1
        j2: Point = edge.p2
        
        circuit_with_j1 = None
        circuit_with_j2 = None
        for circuit in list_of_circuit_sets:
            for juntion in circuit:
                if juntion == j1:
                    circuit_with_j1 = circuit
                if juntion == j2:
                    circuit_with_j2 = circuit

        # Each end found
        if circuit_with_j1 and circuit_with_j2:
            # Each end in same circuit!!
            if circuit_with_j1 == circuit_with_j2:
                pass
            # Each end in different circuits!!
            else:
                merged_circuit: set[Point] = circuit_with_j1 | circuit_with_j2
                list_of_circuit_sets.append(merged_circuit)

                list_of_circuit_sets.remove(circuit_with_j2)
                list_of_circuit_sets.remove(circuit_with_j1)

        # One end in a circuit, so add the other end
        elif circuit_with_j1:
            circuit_with_j1.add(j2)
        elif circuit_with_j2:
            circuit_with_j2.add(j1)

        # Not yet seen
        else:
            new_circuit: set[Point] = {j1, j2}
            list_of_circuit_sets.append(new_circuit)

        edge.connect_juntions()

        # Stop exactly when final juntion is connected
        if Point.all_connected():
            final_edge = edge
            break

    return final_edge.p1.x * final_edge.p2.x
            
if __name__ == "__main__":
    filename = ["debug",    # index 0
                "example",  # index 1
                "input"]    # index 2
    print(f"Answer: {solve(f"2025\\day8\\{filename[2]}.txt")}")  # Set filename 