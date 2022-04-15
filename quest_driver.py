import pandas as pd
import numpy as np
import re


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
            print(1)
            val = re.findall('{.*?}', b)
            for k in val:
                j = eval(k[1:-1])  # супер большая уязвимость, но я хз как иначе форматировать
                b = b.replace(k, j, 1)
                print(b)
            return b
        else:
            return self.quest_file.loc[[id]].dropna(axis=1)['Text'].values.tolist()[0]

    def return_image(self, id):
        return self.quest_file.loc[[id]]['Image'].values.tolist()[0]

    def update(self, id):
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
        return self.show()

    def show(self):
        return self.return_text(self.id), self.return_image(self.id), self.return_buttons(self.id)


que = QuestDriver(file='Template.xlsx', player={'Name': 'Peter', 'Age': 45, 'id': 1, 'rep_pol': 4})
print(que.show())
print(que.update(2.0))