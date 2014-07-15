__author__ = 'LiuyinC'

## Read the first N lines from output.txt and write them into problem_1_submission.txt

N = 5000
input_file = open("output.txt", 'r')
output_file = open('problem_1_submission.txt', 'w')
for i in range(N):
    line = input_file.next().strip()
    output_file.write(line + '\n')

input_file.close()
output_file.close()
