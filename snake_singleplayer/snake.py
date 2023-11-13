class Snake:
    def __init__(self, x: int, y: int):
        self.body = [[y, x], [y+1, x], [y+2, x]]
        self.facing = "N"
        self.fruits = 0
        self.changing_facing = 0

    def move(self):
        """ Method to move the snake into the map coordinates """
        for index in reversed(range(1, len(self.body))):
            self.body[index] = self.body[index-1].copy()

        match self.facing:
            case "N":
                self.body[0][0] -= 1
            case "S":
                self.body[0][0] += 1
            case "E":
                self.body[0][1] -= 1
            case "W":
                self.body[0][1] += 1

    def change_facing(self, facing: str):
        """ Method to change the facing of the snake """
        if facing == "N" and self.facing in ["E", "W"]:
            self.facing = facing
        elif facing == "S" and self.facing in ["E", "W"]:
            self.facing = facing
        elif facing == "E" and self.facing in ["N", "S"]:
            self.facing = facing
        elif facing == "W" and self.facing in ["N", "S"]:
            self.facing = facing
        self.changing_facing += 1

    def check_lose_conditions(self) -> bool:
        """ Method to verify if player died """
        if not 0 <= self.body[0][0] <= 19 or not 0 <= self.body[0][1] <= 19:  # outside map
            return True
        elif self.body[0] in self.body[1:]:  # on his body
            return True
        return False

    def check_fruit_condition(self, fruit_coords: tuple[int, int]) -> bool:
        """ Method to check if the head is eating a fruit """
        if list(fruit_coords) == self.body[0]:
            return True
        return False

    def check_win_condition(self) -> bool:
        """ Method to check if the game is win """
        if len(self.body) >= 400:
            return True
        return False

    def extend(self):
        """ Method to add a part to the body """
        y1, x1 = self.body[-1]
        y2, x2 = self.body[-2]
        if y1 == y2 + 1 and x1 == x2:
            # N
            self.body.append([y1+1, x1])
        elif y1 == y2 - 1 and x1 == x2:
            # S
            self.body.append([y1-1, x1])
        elif y1 == y2 and x1 == x2 + 1:
            # E
            self.body.append([y1, x1-1])
        elif y1 == y2 and x1 == x2 - 1:
            # W
            self.body.append([y1, x1+1])
