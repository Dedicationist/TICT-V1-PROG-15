studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]
def StudentGemiddelde(studentencijfers):
    GemiddeldeLijst = []
    for studenten in studentencijfers:
        for cijfers in studenten:
            gemiddelde = sum(cijfers) / len(cijfers)
            GemiddeldeLijst.append(gemiddelde)
print(StudentGemiddelde(studentencijfers))

