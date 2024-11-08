class Libro:
    conteggio_libri = 0

    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        Libro.conteggio_libri += 1

    def mostra_info(self):
        return "Titolo: " + self.titolo + ", Autore: " + self.autore + ", Pagine: " + str(self.pagine)

    def lungo(self):
        return self.pagine > 300

    @classmethod
    def mostra_conteggio_libri(cls):
        print(f"Libri Totale: {cls.conteggio_libri}")

class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    def mostra_libri(self):
        if not self.libri:
            print("La biblioteca è vuota.")
        else:
            for libro in self.libri:
                print(libro.mostra_info())
                if libro.lungo():
                    print("        Il libro ha piu di 300 pagine.")
                else:
                    print("        Il libro ha menu di 300 pagine.")

    def mostra_totale_libri(self):
        print(f"Libri Totale nella Biblioteca: {len(self.libri)}")

    def salva_su_file(self, nome_file="biblioteca.txt"):
        with open(nome_file, "w") as file:
            for libro in self.libri:
                file.write(f"{libro.titolo}, {libro.autore}, {libro.pagine}\n")
        print(f"Informazioni sui libri salvate in '{nome_file}'.")

# Sample usage
libri = [Libro("Red see", "Alex", 210),
         Libro("Blue ice", "Lana", 390),
         Libro("Love Story", "Jack", 450)]

biblioteca = Biblioteca()
for libro in libri:
    biblioteca.aggiungi_libro(libro)
biblioteca.mostra_libri()
biblioteca.mostra_totale_libri()
Libro.mostra_conteggio_libri()
biblioteca.salva_su_file()
