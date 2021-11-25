class Student():
    def __init__(self, firstName, middleName, lastName, scores):
        self.firstName     = firstName
        self.middleName    = middleName
        self.lastName      = lastName
        self.scores        = scores

    def __str__(self):
        scores = []
        scoresString = ''

        for score in self.scores:
            scores.append('Term number: ' + str(score) + ' -> Average score:' + str(self.scores[score]))
            
        for score in scores:
            scoresString = scoresString + score + '\n'
        return 'Full name: ' +  self.firstName + ' ' + self.middleName + ' ' + self.lastName + '\n' + scoresString

    def __setitem__(self, term, score):
        """ set score of specefic student term """
        self.scores[term] = score

    def __getitem__(self, term): 
        """ return score of specefic student term """
        return self.scores[term]

    def __len__(self):
        """ return count of student term """
        return len(self.scores)


firstName = 'John'
middleName = 'Packard'
lastName = 'fabian'
scores = {1:12.45, 2:13, 3:14.60} 
s1 = Student(firstName, middleName, lastName, scores)

print(s1)

s1[1] = 15

print(s1)

print(s1[2])

print(len(s1))