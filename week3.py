"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    res = [0,0,0,0,0,0]
    for val in hand:
        if val:
            res[val-1] = res[val-1] + 1
    sumval = res[0]
    for index in range(1,len(res)):
        if res[index]*(index+1)>sumval:
            sumval = res[index]*(index+1)
    return sumval


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcome = []
    sumval = 0
    for index in range(1,num_die_sides+1):
        outcome.append(index)
    sequences = set(gen_all_sequences(outcome,num_free_dice))
    held = held_dice
    for item in sequences:
        held = held + item
        sumval = sumval + score(held)
        held = held_dice
    
    expval = float(sumval)/len(sequences)
    return expval


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    hands = list(hand)
    masks = [list(elem) for elem in gen_all_sequences((0,1),len(hand))]
    final = []
    for idx in range(0,len(masks)):
        temp = []
        for jdx in range(0,len(hand)):
            if(masks[idx][jdx]!=0):
                temp.append(hands[jdx]*masks[idx][jdx])
        final.append(temp)
    result = set([tuple(elem) for elem in final])
    return result


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    hold_list = gen_all_holds(hand)
    maxval = 0.0
    hold = ()
    for item in hold_list:
        if item:
            expval = expected_value(item,num_die_sides,num_die_sides-len(item))
            if maxval>expval:
                maxval = expval
                hold = item
            
    return (maxval, hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
#import user35_uLOFnLQSJV29rFh_5 as expected_value_testsuite
#expected_value_testsuite.run_suite(expected_value)
#import user35_oGFuhcPNLh_0 as score_testsuite
#score_testsuite.run_suite(score)
#import user35_mGREPnDxbs_0 as strategy_testsuite
#strategy_testsuite.run_suite(strategy)