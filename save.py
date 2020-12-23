'''file for enabling saving to file option'''
#user_id -- name/number of the user
#max_length -- the maximum length of sequence that user repeated without any mistakes
#seq1time -- time spent by user on the first sequence
#seq2time -- time spent by user on the second sequence
#seq3time -- time spent by user on the third sequence
#seq4time -- time spent by user on the fourth sequence
#final_score -- final score of the user
def filelog(user_id, max_length, seq1time, seq2time, seq3time, seq4time, final_score):
    '''saves user data into a file'''
    filename = "results_user_" + str(user_id) + ".txt"
    f = open(filename, "x")
    f.write("user ID is " + str(user_id) + "\n")
    f.write("maximum length is " + str(max_length) + "\n")
    f.write("sequence 1 time is " + str(round(seq1time, 2)) + "\n")
    f.write("sequence 2 time is " + str(round(seq2time, 2)) + "\n")
    f.write("sequence 3 time is " + str(round(seq3time, 2)) + "\n")
    f.write("sequence 4 time is " + str(round(seq4time, 2)) + "\n")
    f.write("final score is " + str(final_score) + "\n")
    f.close()

def main ():
    ''''main function for testing purposes'''
    max_length = 5
    seq1time = 2.45
    seq2time = 5.32
    seq3time = 3.42
    seq4time = 35
    finalscore = 69
    user_id = 5
    filelog(user_id, max_length, seq1time, seq2time, seq3time, seq4time, finalscore)

#actual testing
if __name__ == '__main__':
    main()
