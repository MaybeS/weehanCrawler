import pickle

def save(n):
    with open('page.p', 'wb') as file:
        pickle.dump(n, file)

def load():
    try :
        with open('page.p', 'rb') as file:
            return pickle.load(file)
    except:
        return 1