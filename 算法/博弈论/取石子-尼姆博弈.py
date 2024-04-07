"""
作者：legionb
日期：2024年04月06日
"""
# 有n堆石子，每堆石子的数量是a1, a2, a3……，二个人依次从这些石子堆中的一个拿取任意的石子，至少一个，最后一个拿光石子的人胜利
#
# n = 1: 先手全拿，先手必胜。
#
# n = 2:有两种情况，一种可能相同，一种情况一堆比另一堆少（多）
#
# (m, m)按照“有一学一，照猫画猫”法，先手必输。
#
# (m, M)先手先从多的一堆中拿出(M - m)个，此时后手面对(m, m)的局面先手必胜。
#
# 术语: 正经人称(m, m)的局面为奇异局势
#
# n = 3:(m, m, M)先手必胜局，先手可以先拿M, 之后变成了(m, m, 0)的局面，是不是很熟悉
#
#
# (a1, a2, a3)的话，举个例子(1, 2, 3), 先手取完之后可能的局面为(0, 2, 3), (1, 1, 3), (1, 0, 3), (1, 2, 2), (1, 2, 1), (1, 2, 0)都是之前讲过的，情况如下：

#题目：给定n堆石子，两位玩家轮流操作，每次操作可以从任意一堆石子中拿走任意数量的石子（可以拿完，不能不拿），最后无法进行操作的人视作失败
#问如果两人都采用最优策略，先手是否必胜
