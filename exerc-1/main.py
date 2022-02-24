class Language:

    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level

    def get_name(self) -> str:
        return self.name

    def get_language(self) -> int:
        return self.level
    
    
class Role:
    def __init__(self, language: str, level: int) -> None:
        self.language = language
        self.level = level

    def get_name(self) -> str:
        return self.name

    def get_level(self) -> int:
        return self.level

    
class Project:

    def __init__(self, name: str, duration: int, score: int, bestBefore: int, roles: list[Role] ) -> None:
        self.name = name
        self.duration = duration
        self.score = score
        self.bestBefore = bestBefore
        self.roles = roles

    
    def get_name(self) -> str:
        return self.name

    def get_duration(self) -> int:
        return self.duration

    def get_score(self) -> int:
        return self.score
        
    def get_bestBefore(self) -> int:
        return self.bestBefore

    def get_roles(self) -> list[Role]:
        return self.roles


class Employee:

    def __init__(self, name: str, langs: list[Language]) -> None:
        self.name = name
        self.lang = langs
        self.busy = list() #list of tuples of times when busy
        
    def get_name(self) -> str:
        return self.name

    def get_lang(self) -> list[Language]:
        return self.lang

    def is_free(self, proj: Project) -> bool:
        bb = proj.get_bestBefore()
        last_begin = bb - proj.get_duration()

        for b in self.busy:
            if b[0] <= last_begin and b[1] >= last_begin:
                return False
            if b[0] <= bb and b[1] >= bb:
                return False
            if last_begin <= b[0] <= bb and last_begin <= b[1] <= bb:
                return False
        return True

        
    

def read_input(file: str) -> list[list[str]]:
    output = []
    with open(file) as f:
        for line in f:
            output.append(line.split())
    return output


def build(build: list[list[str]]):
    
    people = []
    projects = []

    l = build.pop()  # This part holds the initial info for loops
    n_people = int(l[0])
    n_projects = int(l[1])
    
    while n_people > 0:
        
        l = build.pop()
        name = l[0]

        langs = []
        for _ in range(int(l[1])):  # Iterates over each employee's language
            l = build.pop()
            langs.append(Language(l[0], l[1]))
        people.append(Employee(name, langs))
        
        n_people -= 1
        
    while n_projects > 0:
        
        l = build.pop()
        
        roles = []
        for _ in range(int(l[4])):
            d = build.pop()
            roles.append(Role(d[0], d[1]))
        p = Project(l[0], int(l[1]), int(l[2]), int(l[3]), roles)
        
        projects.append(p)
        n_projects -= 1
        
    def sorting(e: Project):
        return e.bestBefore
    projects.sort(key=sorting)
            
    return (people, projects)


def assigner(p, almost, can_do):
    
    
    
    


def scheduler(employees, projects):
    # assuming projects are already sorted by growing end date

    for p in projects:
        almost = list()
        can_do = list()
        for e in employees:
            if not e.is_free(p):
                continue
            if e.can_do(p):
                can_do.append(e)
            elif e.can_almost_do(p):
                almost.append(p)
        assigner(p, almost, can_do)
    return


def write_output(submission):
    outF = open("submission.txt", mode="w")

    for project in submission:
        #write project name
        outF.write(project[0])
        outF.write("\n")

        #write people's name
        for i in project[1]:
            outF.write(i)
            outF.write(" ")

        outF.write("\n")  
        
    outF.close()


if __name__ == '__main__':    
    out = read_input("tests/a_an_example.in.txt")
    
    e, p = build(out)

    submission = [["ana", ["ana", "bob"]]]

    write_output(submission)
    
