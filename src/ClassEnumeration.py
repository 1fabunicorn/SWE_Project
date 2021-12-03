class_chunks = ["money", "title", "grid", "item", "product", "block", "wrap", "wrapper"]
class_seps = ['-', '_', '__', '--']


def generate(chunks, seps):
    r = []
    for i in chunks:
        for j in chunks:
            for k in seps:
                r.append(i + k + j)
    return set(r)

print(generate(class_chunks, class_seps))
