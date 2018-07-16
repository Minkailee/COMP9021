
from __future__ import print_function
import sys, os

# function for converting raw knights and knaves puzzles into a standard format.
def to_cnf(claim, template, speaker, name_map):

    negate_knaves = lambda x, k: -x if k == "knave" or k == "Knave" or k == "knaves" or k == "Knaves" else x
    id_0_val = name_map[speaker]

    # print("id_0_val=",id_0_val)
    # print("claim=",claim)
    # print("template=",template)

    #  Handle nothing
    if len(template) == 0:
        cnf = [[-id_0_val, id_0_val], [id_0_val, -id_0_val]]
        # print("cnf=",cnf)
        return cnf

    #  Handle P
    if template == "name is a k_id":
        id_1, kid_1 = claim.split()[0], claim.split()[-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)

        cnf = [[-id_0_val, id_1_val], [id_0_val, -id_1_val]]
        # print("cnf=",cnf)
        return cnf

    if template == "at least one of name and name is a k_id":
        id_1, kid_1 = claim.split()[4], claim.split()[-1]
        id_2, kid_2 = claim.split()[6], claim.split()[-1]

        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)


        cnf = [[-id_0_val, id_1_val, id_2_val], [id_0_val, -id_1_val], [id_0_val, -id_2_val]]
        # print("cnf=",cnf)
        return cnf


    #  Handle NOT P
    if template == "it's false that name is a k_id":
        id_1, kid_1 = claim.split()[3], claim.split()[-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)

        cnf = [[-id_0_val, -id_1_val], [id_0_val, id_1_val]]
        return cnf
    elif template == "it's not the case that name is a k_id":
        id_1, kid_1 = claim.split()[5], claim.split()[-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)

        cnf = [[-id_0_val, -id_1_val], [id_0_val, id_1_val]]
        return cnf

    #  Handle P OR Q
    if template == "at least one of the following is true: that name is a k_id or that name is a k_id":
        id_1, kid_1 = claim.split()[9], claim.split()[12]
        id_2, kid_2 = claim.split()[15], claim.split()[18]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, id_1_val, id_2_val], [id_0_val, -id_1_val], [id_0_val, -id_2_val]]
        return cnf
    elif template == "name is a k_id or name is a k_id":
        id_1, kid_1 = claim.split()[0], claim.split()[3]
        id_2, kid_2 = claim.split()[5], claim.split()[8]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, id_1_val, id_2_val], [id_0_val, -id_1_val], [id_0_val, -id_2_val]]
        return cnf

    #  Handle P AND Q
    if template == "name and name are k_ids":
        id_1, kid_1 = claim.split()[0], claim.split()[-1][:-1]
        id_2, kid_2 = claim.split()[2], claim.split()[-1][:-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, id_1_val], [-id_0_val, id_2_val], [id_0_val, -id_1_val, -id_2_val]]
        return cnf
    elif template == "name and name are both k_ids":
        id_1, kid_1 = claim.split()[0], claim.split()[-1][:-1]
        id_2, kid_2 = claim.split()[2], claim.split()[-1][:-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, id_1_val], [-id_0_val, id_2_val], [id_0_val, -id_1_val, -id_2_val]]
        return cnf
    elif template == "name is a k_id and name is a k_id":
        id_1, kid_1 = claim.split()[0], claim.split()[3]
        id_2, kid_2 = claim.split()[5], claim.split()[8]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, id_1_val], [-id_0_val, id_2_val], [id_0_val, -id_1_val, -id_2_val]]
        return cnf
    elif template == "both name is a k_id and name is a k_id":
        id_1, kid_1 = claim.split()[1], claim.split()[4]
        id_2, kid_2 = claim.split()[6], claim.split()[9]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, id_1_val], [-id_0_val, id_2_val], [id_0_val, -id_1_val, -id_2_val]]
        return cnf
    elif template == "name know that name is a k_id and that name is a k_id":
        id_1, kid_1 = claim.split()[3], claim.split()[6]
        id_2, kid_2 = claim.split()[9], claim.split()[12]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, id_1_val], [-id_0_val, id_2_val], [id_0_val, -id_1_val, -id_2_val]]
        return cnf
    elif template == "both name and name are k_ids":
        id_1, kid_1 = claim.split()[1], claim.split()[-1][:-1]
        id_2, kid_2 = claim.split()[3], claim.split()[-1][:-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, id_1_val], [-id_0_val, id_2_val], [id_0_val, -id_1_val, -id_2_val]]
        return cnf

    #  Handle P XOR Q
    if template == "either name is a k_id or name is a k_id":
        id_1, kid_1 = claim.split()[1], claim.split()[4]
        id_2, kid_2 = claim.split()[6], claim.split()[9]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, -id_1_val, -id_2_val], [-id_0_val, id_1_val, id_2_val],
               [id_0_val, -id_1_val, id_2_val], [id_0_val, id_1_val, -id_2_val]]
        return cnf

    #  Handle (P & ~Q) XOR (~P & Q)
    if template == "name and name are not the same":
        id_1, id_2 = claim.split()[0], claim.split()[2]
        id_1_val, id_2_val = name_map[id_1], name_map[id_2]

        cnf = [[-id_0_val, -id_1_val, -id_2_val], [-id_0_val, id_1_val, id_2_val],
               [id_0_val, -id_1_val, id_2_val], [id_0_val, id_1_val, -id_2_val]]
        return cnf
    elif template == "name and name are different":
        id_1, id_2 = claim.split()[0], claim.split()[2]
        id_1_val, id_2_val = name_map[id_1], name_map[id_2]

        cnf = [[-id_0_val, -id_1_val, -id_2_val], [-id_0_val, id_1_val, id_2_val],
               [id_0_val, -id_1_val, id_2_val], [id_0_val, id_1_val, -id_2_val]]
        return cnf
    elif template == "of name and name, exactly one is a k_id":
        id_1, id_2 = claim.split()[1], claim.split()[3][:-1]
        id_1_val, id_2_val = name_map[id_1], name_map[id_2]

        cnf = [[-id_0_val, -id_1_val, -id_2_val], [-id_0_val, id_1_val, id_2_val],
               [id_0_val, -id_1_val, id_2_val], [id_0_val, id_1_val, -id_2_val]]
        return cnf

    #  Handle P IMPLIES Q
    if template == "name could claim that name is a k_id":
        id_1, kid_1 = claim.split()[0], "knight"
        id_2, kid_2 = claim.split()[4], claim.split()[-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, -id_1_val, id_2_val], [id_0_val, id_1_val],
               [id_0_val, -id_2_val]]
        return cnf
    elif template == "name could say that name is a k_id":
        id_1, kid_1 = claim.split()[0], "knight"
        id_2, kid_2 = claim.split()[4], claim.split()[-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, -id_1_val, id_2_val], [id_0_val, id_1_val],
               [id_0_val, -id_2_val]]
        return cnf
    elif template == "name would tell you that name is a k_id":
        id_1, kid_1 = claim.split()[0], "knight"
        id_2, kid_2 = claim.split()[5], claim.split()[-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, -id_1_val, id_2_val], [id_0_val, id_1_val],
               [id_0_val, -id_2_val]]
        return cnf
    elif template == "only a k_id would say that name is a k_id":
        id_1, kid_1 = speaker, "knave"
        id_2, kid_2 = claim.split()[6], claim.split()[-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, -id_1_val, id_2_val], [id_0_val, id_1_val],
               [id_0_val, -id_2_val]]
        return cnf

    #  Handle P <-> Q
    if template == "name and name are both k_ids or both k_ids":
        id_1, kid_1 = claim.split()[0], "knight"
        id_2, kid_2 = claim.split()[2], "knight"
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, -id_1_val, id_2_val], [-id_0_val, id_1_val, -id_2_val],
               [id_0_val, -id_1_val, -id_2_val], [id_0_val, id_1_val, id_2_val]]
        return cnf
    elif template == "name and name are the same":
        id_1, kid_1 = claim.split()[0], "knight"
        id_2, kid_2 = claim.split()[2], "knight"
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, -id_1_val, id_2_val], [-id_0_val, id_1_val, -id_2_val],
               [id_0_val, -id_1_val, -id_2_val], [id_0_val, id_1_val, id_2_val]]
        return cnf

    #  Handle ~(P OR Q)
    if template == "neither name nor name are k_ids":
        id_1, kid_1 = claim.split()[1], claim.split()[-1][:-1]
        id_2, kid_2 = claim.split()[3], claim.split()[-1][:-1]
        id_1_val = negate_knaves(name_map[id_1], kid_1)
        id_2_val = negate_knaves(name_map[id_2], kid_2)

        cnf = [[-id_0_val, -id_1_val], [-id_0_val, -id_2_val], [id_0_val, id_1_val, id_2_val]]
        return cnf

    raise ValueError("Unsupported template provided.")


