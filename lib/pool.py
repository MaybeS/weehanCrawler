import multiprocessing as mp

def run(task, args):
    pool = mp.Pool()
    tasks = [pool.apply_async(task, (arg,)) for arg in args]
    pool.close()
    pool.join()
    return [task.get() for task in tasks]
