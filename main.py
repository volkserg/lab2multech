class Image:

    def __init__(self, filename):
        with open(filename, 'r') as f:
            img = f.read()
            rows = img.split('\n')
            rows.pop()
            self.pixels = []
            self.type = rows.pop(0)
            self.width = int(rows[0].split(' ')[0])
            self.height = int(rows[0].split(' ')[1])
            rows.pop(0)
            self.intens = rows[0]
            rows.pop(0)
            self.get_pixels(rows)

    def get_pixels(self, rows):
        if self.type=='P2':
            self.pixels = []
            for i in rows:
                current_row = i.split(' ')
                if current_row[len(current_row)-1] == '':
                    current_row.pop()
                self.pixels.append([int(j) for j in current_row])

        if self.type == 'P3':
            self.pixels = {}
            r, g, b = [], [], []
            for i in rows:
                r_row, g_row, b_row = [], [], []
                current_row = i.split(' ')
                for j in range(0, len(current_row), 3):
                    r_row.append(int(current_row[j]))
                for j in range(1, len(current_row), 3):
                    g_row.append(int(current_row[j]))
                for j in range(2, len(current_row), 3):
                    b_row.append(int(current_row[j]))
                r.append(r_row)
                g.append(g_row)
                b.append(b_row)
            self.pixels['r'] = r
            self.pixels['g'] = g
            self.pixels['b'] = b

    def save_image(self, filename):
        with open (filename, 'w') as f:
            if self.type == 'P2':
                f.write('P2\n')
                f.write(str(self.width) + ' ' + str(self.height) + "\n")
                f.write(str(self.intens) + "\n")
                for i in range(self.height):
                    for j in range(self.width):
                        f.write(str(self.pixels[i][j]) + " ")
                    f.write("\n")

            if self.type == 'P3':
                f.write('P3\n')
                f.write(str(self.width) + ' ' + str(self.height) + "\n")
                f.write(str(self.intens) + "\n")
                for i in range(self.height):
                    for j in range(self.width):
                        f.write(str(self.pixels['r'][i][j]) + " ")
                        f.write(str(self.pixels['g'][i][j]) + " ")
                        f.write(str(self.pixels['b'][i][j]) + " ")
                    f.write("\n")


class Core:

    def __init__(self, filename):
        self.matrix = []
        self.height, self.width = 0, 0
        self.get_core(filename)

    def get_core(self, filename):
        with open(filename, 'r') as f:
            file = f.read()
            rows = file.split('\n')
            self.width = len(rows[0].split(' '))
            self. height = len(rows)
            for row in rows:
                current_row = row.split(' ')
                self.matrix.append([int(i) for i in current_row])
