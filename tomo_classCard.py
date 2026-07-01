def print_card():
    width = 54
    dash_line = "-" * width
    
    # Headers
    h1 = "Asian Institute of Compute Studies"
    h2 = "Commonwealth Branch"
    h3 = "CLASS CARD"
    
    header1 = f"|{h1.center(width - 2)}|"
    header2 = f"|{h2.center(width - 2)}|"
    header3 = f"|{h3.center(width - 2)}|"
    
    left_width = 24
    right_width = 23
    
    def make_row(left, right):
        return f"| {left.ljust(left_width)} | {right.ljust(right_width)} |"
        
    print(dash_line)
    print(header1)
    print(header2)
    print(dash_line)
    print(header3)
    print(dash_line)
    print(make_row("Name:  Tomo,Lyshan Dave", "Section: BS5MA"))
    print(make_row("Subject:  CC112", "Desc: FUNDA. PROG."))
    print(make_row("Sem:  1ST SEM", "AY: 2026-2027"))
    print(dash_line)
    print(make_row("Grade:  90.15", "Equiv:  1.50"))
    print(dash_line)
    print(make_row("Status:  PASSED", "Teacher Sig:"))
    print(dash_line)

if __name__ == "__main__":
    print_card()
