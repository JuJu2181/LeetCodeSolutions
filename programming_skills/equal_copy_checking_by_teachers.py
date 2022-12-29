"""
Say there are 100 students and 15 teachers and paper of each applicant will be checked by 3 random teachers. How can we ensure that each teacher will check uniform or equal number of papers while checking all 100 papers. Explain me how can I solve me this problem. And also solve it using Python Program
"""

import pandas as pd 
import random 

class Solution:
    def getDistributions(self):
        num_students = 100
        num_teachers = 15 
        #List of papers submitted by each student
        papers = list(range(1,num_students+1))
        teacher_paper = {
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[],
            7:[],
            8:[],
            9:[],
            10:[],
            11:[],
            12:[],
            13:[],
            14:[],
            15:[]
        }

        random.shuffle(papers)

        for i,paper in enumerate(papers):
            teacher = (i % num_teachers)+1
            teacher_paper[teacher].append(paper)
        print(teacher_paper)

if __name__ == "__main__":
    s1 = Solution()
    s1.getDistributions()
