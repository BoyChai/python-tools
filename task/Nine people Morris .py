# 棋盘
def draw_board(g):
    board = [' '] * 24

    """
    绘制游戏棋盘

    Parameters:
    - board (list): 游戏棋盘状态列表
    """

    for i in range(0,len(g)):
        if g[i] == 1:
            board[i] = 'X'
        if g[i] == 2:
            board[i] = 'O'


    print(board[0] + '-----------' + board[1] + '-----------' + board[2])
    print('|' + '           |           ' + '|')
    print('|' + '           |           ' + '|')
    print('|' + '   ' + board[3] + '-------' + board[4] + '-------' + board[5] + '   ' + '|')
    print('|' + '   ' + '|' + '       |       ' + '|' + '   ' + '|')
    print('|' + '   ' + '|' + '       |       ' + '|' + '   ' + '|')
    print('|' + '   ' + '|' + '   ' + board[6] + '---' + board[7] + '---' + board[8] + '   ' + '|' + '   ' + '|')
    print('|' + '   ' + '|' + '   ' + '|' + '       ' + '|' + '   ' + '|' + '   ' + '|')
    print(board[9] + '---' + board[10] + '---' + board[11] + '       ' + board[12] + '---' + board[13] + '---' + board[
        14])
    print('|' + '   ' + '|' + '   ' + '|' + '       ' + '|' + '   ' + '|' + '   ' + '|')
    print('|' + '   ' + '|' + '   ' + board[15] + '---' + board[16] + '---' + board[17] + '   ' + '|' + '   ' + '|')
    print('|' + '   ' + '|' + '       |       ' + '|' + '   ' + '|')
    print('|' + '   ' + '|' + '       |       ' + '|' + '   ' + '|')
    print('|' + '   ' + board[18] + '-------' + board[19] + '-------' + board[20] + '   ' + '|')
    print('|' + '           |           ' + '|')
    print('|' + '           |           ' + '|')
    print(board[21] + '-----------' + board[22] + '-----------' + board[23])


def request_location(question_str):
    """
    通过控制台请求用户输入一个整数，表示棋盘上的位置。

    参数:
    - question_str (str): 提示用户输入的字符串。

    返回:
    - int: 表示棋盘上的位置的整数。
    """
    while True:
        try:
            # 获取用户输入的位置字符串
            location_str = input(question_str)
            # 将输入的字符串转换为整数
            location = int(location_str)

            # 检查位置是否在合法范围内
            if 0 <= location <= 23:
                return location
            else:
                raise RuntimeError("位置必须在0到23之间。")
        except ValueError:
            print("请输入一个整数。")



# 任务1: 检查邻接关系
def is_adjacent(i, j):
    """
    检查棋盘上两点是否相邻。

    参数:
    - i (int): 第一个点的索引。
    - j (int): 第二个点的索引。

    返回:
    - bool: 如果两点相邻，则为True，否则为False。
    """
    # 定义点之间的邻接关系
    adjacency_map = {
        0: [1, 9],
        1: [0, 2, 4],
        2: [1, 14],
        3: [10, 4],
        4: [1, 3, 5, 7],
        5: [4, 13],
        6: [11, 7],
        7: [4, 6, 8],
        8: [7, 12],
        9: [0, 10, 21],
        10: [3, 9, 11, 18],
        11: [6, 10, 15],
        12: [8, 13, 17],
        13: [5, 12, 14, 20],
        14: [2, 13, 23],
        15: [11, 16],
        16: [15, 17, 19],
        17: [12, 16],
        18: [10, 19],
        19: [16, 18, 20, 22],
        20: [13, 19],
        21: [9, 22],
        22: [19, 21, 23],
        23: [14, 22]
    }

    # 检查 j 是否在 i 的邻接点列表中
    return j in adjacency_map[i]


# 任务2: 设置游戏状态
def new_game():
    """
    创建一个新游戏的游戏状态。

    返回:
    - list: 包含四个元素的列表，表示新游戏的状态。
    """
    # 初始化棋盘，玩家1和玩家2的未放置棋子数量，以及当前轮到的玩家
    initial_board = [0] * 24
    player1_counters = 9
    player2_counters = 9
    active_player = 1

    # 返回游戏状态列表
    return [initial_board, player1_counters, player2_counters, active_player]


# 任务3: 计数棋子

def remaining_counters(g):
    """
    计算当前玩家的总棋子数。

    参数:
    - g (list): 包含四个元素的列表，表示游戏状态。

    返回:
    - int: 当前玩家可用的总棋子数。
    """
    # 获取当前玩家的索引
    player_index = g[3]

    # 获取当前玩家未放置的棋子数量和棋盘上的棋子数量
    unused_counters = g[player_index]
    placed_counters = g[0].count(player_index)

    # 返回总棋子数
    return unused_counters + placed_counters


# 任务4: 检查磨坊

