import pandas as pd
import numpy as np
import re
import json


class QuestDriver:
    def __init__(self, file: str, player: dict = None):
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
                    self.player[key] += log_rep[way][key]
        id = str(id).split()
        if len(id) == 1:
            self.id = int(float(id[0]))
        else:
            num = str(self.player[id[0]])
            goal = str(id[2])
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


que = QuestDriver(file='Template.xlsx', player={'Name': 'Peter', 'Age': 45, 'id': 1, 'rep_pol': 4})
a = que.update(3.0)
print(a)
print(que.update('rep_pol > 5 5 7'))
print(que.end_of_session())