templates = set([])

def templatize(names, claim):
    """Transform a claim into a regex-capable template."""
    for name in names:
        while name in claim:
            claim = claim.replace(name, "name")

    while "knave" in claim:
        claim = claim.replace("knave", "k_id")

    while "knight" in claim:
        claim = claim.replace("knight", "k_id")


    while "Knave" in claim:
        claim = claim.replace("Knave", "k_id")

    while "Knight" in claim:
        claim = claim.replace("Knight", "k_id")

    while " am " in claim:
        claim = claim.replace(" am ", " is ")

    while "Sir " in claim:
        claim = claim.replace("Sir ", "")

    while " Sir " in claim:
        claim = claim.replace(" Sir ", "")  

    while "Sir " in claim:
        claim = claim.replace("Sir ", "")  

    return claim.lower()


name_map_global = []

def parse(puzzle):
    """Parse puzzles of form {name: claim} into symbolized form."""
    # Replace instances of "I" with name of speaker
    puzzle = {name: claim.replace(" I ", " " + name + " ").replace("I ", name + " ").replace(" I", " " + name).replace(",", "").replace("!", "").replace(".", "").replace("Sir ", "").replace(" Sir ", "").replace(" Sir", "")
              for name, claim in puzzle.items()}

    global name_map_global
    names = puzzle.keys()
    name_map = {list(names)[i]: i + 1 for i in range(len(names))}
    inverse_name_map = {int_id: name for name, int_id in name_map.items()}

    name_map_global = list(name_map)
    # print("name_map=", list(name_map))
    # print("name_map_global=", name_map_global)

    # print("inverse_name_map=",list(inverse_name_map))

    puzzle_cnf = []
    for speaker, claim in puzzle.items():

        # transform given claim into a template
        template = templatize(names, claim)

        # print("template=",template)

        cnf_claim = to_cnf(claim, template, speaker, name_map)
        puzzle_cnf.extend(cnf_claim)

        global templates
        templates.add(template)

    return puzzle_cnf, inverse_name_map


