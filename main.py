import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


class DsaRoller:
    def __init__(self, val1, val2, val3, mod=0):
        self.roll_list = []
        self.val1 = val1 + mod
        self.val2 = val2 + mod
        self.val3 = val3 + mod
        for dice_1 in range(1, 21):
            for dice_2 in range(1, 21):
                for dice_3 in range(1, 21):
                    self.roll_list.append([dice_1 + dice_2 + dice_3,
                                           dice_1,
                                           dice_2,
                                           dice_3])

    def ability_check(self):
        res_list = []
        for dice_1 in range(1, 21):
            for dice_2 in range(1, 21):
                for dice_3 in range(1, 21):
                    test = lambda x, y: x - y if (x - y) > 0 else 0
                    diff_1 = test(dice_1, self.val1)
                    diff_2 = test(dice_2, self.val2)
                    diff_3 = test(dice_3, self.val3)
                    crit_fail = lambda x, y, z: \
                        np.count_nonzero(np.asarray([dice_1, dice_2, dice_3]) == 20) < 2
                    tot_diff = diff_1 + diff_2 + diff_3 if crit_fail(self.val1, self.val2, self.val3) else 60
                    res_list.append([tot_diff,
                                     diff_1,
                                     diff_2,
                                     diff_3])
        return res_list

    def pass_counts(self):
        res_list = self.ability_check()
        res_list = np.asarray([elem [0] for elem in res_list])
        pass_number = []
        ez_pass_list = res_list[res_list == 0]
        pass_number.append([0, len(ez_pass_list), len(ez_pass_list)])
        for i in range(1, 61):
            ez_pass_list = res_list[res_list == i]
            pass_number.append([i, len(ez_pass_list), len(ez_pass_list) + pass_number[i-1][2]])

        return pass_number

    def pass_possibility(self):
        pass_number = self.pass_counts()
        pass_possibility = [[elem[0], elem[2]/8000] for elem in pass_number]
        return pass_possibility


def chances(val1, val2, val3, level=0):
    return [[mod, DsaRoller(val1, val2, val3, mod).pass_possibility()[level][1]] for mod in range(-5, 6)]


def print_chances(val1, val2, val3, level=0, ability=""):
    chance_list = chances(val1, val2, val3, level)
    output = "\n".join([" -> ".join([str(elem) for elem in sublist]) for sublist in chance_list])
    print(ability)
    print("values: {0}, {1}, {2}; ability level: {3}".format(val1, val2, val3, level))
    print(output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = DsaRoller(11, 11, 10, mod=0)
    b = A.ability_check()
    pass_list = A.pass_counts()
    pass_poss = A.pass_possibility()

    print_chances(14, 14, 15, level=12, ability="Taschendiebstahl")
    print_chances(14, 14, 15, level=14, ability="Taschendiebstahl")
    print_chances(10, 11, 11, level=10, ability="Sinnenschärfe")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# TODO DSA Wahrscheinlichkeitsrechner