def is_in_mill(g, i):
    """
    检查给定点是否在磨坊中。

    参数:
    - g (list): 包含游戏状态的列表。
    - i (int): 要检查的点的索引。

    返回:
    - int: -1，如果 i 超出 0-23 范围（含），或者点 i 上没有棋子
           0，如果点 i 上的棋子不在磨坊中
           1，如果点 i 上的棋子属于玩家 1 并且在一个或多个磨坊中
           2，如果点 i 上的棋子属于玩家 2 并且在一个或多个磨坊中
    """
    # 检查索引范围
    if i < 0 or i > 23 or g[0][i] == 0:
        return -1

    # 获取当前点的所有可能的磨坊组合
    mills = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [9, 10, 11], [12, 13, 14], [15, 16, 17],
        [18, 19, 20], [21, 22, 23],
        [0, 9, 21], [3, 10, 18], [6, 11, 15],
        [1, 4, 7], [16, 19, 22], [8, 12, 17],
        [5, 13, 20], [2, 14, 23]
    ]

    player = g[0][i]  # 获取当前点的玩家

    # 遍历所有可能的磨坊
    for mill in mills:
        if i in mill and all(g[0][j] == player for j in mill):
            return player

    return 0  # 当前点上的棋子不在任何磨坊中

# 任务5: 检查玩家是否可以移动

def player_can_move(g):
    """
    检查当前玩家是否有有效的移动。

    参数:
    - g (list): 包含游戏状态的列表。

    返回:
    - bool: 如果当前玩家有有效的移动，则为True，否则为False。
    """
    # 获取当前玩家
    active_player = g[3]

    # 检查是否有未放置的棋子，如果有，当前玩家可以放置棋子
    if g[1] > 0:
        return True

    # 遍历棋盘上的每个点，检查当前玩家的棋子是否有相邻的空位置可以移动
    for i in range(24):
        if g[0][i] == active_player:
            # 获取当前点的邻接点
            neighbors = [j for j in range(24) if is_adjacent(i, j) and g[0][j] == 0]
            if neighbors:
                return True  # 存在相邻的空位置，可以移动棋子

    return False  # 如果没有未放置的棋子且无法移动已放置的棋子，则返回False

# 任务6: 放置棋子

def place_counter(g, i):
    """
    在棋盘上的指定点放置当前活跃玩家的棋子。

    参数:
    - g (list): 包含游戏状态的列表。
    - i (int): 要放置棋子的点的索引。

    注意:
    - 如果指定的位置已经有棋子，该函数应引发 RuntimeError。
    - 该函数应该更新游戏状态 g 以将棋子放置在棋盘上，并减少当前玩家手中的棋子数量。
    """
    # 获取当前玩家
    active_player = g[3]

    # 检查指定的位置是否已经有棋子
    if g[0][i] != 0:
        raise RuntimeError("指定位置已经有棋子")

    # 在指定位置放置当前玩家的棋子
    g[0][i] = active_player

    # 减少当前玩家手中的棋子数量
    g[g[3]] -= 1

# 任务7: 移动棋子
def move_counter(g, i, j):
    """
    将当前活跃玩家的棋子从棋盘上的一个点移动到相邻的另一个点。

    参数:
    - g (list): 包含游戏状态的列表。
    - i (int): 要移动的棋子的起始点的索引。
    - j (int): 要移动的棋子的目标点的索引。

    注意:
    - 如果此移动不可能，即如果点 i 和 j 不相邻，点 i 不包含当前玩家的棋子，或者点 j 已经有棋子，则该函数应引发 RuntimeError。
    - 该函数应更新游戏状态以反映移动的棋子。
    """
    # 获取当前玩家
    active_player = g[3]

    # 检查点 i 和点 j 是否相邻
    if not is_adjacent(i, j):
        raise RuntimeError("点 "+str(i)+" 和点 "+str(j)+" 不相邻")

    # 检查点 i 上是否有当前玩家的棋子
    if g[0][i] != active_player:
        raise RuntimeError("点 "+str(i)+" 上没有当前玩家的棋子")

    # 检查点 j 是否已经有棋子
    if g[0][j] != 0:
        raise RuntimeError("点 "+str(j)+" 已经有棋子")

    # 移动棋子
    g[0][i] = 0  # 将点 i 上的棋子移走
    g[0][j] = active_player  # 在点 j 放置当前玩家的棋子

# 任务8: 移除对手的棋子
def remove_opponent_counter(g, i):
    """
    从棋盘上移除对手的棋子。

    参数:
    - g (list): 包含游戏状态的列表。
    - i (int): 要移除棋子的点的索引。

    注意:
    - 如果点 i 上的棋子不是对手的棋子，该函数应引发 RuntimeError。
    - 该函数应更新游戏状态 g 以移除指定点上的对手棋子。
    """
    # 获取当前玩家
    active_player = g[3]

    # 检查指定的位置上是否有对手的棋子
    if g[0][i] == active_player:
        raise RuntimeError("指定位置上的棋子不是对手的棋子")
    if g[0][i] == 0:
        raise RuntimeError("指定位置上没棋子")
    # 移除对手的棋子
    g[0][i] = 0


