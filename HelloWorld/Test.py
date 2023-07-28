def flatten(lst):
    flat_list = []
    for sublist in lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def chunk(lst, size):
    chunks = []
    for i in range(0, len(lst), size):
        chunks.append(lst[i:i+size])
    return chunks

def normalize_chunks(l, n):
    return chunk(flatten(l), n)

my_list = [[4,5,6,7],[3,4],[1],[1,7,86]]

print(normalize_chunks(my_list, 3))
print(normalize_chunks(my_list, 2))