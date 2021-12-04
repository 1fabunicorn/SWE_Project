class_chunks = ["money", "title", "grid", "item", "product", "card", "block", "wrap", "wrapper", "reg", "price", "name",
                "pricing", "pricing", "details" "collection__title", "product__price"]
class_seps = ['-', '_', '__', '--']

class ClassEnumeration():
    def __init__(self):
        self.classes = self.generate(class_chunks, class_seps)

    def generate(self, chunks, seps):
        r = []
        for i in chunks: # generate combos
            for j in chunks:
                for k in seps:
                    r.append(i + k + j)
        r = set(r)
        r.update(class_chunks)
        return r

    def get(self, response):
        t = []
        f = []
        for class_combo in self.classes:
            r = response.css("." + class_combo + " ::text").getall()
            if r:
                for selection in r:
                    s = selection.strip()
                    if s:
                        t.append(s)
                # t.append({class_combo:r})
        return t


