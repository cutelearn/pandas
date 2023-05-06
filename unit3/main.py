import pandas as pd

class Score:
    def __init__(self, course, data):
        self.course = course
        self.data = data
        self.df = pd.DataFrame(data, columns=course, index=range(1, len(data)+1))

    def add_total(self):
        total = [self.df.loc[i].sum() for i in range(1, len(self.df)+1)]
        self.df["Total"] = total

    def add_average(self):
        average = self.df.mean()
        self.df.loc["Average"] = average

    def remove_average(self):
        self.df = self.df.drop(index=["Average"])

    def sort_by_total(self):
        self.df = self.df.sort_values(by="Total", ascending=False)

    def add_rank(self):
        rank = [i for i in range(1, len(self.df)+1)]
        self.df["Rank"] = rank

def main():
    course = ["Chinese", "English", "Math", "Natural", "Society"]
    chinese = [14, 12, 13, 10, 13]
    english = [13, 14, 11, 13, 12]
    math = [15, 9, 12, 12, 10]
    natural = [15, 12, 13, 14, 9]
    society = [12, 13, 14, 11, 15]


    score = Score(course, [chinese, english, math, natural, society])
    print(score.df)
    print("##################################################")


    score.add_total()
    print(score.df)
    print("##################################################")


    score.add_average()
    print(score.df)
    print("##################################################")


    score.remove_average()
    print(score.df)
    print("##################################################")


    score.sort_by_total()
    print(score.df)
    print("##################################################")

    score.add_rank()
    print(score.df)


if __name__ == "__main__":
    main()