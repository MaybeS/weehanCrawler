import multiprocessing as mp

def run(task, args):
    pool = mp.Pool()
    r = pool.map_async(task, args)
    pool.close()
    pool.join()
    return r.get()