# 任务9
def turn(g):
    """
    模拟游戏的一回合。

    参数:
    - g (list): 包含游戏状态的列表。

    返回:
    - bool: 如果游戏结束，则为True；否则为False。
    """

    # 检查当前玩家是否无法移动或以其他方式输掉了游戏
    if not player_can_move(g):
        print("当前玩家无法移动，游戏结束。")
        return False

    # 如果当前玩家手中有一个或多个棋子
    if g[g[3]] > 0:
        while True:
            try:
                # 使用 request_location 向玩家询问放置棋子的位置
                location = request_location("请玩家"+str(g[3])+"输入要放置棋子的位置：")
                # 更新游戏状态 g 以放置此棋子
                place_counter(g, location)

                # 如果放置的棋子形成了磨坊，要求玩家提供要移除的对手棋子的位置，并更新游戏状态 g 以移除此棋子。
                if is_in_mill(g, location) != 0:
                    while True:
                        try:
                            opponent_location = request_location("请输入要移除的对手棋子位置：")
                            remove_opponent_counter(g, opponent_location)
                            break
                        except RuntimeError as e:
                            print(e)
                            # 如果玩家给出了无效的位置，重新提示玩家输入位置
                break
            except RuntimeError as e:
                print(e)
                # 如果玩家给出了无效的位置，重新提示玩家输入位置

    # 否则，当前玩家手中没有棋子
    else:
        while True:
            try:
                # 使用 request_location 向玩家询问要移动的棋子的位置
                source_location = request_location("请玩家"+str(g[3])+"输入要移动的棋子位置：")
                # 再次使用 request_location 向玩家询问要将该棋子移动到的位置
                target_location = request_location("请玩家"+str(g[3])+"输入要将棋子移动到的位置：")

                # 更新游戏状态 g 以移动此棋子
                move_counter(g, source_location, target_location)

                # 如果移动形成了磨坊，要求玩家提供要移除的对手棋子的位置，并更新游戏状态 g 以移除此棋子。
                if is_in_mill(g, target_location) != 0:
                    while True:
                        try:
                            opponent_location = request_location("请输入要移除的对手棋子位置：")
                            remove_opponent_counter(g, opponent_location)
                            break
                        except RuntimeError as e:
                            print(e)
                            # 如果玩家给出了无效的位置，重新提示玩家输入位置
                break
            except RuntimeError as e:
                print(e)
                # 如果玩家给出了无效的位置，重新提示玩家输入两个位置

    # 更新游戏状态以切换当前玩家
    g[3] = 3 - g[3]

    # 返回 True 表示游戏尚未结束
    return True

# 任务10
def save_state(g, filename):
    """
    将游戏状态保存到文本文件中。

    参数:
    - g (list): 包含游戏状态的列表。
    - filename (str): 要保存游戏状态的文件名。

    注意:
    - 如果无法保存文件，将引发 RuntimeError。
    """
    try:
        with open(filename, 'w') as file:
            # 保存棋盘状态
            file.write(','.join(map(str, g[0])) + '\n')
            # 保存玩家1的未放置棋子数量
            file.write(str(g[1]) + '\n')
            # 保存玩家2的未放置棋子数量
            file.write(str(g[2]) + '\n')
            # 保存当前轮到的玩家
            file.write(str(g[3]) + '\n')
    except Exception as e:
        raise RuntimeError(f"无法保存游戏状态到文件 {filename}: {e}")
def load_state(filename):
    """
    从文本文件中加载游戏状态。

    参数:
    - filename (str): 包含游戏状态的文件名。

    返回:
    - list: 包含游戏状态的列表。
    """
    try:
        with open(filename, 'r') as file:
            # 读取棋盘状态
            board_line = file.readline().strip()
            board = list(map(int, board_line.split(',')))
            # 读取玩家1的未放置棋子数量
            player1_counters = int(file.readline().strip())
            # 读取玩家2的未放置棋子数量
            player2_counters = int(file.readline().strip())
            # 读取当前轮到的玩家
            active_player = int(file.readline().strip())

            # 返回加载的游戏状态
            return [board, player1_counters, player2_counters, active_player]
    except Exception as e:
        raise RuntimeError(f"无法从文件 {filename} 加载游戏状态: {e}")


def play_game():
    """
    模拟游戏过程，创建新的游戏状态并反复调用 turn(g)。
    一旦游戏结束，显示获胜者。
    """
    print("欢迎来到九人莫里斯游戏！")

    # 创建新游戏
    game_state = new_game()

    while True:
        # 打印当前棋盘
        draw_board(game_state[0])

        # 模拟一回合
        result = turn(game_state)

        # 判断游戏是否结束
        if not result:
            # 游戏结束，显示获胜者
            winner = "玩家 1" if remaining_counters(game_state) <= 0 else "玩家 2"
            print(f"\n游戏结束！{winner} 获胜！")
            break


# 调用 play_game() 函数开始游戏
play_game()
