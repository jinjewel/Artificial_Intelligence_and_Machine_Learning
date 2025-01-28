# 너비 우선 탐색(BFS, breadth-first search)

# 상태를 나타내는 클래스
class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.goal = goal
        self.moves = moves

    # i1과 i2를 교환하여 새로운 상태를 반환한다.
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)
    
    # 자식 노드를 확장하여서 리스트에 저장하여 반환한다.
    def expend(self, moves):
        result = []
        i = self.board.index(0) # 숫자 0(빈칸)의 위치를 찾는다.

        if not i in [2, 5, 8]: # RIGHT 연산자
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]: # DOWN 연산자
            result.append(self.get_new_board(i, i+3, moves))  
        if not i in [0, 1, 2]: # UP 연산자
            result.append(self.get_new_board(i, i-3, moves)) 
        if not i in [0, 3, 6]: # LEFT 연산자 
            result.append(self.get_new_board(i, i-1, moves))        
            
        return result
    
    # 객체를 출력할 때 사용한다.
    def __str__(self):
        return str(self.board[:3]) + "\n" + str(self.board[3:6]) + "\n" + str(self.board[6:]) + "\n" + "------------------" + "\n"
    
    # 객체를 비교할 때 사용한다.
    def __eq__(self, other):
        return self.board == other.board
    
if __name__ == "__main__":
    
    # 초기 상태
    puzzle = [2, 8, 3, 1, 6, 4, 7, 0, 5]

    # 목표상태
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    # open 리스트
    open_queue = []
    open_queue.append(State(puzzle, goal))
    closed_queue = []
    moves = 0
    count = 0
    while len(open_queue) != 0:
        count += 1
        current = open_queue.pop() # open 리스트의 앞에서 삭제한다.
        print(current)

        if count == 10:
            break

        if current.board == goal:
            print("탐색 성공")
            print(count)
            break

        moves = current.moves + 1
        closed_queue.append(current)
        for state in current.expend(moves):

            # 이미 거처간 노드이면 
            if (state in closed_queue) or (state in open_queue):
                continue  # 노드를 버린다.
            else:
                open_queue.append(state) # open 리스트에 추가한다.