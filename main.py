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
            q = 0
            self.pixels = []
            pixels = []
            for i in rows:
                current_row = i.strip().split(' ')
                if current_row[len(current_row)-1] == '':
                    current_row.pop()
                for j in current_row:
                    pixels.append(int(j))
            for i in range(self.height):
                temp_row = []
                for j in range(self.width):
                    temp_row.append(pixels[q])
                    q += 1
                self.pixels.append(temp_row)

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

    def _conv_pixel(self, m1, m2):
        res = 0
        # print(m1, m2)
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                res += m1[i][j]*m2[i][j]
        return res

    # def _exp(self, coresize):
    #     size = int(coresize/2)
    #     new_img = []
    #     for i in range(0, self.height + 2 * size):
    #         row = []
    #         for j in range(0, self.width + 2 * size):
    #             if ((j < size) or (j >= self.width + size)) or ((i < size) or (i>=self.height+size)):
    #                 row.append(0)
    #             else:
    #                 row.append(self.pixels[i-size][j-size])
    #         new_img.append(row)
    #     return new_img

    def change(self, pixels, core):
        new_pixels = []
        img = pixels #self._exp(core.size)
        for i in range(len(img)-core.size+1):
            new_pixel_row = []
            for j in range(len(img[0])-core.size+1):
                matrix = []
                rows = img[i:i+core.size]
                for row in rows:
                    matrix.append(row[j:j+core.size])
                new_pixel_row.append(self._conv_pixel(matrix, core.matrix))
            new_pixels.append(new_pixel_row)
        return new_pixels

    def make_filter(self, core):
        if self.type == 'P2':
            pixels = self.change(self.pixels, core)
            for pix in pixels:
                print(pix)




class Core:

    def __init__(self, filename):
        self.matrix = []
        self.height, self.width = 0, 0
        self.get_core(filename)

    def get_core(self, filename):
        with open(filename, 'r') as f:
            file = f.read()
            rows = file.split('\n')
            self.size = len(rows)
            for row in rows:
                current_row = row.split(' ')
                self.matrix.append([int(i) for i in current_row])
