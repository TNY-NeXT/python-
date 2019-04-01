from time import ctime, sleep
import threading

def music(fund):
    for i in range(2):
        print('I was listening to %s. %s' % (fund, ctime()))
        sleep(1)
    print('end listening')


def movie(func):
    for i in range(2):
        print('I was at the %s. %s' % (func, ctime()))
        sleep(5)
    print('end watching')


t_list = []
t1 = threading.Thread(target=music, args=('月半弯',))
t_list.append(t1)
t2 = threading.Thread(target=movie, args=('蝙蝠侠',))
t_list.append(t2)

if __name__ == '__main__':  # 该语句的作用是：只在 main 主程序里执行以下的语句。
    # music('月半弯')
    # movie('蝙蝠侠')

    # t1.setDaemon(True)  # 谁设置daemon谁的优先级就最低。
    t2.setDaemon(True)  #守护进程的意思
    for i in t_list:
        # i.setDaemon(True)  # 为什么这里的 i 是属于主函数的？
        i.start()
        # print(threading.current_thread())
    # i.join()  #  设置了daemon 就不用设置join了。

    # print(threading.current_thread())
    # print(threading.active_count())
    print('all over %s' % ctime())
