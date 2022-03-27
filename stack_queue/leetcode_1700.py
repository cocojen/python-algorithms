from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        myCounter = Counter(students)
        for sandwich in sandwiches:
            if not myCounter[sandwich]:
                break
            else:
                myCounter[sandwich] -= 1
        return myCounter.total()
            