def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """
    houses_set = set()
    my_file = open(filename, 'r')
    for line in my_file:
        line = line.rstrip()
        line_as_list = line.split('|')

        first_name, last_name, house, advisor, cohort = line_as_list
        if house == '':
            house = 'N/A'
        else:
           houses_set.add(house)

    my_file.close()

    return houses_set
 

def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """

    cohort_set = set()
    my_file = open(filename, 'r')

    all_students = set()
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []
    
    for line in my_file:
        line = line.rstrip()
        line_as_list = line.split('|')

        first_name, last_name, house, advisor, cohort = line_as_list

        if cohort == 'I':
            continue
        else:
            cohort_set.add(cohort)

        full_name = first_name + ' ' + last_name

        if cohort == 'Winter 2015':
            winter_15.append(full_name)
        elif cohort == "Spring 2015":
            spring_15.append(full_name)
        elif cohort == "Summer 2015":
            summer_15.append(full_name)
        elif cohort == "TA":
            tas.append(full_name)


    all_students = [sorted(winter_15), sorted(spring_15), sorted(summer_15), sorted(tas)]

    my_file.close()

    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    # Code goes here
    houses_set = set()
    my_file = open(filename, 'r')

    for line in my_file:
        line = line.rstrip()
        line_as_list = line.split('|')

        first_name, last_name, house, advisor, cohort = line_as_list
        
        houses_set.add(house)

        # full_name = first_name + ' ' + last_name

        # if house == ''
        # check if cohort is 'I'
        # add to Instructor list

        if house == '':
            if cohort == "TA":
                tas.append(last_name)
            else:
                instructors.append(last_name)
        else:
            if house == 'Gryffindor':
                gryffindor.append(last_name)
            elif house == "Hufflepuff":
                hufflepuff.append(last_name)
            elif house == "Slytherin":
                slytherin.append(last_name)
            elif house == "Dumbledore's Army":
                dumbledores_army.append(last_name)
            elif house == "Order of the Phoenix":
                order_of_the_phoenix.append(last_name)
            elif house == "Ravenclaw":
                ravenclaw.append(last_name)


        # if house == 'Gryffindor':
        #     gryffindor.append(last_name)
        # elif house == "Hufflepuff":
        #     hufflepuff.append(last_name)
        # elif house == "Slytherin":
        #     slytherin.append(last_name)
        # elif house == "Dumbledore's Army":
        #     dumbledores_army.append(last_name)
        # elif house == "Order of the Phoenix":
        #     order_of_the_phoenix.append(last_name)
        # elif house == "Ravenclaw":
        #     ravenclaw.append(last_name)
        # elif cohort == "TA":
        #     tas.append(last_name)
        # elif cohort == "I":
        #     instructors.append(last_name)
            
        
    all_students = [sorted(hufflepuff), sorted(gryffindor), sorted(ravenclaw), sorted(slytherin), sorted(dumbledores_army), sorted(order_of_the_phoenix), sorted(tas), sorted(instructors)]

    my_file.close()

    return all_students



def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    # Code goes here
    with open(filename) as my_file:
        for line in my_file:
            line = line.rstrip()
            line_as_list = line.split('|')

            first_name, last_name, house, advisor, cohort = line_as_list

            full_name = first_name + ' ' + last_name

            line_as_tuple = (full_name, house, advisor, cohort)

            student_list.append(line_as_tuple)

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here

    print "Search our directory to find a Hackbright student's cohort."    
    

    inputted_name_to_search = raw_input("Enter full name (ex: Jane Doe) to search our directory.\n>> ")

    name_to_search = inputted_name_to_search.rstrip()

    for student_info in student_list:
        student_full_name = student_info[0]

        if name_to_search == student_full_name:
            cohort = student_info[3]
            print "{}'s Cohort: {}".format(student_full_name, cohort)
            return cohort
        else:
            continue

    print "Student not found."
    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()
    staff_first_names = []
    student_first_names = []

    # Code goes here
    with open(filename) as my_file:
        for line in my_file:
            line = line.rstrip()
            line_as_list = line.split('|')

            first_name, last_name, house, advisor, cohort = line_as_list

            if cohort == 'TA' or cohort == 'I':
                staff_first_names.append(first_name)
            else:
                student_first_names.append(first_name)

    print staff_first_names
    print student_first_names   



    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and returns everyone in their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
# print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
