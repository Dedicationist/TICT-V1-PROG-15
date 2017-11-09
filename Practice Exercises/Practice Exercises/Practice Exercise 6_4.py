studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def StudentGemiddelde(studentencijfers):
    global GemiddeldeLijst
    GemiddeldeLijst = []
    for studenten in studentencijfers:
        gemiddelde = sum(studenten) / len(studenten)
        GemiddeldeLijst.append(gemiddelde)
    return GemiddeldeLijst

def AlgemeenGemiddelde(GemiddeldeLijst):
    gemiddelde = sum(GemiddeldeLijst) / len(GemiddeldeLijst)
    return gemiddelde




print(StudentGemiddelde(studentencijfers))
print(AlgemeenGemiddelde(GemiddeldeLijst))

