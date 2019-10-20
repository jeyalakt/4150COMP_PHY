import multiprocessing as mp
def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    for i in range(0,1000):
        q = mp.Queue()
        p = mp.Process(target=foo, args=(q,))
        p.start()
        print(q.get())
        p.join()
        print (i)