def clean(puzzle):


    rm_lead_apo = lambda x: x[1:] if x[0] == '\'' else x
    rm_ws = lambda x: x.strip()

    # if "!" in puzzle:
    #     lines = puzzle.split("!")
    # else:
    #     lines = puzzle.split(".")


    # lines = str(puzzle.split(".")).split("!")
    # lines, name_line = lines[1:], lines[0]

    str_index = 0
    while puzzle[str_index] != "." and puzzle[str_index] != "!":
        str_index += 1
    name_line = puzzle[:str_index]
    #print("name_line=", name_line)

    lines = puzzle[str_index+1:]
    #print("lines = ", lines)

    sub_comma_for_and = lambda x: x.replace("and", ",")
    make_names = lambda x: list(map(rm_ws, x.split("Sirs")[1].split(",")))

    names = make_names(sub_comma_for_and(name_line))

    # print(type(names))
    #print("names=", names)

    lines_list = []
    lines_index_pre = 0
    lines_index_last = 0

    # words devide
    if '!"' not in lines and '."' not in lines:
        while lines_index_pre < len(lines):
            if lines[lines_index_pre] == ".":
                lines_list.append(lines[lines_index_last:lines_index_pre])
                lines_index_last = lines_index_pre + 1
            lines_index_pre += 1
        lines_list.append(lines[lines_index_last:lines_index_pre])
        print("lines_list = ", lines_list)

    # words devide
    else:
        while lines_index_pre < len(lines)-1:
            if (lines[lines_index_pre] == '.' or lines[lines_index_pre] == '!') and lines[lines_index_pre+1] == '"':
                lines_list.append(lines[lines_index_last:lines_index_pre+2])
                lines_index_last = lines_index_pre + 2
            lines_index_pre += 1
        lines_list.append(lines[lines_index_last:lines_index_pre])
        print("lines_list = ", lines_list)  


    claims = {}

    # count = 0
    for every_line in lines_list:
        # count += 1
        # print("count = ", count)
        # print(line)

        # if len(line) > 1:
        #     formatted_line = rm_ws(rm_lead_apo(line))
        #     name = formatted_line[:formatted_line.find(" ")]
        #     claim = formatted_line[formatted_line.find(" ") + 1:]

        #     if name not in names:
        #         raise ValueError("Badly formatted puzzle")
        #     else:
        #         claims[name] = clean_claim(claim)
        every_line = every_line + ' '
        list1 = every_line.split("Sir ")
        list2 = list1[1:]
        for every in list2:
            if every[0:every.find(" ")] not in names:
                names.append(every[0:every.find(" ")])

        index1 = every_line.find('"')
        if index1:
            remain_str = every_line[index1+1:]
            # print("remain_str = ", remain_str)
            index2 = remain_str.find('"')
            claim_str = every_line[index1+1:index1+index2+1]
            # print(claim_str)

            for every_name in names:
                if every_name in every_line[:index1] or every_name in every_line[index1+index2+1:]:
                    claims[every_name] = claim_str

    # print("names=", names)

    for every_name2 in names:
        if every_name2 not in claims:
            claims[every_name2] = ""
    # print("claims=",claims)
    return claims

