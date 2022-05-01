import pandas as pd
import numpy as np
import re
import json
import ast


class QuestDriver:
    def __init__(self, file: str, player: dict = {'Name': 'Peter', 'Age': 45, 'id': 1, 'rep_pol': 7}):
        self.quest_file = pd.read_excel(file).set_index(['id'])
        self.buttons = self.quest_file[self.quest_file.columns[
            (np.array(self.quest_file.columns.str.find('Button')) != -1) | (
                    np.array(self.quest_file.columns.str.find('res')) != -1)]]
        self.player = player
        self.id = self.player['id']

    def return_buttons(self, id):
        n = self.buttons.loc[[id]].dropna(axis=1)
        num_but = n.shape[1] // 2
        but_text = n.values.tolist()[0][::2]
        ways = n.values.tolist()[0][1::2]
        return num_but, but_text, ways

    def return_text(self, id):
        b = self.quest_file.loc[[id]].dropna(axis=1)['Text'].values.tolist()[0]
        if '{self.player[' in b:
            val = re.findall('{.*?}', b)
            for k in val:
                j = eval(k[1:-1])  # супер большая уязвимость, но я хз как иначе форматировать
                b = b.replace(k, j, 1)
            return b
        else:
            return self.quest_file.loc[[id]].dropna(axis=1)['Text'].values.tolist()[0]

    def return_image(self, id):
        return self.quest_file.loc[[id]]['Image'].values.tolist()[0]

    def update(self, id):
        log_rep = self.quest_file.loc[[self.id]]['Rep_change'].values.tolist()[0]
        if log_rep == log_rep:
            log_rep = json.loads(log_rep.strip())
            way = str(self.return_buttons(self.id)[2].index(id))
            if way in log_rep.keys():
                for key in log_rep[way].keys():
                    if key in self.player:
                        self.player[key] += log_rep[way][key]
                    else:
                        self.player[key] = log_rep[way][key]

        id = str(id).split()
        if len(id) == 1:
            self.id = int(float(id[0]))
        else:
            try:
                num = str(self.player[id[0]])
            except KeyError:
                self.player[id[0]] = 0
                num = str(self.player[id[0]])
            goal = str(id[2])
            print(num + id[1] + goal)
            if eval(num + id[1] + goal):
                self.id = int(id[3])
            else:
                self.id = int(id[4])
        self.player['id'] = self.id
        return self.show()

    def show(self):
        return self.return_text(self.id), self.return_image(self.id), self.return_buttons(self.id)

    def end_of_session(self):
        return self.player


if __name__ == "__main__":
    que = QuestDriver(file='Template.xlsx', player={'Name': 'Kirill', 'Age': 45, 'id': 106, 'rep_pol': 4, "night_flag":1})
    a = que.update(107)
    print(a[0])
    print(a[2][1])
    while True:
        c = int(input()) - 1
        a = que.update(a[2][2][c])
        print(a[0])
        print(a[2][1])
