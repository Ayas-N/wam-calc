def check(num):
    '''Checks if the number can be converted to a float, also makes sure number is more than 0'''
    try:
        num = float(num)
        if num < 0: 
            raise ValueError

    except ValueError:
        print("Please enter a valid input (Non-string >= 0)")
        return None

    return num   

def calc(marks_ls):
    '''Takes in a list of tuples (weighting, marks) and reutrns a float subject_mark'''
    subject_mark = 0
    for i in range(len(marks_ls)):
        subject_mark += (marks_ls[i][0] * marks_ls[i][1])/100
    
    return subject_mark

def final_calc(subj_ls):
    '''Takes in the list of tuples (cp, marks, number), gets sum of (cp * marks) / sum of cp)'''
    cp_marks = 0
    cp_sum = 0
    for i in range(len(subj_ls)):
        cp_marks += (subj_ls[i][0] * subj_ls[i][1])
        cp_sum += subj_ls[i][0]

    return (cp_marks/cp_sum)

def wam_summary(subj_ls):
    '''Returns a formatted string containing Subject number, credit point, and marks scored for that subject'''
    breakpoint()
    str_out = ""
    for i in range(len(subj_ls)):
        str_out += f"Subject {subj_ls[i][2]}, {int(subj_ls[i][0])} cp- {subj_ls[i][1]} marks\n"
    
    return str_out

def main():
    # Outer loop used for writing the credit point of a subject
    print("Welcome to the WAM calculator!")
    subject_no = 1
    subj_ls = []
    while True:
        cp = input("Enter cp for the unit here: (Type 'done' when you finish) ")
        # Invalid outputs will not count and restart the program.
        if cp.lower().strip() == "done":
            if len(subj_ls) < 1:
                print("No input was received. Have a good day :)")
                break

            print(f"Your final WAM is {final_calc(subj_ls)}")
            print(wam_summary(subj_ls))
            break

        try:
            cp = int(cp)
            if cp <= 0: 
                raise ValueError

        except ValueError:
            print("Please enter a valid input (Non-string >= 0)")
            continue

        # Inner loop, keeps track of weighting and marks for the subject.
        weight = 100
        usr_weight = 0
        print(f"Subject {subject_no}: ")
        unit_ls = []
        while usr_weight < 100:
            print(f"Current weighting on all tasks: {usr_weight}")
            # Get weighting
            usr_input = check(input("Enter the weighting for an assessment here: "))

            if usr_input == None:
                continue

            usr_weight += usr_input
            usr_mark = 0

            if usr_weight > 100:
                print("The total weighting of your marks was more than 100. Please try again.")
                usr_weight = 0
                continue

            # Get percentage
            usr_mark = check(input("Enter the percentage you've scored for the assessment here: "))

            if usr_mark == None:
                usr_weight -= usr_input
                continue
 
            # Create a tuple of (weighting, user mark) add this to a list to be used in calc()
            unit_mark = (usr_input, usr_mark)
            unit_ls.append(unit_mark)

        # Create a tuple, add it to subject list so it can be displayed later.
        subj_mark = calc(unit_ls)
        unit_tup = (cp, subj_mark, subject_no)
        subj_ls.append(unit_tup)
        subject_no += 1

if __name__ == "__main__":
    main() 