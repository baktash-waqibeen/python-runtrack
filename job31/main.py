def calcul_notes(student_notes):
    print(student_notes)
    note_list = []
    new_notes = []
    i = 0

    while i < 100:
        note_list.append(i)
        i += 1

    for student_note in student_notes:
        student_note = int(student_note)
        j = 0
        for j in note_list:
            if student_note == note_list[j]:
                if (note_list[j] + 1) % 5 == 0:
                    new_notes.append(student_note + 1)
                    break
                elif (note_list[j] + 2) % 5 == 0:
                    new_notes.append(student_note + 2)
                    student_note = student_note + 2
                    break
                elif(note_list[j] + 3) % 5 == 0:
                    new_notes.append(student_note + 3)
                    student_note = student_note + 3
                    break
                else:
                    new_notes.append(student_note)
                    break
            j += 1

    return(new_notes)


nb_students = input("How many notes do you want to enter? \n")

i = 0
notes = []
while i < int(nb_students):
    note = input("Enter the student's note number " + str(i + 1) + "\n")
    notes.append(note)
    i += 1

calcul_notes(notes)
