# print(2**10)
# print(bin(10))
# print(0b1010)
# print({0b1010:'ㅅ'})
# a = [1,2,3]
# print(a[0b10])
# print(1024*20*20)
# print(0b111111111)
# print(2**9)
# print(str(bin(0b111111111)).count('1'))
# print()
#
# print(1 << (1-1))
# print(1 << (2-1))
# print(1 << (3-1))
# print(str(bin(4)))
# print(str(bin(256)))
# print(1 << (7-1))
#
# append_q(q, visited, prev_cnt, nr, nc, new_coin, last_coin)
#

board = [[1,2,3,4], [5, 6,7,8], [9,10,11,12], [13,14,15,16]]

new_board = [line for line in zip(*board)]
print(new_board[::-1])
print(new_board)