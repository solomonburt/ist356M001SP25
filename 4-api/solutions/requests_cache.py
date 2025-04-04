import pickle

def load_cache(pickle_file):
    '''Load the cache from a pickle file. If the file does not exist, return an empty dictionary.'''
    # Check if the file exists and load it, otherwise return an empty dictionary
    # Use a try-except block to handle the FileNotFoundError
    try:
        with open(pickle_file, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
    
def clear_cache(pickle_file):
    '''This function clears the cache by overwriting the cache file with an empty dictionary.'''
    # open pickle file in write-binary mode ('wb'). With statement closes file after writing.
    with open(pickle_file, 'wb') as f:
        pickle.dump({}, f) # serializes the empty dictionary {} and writes it to the file, effectively clearing the cache.
        return {} #after clearing the cache, this function returns an empty dictionary indicating cleared cache

def save_cache(cache, pickle_file):
    '''This function saves the cache (a Python object like a dictionary) to a pickle file.'''
    with open(pickle_file, 'wb') as f: # open file in write-binary mode ('wb')
        pickle.dump(cache, f) # serializes the cache object and writes it to the file.

if __name__ == '__main__':
    cache = clear_cache('test.pkl')
    assert cache == {}
    cache['test'] = 'test'
    save_cache(cache, 'test.pkl')
    cache = load_cache('test.pkl')
    assert cache == {'test': 'test'}
    assert cache['test'] == 'test'

