
from ways.graph import load_map_from_csv
import pandas as pd
import random

class ProblemCreator:


    def __init__(self):
        self.roads = load_map_from_csv()
        self.problems_list = []

    def print_roads(self):
        print(self.roads)

    def convert_problem_list_to_txt_file(self):
        with open('problems.txt', 'w') as f:
            for p in self.problems_list:
                f.write(f"{p['start']}, {p['goal']}\n")
        # df = pd.DataFrame.from_dict(self.problems_list)
        # df.to_csv('problems.csv', index = False, header=True)


    def create_one_problem(self):
        list = []
        junction_index = random.randint(0, len(self.roads))
        list.append(junction_index)
        path_length = random.randint(10,20)
        for _ in range(0, path_length):
            next_junction = self.roads.go_to_next_junction(junction_index)
            if next_junction != -1:
                list.append(next_junction)
                junction_index = next_junction
            else:
                print("Error was detected, I'm trying again")
                return self.create_one_problem()
        return list[0], list[-1]


    def create_all_problems(self):
        for _ in range(0,100):
            print(_)
            start, goal = self.create_one_problem()
            problem = { "start" : start, "goal" : goal}
            self.problems_list.append(problem)
        self.convert_problem_list_to_txt_file()

        

creator  = ProblemCreator()
creator.create_all_problems()