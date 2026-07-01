# NLP Chatbot - Shellhelp College Advisor

print("Shellhelp: Kamusta! Ako si Shellhelp")
print("Tanong mo lang ako tungkol sa courses, enrollment, o schedules.")
print("Type 'exit' para umalis.\n")

while True:
    msg = input("You: ").lower()

    if msg == "exit":
        print("Shellhelp: Bye! Good luck sa college mo!")
        break
    elif "enroll" in msg or "requirement" in msg or "pasukan" in msg:
        print("Shellhelp: Para mag-enroll, kailangan mo ng:")
        print("  - Form 137 / Report Card")
        print("  - PSA Birth Certificate")
        print("  - Good Moral Certificate")
        print("  - 2x2 ID Picture (4 pcs)")
        print("  - Barangay Clearance")
        print("  Tip: Pumunta ka ng maaga kasi mahaba pila kapag enrollment!")
    elif "course" in msg or "program" in msg or "kunin" in msg or "maganda" in msg:
        print("Shellhelp: Eto mga magandang courses na pwede mong kunin:")
        print("  - BSIT (Information Technology) - in-demand, maraming IT jobs!")
        print("  - BSCS (Computer Science) - high salary, coding-heavy!")
        print("  - BSBA (Business Administration) - maganda kung gusto mo mag-business")
        print("  - BSHM (Hospitality Management) - para sa hotel at tourism industry")
        print("  - BSEd (Education) - kung gusto mo magturo, noble profession!")
        print("  Tip: Piliin mo yung course na passion mo, hindi lang uso!")
    elif "schedule" in msg or "sched" in msg or "oras" in msg or "kailan" in msg:
        print("Shellhelp: Eto ang schedule ng klase:")
        print("  - Monday to Friday: 7:00 AM - 5:00 PM")
        print("  - Saturday: 8:00 AM - 12:00 PM")
        print("  - Sunday: Walang klase")
        print("  Note: Depende pa rin sa course mo ang exact schedule.")
    elif "hello" in msg or "hi" in msg or "kamusta" in msg:
        print("Shellhelp: Hello! Ano maitutulong ko? Ask mo lang!")
    elif "salamat" in msg or "thanks" in msg:
        print("Shellhelp: Walang anuman! Balik ka lang kung may tanong ka pa!")
    else:
        print("Shellhelp: Hindi ko nagets yun. Try mo itanong about courses, enrollment, o schedule.")
