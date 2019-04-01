 import time
 import threading

 begin = time.time()


 def foo(n):
     print('foo %s' % n)
    time.sleep(1)
    print('end the foo')
     return


 def bar(n):
     print('bar %s' % n)
     time.sleep(3)
     print('end the bar')
     return

#串行执行花费4秒多
# foo(2)
# bar(3)

#并行执行3秒多
 t1 = threading.Thread(target=foo, args=(2,))
 t2 = threading.Thread(target=bar, args=(2,))
 t1.start()
 t2.start()
 print('...the main function....')
 t1.join()
 t2.join()
 end = time.time()
 print(end-begin)
