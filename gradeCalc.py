"""Grade Calculation
Riza Marjadi"""

gradeMax = [50, 25, 20, 70, 100]
gradeWeight = [.1, .35, .1, .3, .15]

def finalGrade(homework, project, quiz, exam, final):
    homeworkGr = homework / gradeMax[0] * gradeWeight[0]
    projectGr = project / gradeMax[1] * gradeWeight[1]
    quizGr = quiz / gradeMax[2] * gradeWeight[2]
    examGr = exam / gradeMax[3] * gradeWeight[3]
    finalExamGr = final / gradeMax[4] * gradeWeight[4]
    finalGr = homeworkGr + projectGr + quizGr + examGr + finalExamGr
    print('\n')
    print(' ' * 12 + 'Weights'.rjust(10) + 'Scores'.rjust(9) + 'Max Scores'.rjust(13) + 'Weighted Grades'.rjust(18))
    print('Homework'.ljust(12) + '{0:.2%}'.format(gradeWeight[0]).rjust(10) + str(homework).rjust(9) + str(gradeMax[0]).rjust(13) + '{0:.2%}'.format(homeworkGr).rjust(18))
    print('Projects'.ljust(12) + '{0:.2%}'.format(gradeWeight[1]).rjust(10) + str(project).rjust(9) + str(gradeMax[1]).rjust(13) + '{0:.2%}'.format(projectGr).rjust(18))
    print('Quizzes'.ljust(12) + '{0:.2%}'.format(gradeWeight[2]).rjust(10) + str(quiz).rjust(9) + str(gradeMax[2]).rjust(13) + '{0:.2%}'.format(quizGr).rjust(18))
    print('Exams'.ljust(12) + '{0:.2%}'.format(gradeWeight[3]).rjust(10) + str(exam).rjust(9) + str(gradeMax[3]).rjust(13) + '{0:.2%}'.format(examGr).rjust(18))
    print('Final Exam'.ljust(12) + '{0:.2%}'.format(gradeWeight[4]).rjust(10) + str(final).rjust(9) + str(gradeMax[4]).rjust(13) + '{0:.2%}'.format(finalExamGr).rjust(18))
    print('=' * 62)
    print('Final Grade'.ljust(44) + '{0:.2%}'.format(finalGr).rjust(18))

homework = int(input('Homework scores: '))
project = int(input('Project scores: '))
quiz = int(input('Quiz scores: '))
exam = int(input('Exam scores: '))
final = int(input('Final exam: '))

finalGrade(homework, project, quiz, exam, final)
