# 깊이 우선 탐색(DFS, Depth-First Search)

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

        if not i in [0, 1, 2]: # UP 연산자
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6]: # LEFT 연산자
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8]: # RIGHT 연산자
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]: # DOWN 연산자
            result.append(self.get_new_board(i, i+3, moves))
        return result
    
    # 객체를 출력할 때 사용한다.
    def __str__(self):
        return str(self.board[:3]) + "\n" + str(self.board[3:6]) + "\n" + str(self.board[6:]) + "\n" + "------------------" + "\n"
    
    # 객체를 비교할 때 사용한다.
    def __eq__(self, other):
        return self.board == other.board
    
if __name__ == "__main__":
    
    # 초기 상태
    puzzle = [1, 2, 3, 0, 4, 6, 7, 5, 8]

    # 목표상태
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # open 리스트와 closed 리스트
    open_queue = []
    closed_queue = []

    # 초기 상태를 open 리스트에 추가
    open_queue.append(State(puzzle, goal))

    while open_queue:
        # 스택의 맨 뒤에서 상태를 꺼냄
        current = open_queue.pop()
        
        # 현재 상태 출력
        print(current)
        
        # 목표 상태에 도달했는지 확인
        if current.board == goal:
            print("탐색 성공")
            break

        # 현재 상태를 closed 리스트에 추가
        closed_queue.append(current)
        
        # 자식 노드 확장
        for state in current.expend(current.moves + 1):
            # 이미 탐색한 상태가 아니면 open 리스트에 추가
            if state not in closed_queue and state not in open_queue:
                open_queue.append(state)
