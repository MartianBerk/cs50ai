from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
# ----
# A is a Knave
knowledge0 = And(
    # These first two conditions encode XOR: Or + Not(And)
    # A cannot be both a Knight & a Knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # This condition encodes the sentence: A is a Knight & a Knave
    # We consider the implication from both sides.
    # We know the Knave lies so we Not his consequent.
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
# ----
# A is a Knave
# B is a Knight
knowledge1 = And(
    # A cannot be both a Knight & a Knave
    # Neither can B
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # This condition encodes the sentence: 
    # A says "We are both Knaves."
    # We consider the implication from both sides,
    # where Knight is True (truth) and Knave is False (lie).
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# ----
# A is a Knave
# B is a Knight
knowledge2 = And(
    # A cannot be both a Knight & a Knave
    # Neither can B
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # These two conditions encodes the sentence:
    # A says "We are the same kind" by taking as truth
    # for the Knight and a lie for the Knave.
    Implication(AKnight, And(AKnight, BKnight)),
    Implication(AKnave, Not(And(AKnave, BKnave))),

    # As above, these two encodes the sentence:
    # B says "We are of different kinds"
    Implication(BKnight, And(BKnight, AKnave)),
    Implication(BKnave, Not(And(BKnave, AKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# ----
# A is a Knight
# B is a Knave
# C is a Knight
knowledge3 = And(
    # A cannot be both a Knight & a Knave
    # Neither can B or C
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # These conditions encode the first sentence:
    # A says either "I am a Knight" or "I am a Knave"
    Implication(AKnight, AKnight),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(AKnave, Not(AKnave)),

    # These encode the sentence:
    # B says "A said 'I am a Knave'."
    Implication(BKnight, AKnave),
    Implication(BKnave, Not(AKnave)),

    # These encode the sentence:
    # B says "C is a Knave"
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # And lastly, these encode the sentence:
    # C says "A is a Knight"
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