def has_common(list1, list2):
    for item1 in list1:
        if item1 in list2:
            return True
    return False

def process(puzzle, do_clean=True):
    """Process an individual knights and knaves problem."""
    global name_map_global
    if do_clean:
        puzzle = clean(puzzle)

    cnf, inverse_name_map = parse(puzzle)
    # print (cnf)
    add_kid = lambda x, i: "Knight(" + x + ")" if i > 0 else "Knave(" + x + ")"

    parsed_results = []

    names_length = len(name_map_global)
    solutions_all = []
    temp = []
    # print('names_length = ', names_length)

    for i in range(2**names_length):
        for j in range(names_length):
            if (i & 2**j):
                temp.append(j + 1)
            else:
                temp.append(-1 * (j + 1))
        solutions_all.append(temp)
        temp = []
        # print('solutions_all = ', solutions_all)

    # print('len(solutions_all) = ', len(solutions_all))

    # print('cnf = ', cnf)

    solutions_final = []
    add_flag = True

    for every_solution in solutions_all:
        for every_cnf in cnf:

            if not has_common(set(every_cnf), every_solution):
                add_flag = False
                break
        if add_flag:
            solutions_final.append(every_solution)

        add_flag = True

    # print('solutions_final = ', solutions_final)
        
    # if pycosat.solve(cnf) == "UNSAT":
    #     pass
    # else:
    #     results = pycosat.itersolve(cnf)
    #     # print(type(results))
    #     # print(list(results))

    #     for result in results:
    #         result = [add_kid(inverse_name_map[abs(i)], i) for i in result]
    #         parsed_results.append(result)

    #     # for every_result in results:
    #     #     print(every_result)

    for result in solutions_final:
        result = [add_kid(inverse_name_map[abs(i)], i) for i in result]
        parsed_results.append(result)

    return parsed_results


def main_function():
    global name_map_global
    puzzle = ""
    puzzle_list = []
    text = input("Which text file do you want to use for the puzzle? ")
    with open(text, "r") as f:
        for line in f:
            # print(line)
            puzzle = puzzle.strip("\n") + str(line).strip("\n") + " "
    f.close()

    puzzle_list.append(puzzle)
    # print(puzzle_list)

    # Index all solutions from website

    for every_puzzle in puzzle_list:
        solutions = process(every_puzzle)

    # print("len(solutions)=",len(solutions))
    # print("solutions=",solutions)

    name_map_global = sorted(name_map_global)
    # print(name_map_global)


    print("The Sirs are: ", end="")
    for everyname in name_map_global:
        print(everyname + " ",end="")
    print()

    length = len(solutions)
    if length == 0:
        print("There is no solution.")

    elif length > 1:
        print("There are " + str(length) + " solutions.")

    else:
        print("There is a unique solution:")
        for everyname in name_map_global:
            for every_s in solutions[0]:
                if everyname in every_s:
                    print("Sir " + everyname + " is a " + every_s[:every_s.find("(")] + ".")



if __name__ == "__main__":
    main_function()
