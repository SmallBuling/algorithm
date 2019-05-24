'''
list实现堆
入栈：list.append（）（增加元素到list的尾部）
出栈：list.pop()  （pop里面不要添加参数，这样它pop的是list的最后一个元素）
上面的结构就实现了一个先进后出的堆栈，栈顶在list的尾部

list实现队列
入队：list.append（）（增加元素到list的尾部）
出队：list.pop(0)
队头在list尾部，队尾在list[0]
问题：出队比较慢，因为出队完了需要将后面的元素一个一个往前挪
'''
if __name__ == '__main__':
    stack = [1,2,3]
    stack.append(4)
    print(stack)
    stack.pop()
    print(stack)

    queue = ['li','ming','liang']
    queue.append('xiaoli')
    print(queue)
    queue.pop(0)
    print(queue)






