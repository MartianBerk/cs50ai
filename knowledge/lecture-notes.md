# Knowledge - Lecture 2

Knowledge Based Agents - agents that reason by operating on internal representations of knowledge.

If it didn't rain, Harry visited Hagrid today.
<br />
Harry vistied Hagrid or Dumbledore today, but not both.
<br />
Harry visited Dumbledore today.

With these three statements, we as humans can start reasoning other information. For example:

Harry did not visit Hagrid today.
<br />
It rained today.

How can we make our AI intelligent enough to make similar reasoning?
<br />
We need to be a little more formal.

### Terms
- <b>Sentence</b> - As assertion about the world in a knowledge representation language.
- <b>Propositional Logic</b> - Based on statements about the world.
- <b>Propositional Symbols</b> - P, Q, R. These represent some sentence or fact.
- <b>Logical Connectives</b> - not, and, or, implication & biconditional. These are the 5 main ones that underpin propositional logic.
- <b>Not</b> - Reverses the statement of the proposition.
- <b>And</b> - Combines two propositions, both must be true.
- <b>Or</b> - Combines two propositions, either must be true. This would be inclusive OR (either or both is true). There is also the notion of exclusive or where by both true would be false.
- <b>Implication</b> - P implies Q means if P is true and Q is true then is implies true. Similarly if both are false this implies true. But if P is false, it makes no implication whatsoever so implies will always be true. The only way implication is false is if P is true but Q is false.
- <b>Biconditional</b> - Condition that goes in both directions. If and only if. Only true when P and Q are the same. 
- <b>Model</b> - A model assigns a truth value to every propsitional symbol. So take two propositions, P and Q. The model will assign truth values to them. You could conceive the numbers of models is equal to the number of possible outcomes. Number of models (outcomes) is equal to 2^n where n is the number of propositions.
- <b>Knowledge Base</b> - A set of sentences known by a knowledge based agent. A set of things the AI knows about the world. We might tell the AI this information to store in its knowledge base and will use it to draw conclusions about the rest of the world.
- <b>Entailment</b> - A entails B. In every model where A is true then B is also true. If I know alpha to be true, then beta must also be true. Its this idea of entailment we want to encode into a computer. Coming back to the Harry Potter example above, the computer can infer the same information from the three statements that we can using entailment.
- <b>Inference</b> - The process of deriving new sentences from old ones.

### Inference Example
Define the propositions.
<br />
P: It is Tuesday.
<br />
Q: It is raining.
<br />
R: Harry will go for a run.

Knowledge Base (KB): 
<br />
P and not Q implies R.
<br />
(P and !Q) -> R
<br />
If it is Tuesday and it is not raining then Harry will go for a run.

P = True & Q = False

Using this information we can draw some inferences. We know the whole expression to be True so the implication is that R is True = Harry will go for a run.
<br />
Inference = R

Using only information inside the knowledge base, does KB entail alpha? Can we do this algorithmically.

<b>Model Checking</b>
<br />
One algorithm to do this. To determine if KB entails alpha, we will enumerate all possible models. If in every model, in every combination of worlds (models), where KB is True and Query is True, the KB entails Query. 

Is it guaranteed Harry will go for a run? 
<br />
Query = R.
<br />
We have 8 possible models. 3 propositions = 2^3 = 8.

|   P   |   Q   |   R   |   KB  |
| ----- | ----- | ----- | ----- |
| false | false | false | false |
| false | false | true  | false |
| false | true  | false | false |
| false | true  | true  | false |
| true  | false | false | false |
| true  | false | true  | true  |
| true  | true  | false | false |
| true  | true  | true  | false |

<b>Knowledge Engineering</B>
<br />
Take a problem and break it down into Symbols, propositions that a computer can then solve inferences.

### Cluedo

Propositional Symbols - each of the possible things in the envelope.

Initial information.
We know that someone in the murderer? OR
<br />
We know that one of the rooms was used? OR
<br />
We know that one of the weapons was used? OR

As the game goes on, you unlock additional information. Could introduce NOT along the way to remove options.

<b>Algorithm</b>
<br />
Check knowledge takes knowledge and tries to draw conclusions using model_check. If it knows something to be true, print YES in Green, otherwise it will check for NOT symbol. If unsure on this assertion, then Maybe it's true.

Knowledge = AND(OR(characters), OR(rooms), OR(weapons))  # Initial knowledge

If you run the knowledge check at this stage, all MAYBES

As you provide information, the AI will conclude inferences. So, you draw three cards that tell you in the envelope it cannot be three of the things. You can add them to the knowledge and now check_knowledge will eliminate some options.

Someone makes a guess and it's wrong, we know that one of those three things was wrong at minimum. OR(NOT(x), NOT(y), NOT(z)). This won't elimiate any options yet. But next someone shows you the Plum card so you know Plum is not in the envelope. Now we have a character.

Now let's add it's not the Ballroom, someone added it, should be able to conclude it's the library but you can also conclude the weapon. This was an inference by checking all the models. It came from the OR clause above, combined with the other certainties it could figure it out.

All this can be tightly aligned to logic puzzles.

### Inference Rules

Model checking is not efficient, we are enumerating all the options really. 2^n. As soon as we get larger sets of data, it won't work, or at least not well.

--------

<b>Modus Ponens</b>
```
If it is raining, then Harry is inside.
It is raining.
-----------------
Harry is inside.
```

If we know that alpha implies beta and alpha is true, then beta must be true. This is an inference rule, that beta is true if alpa is true and alpha implies beta.

```
a -> B
a
------
B
```

<b>And Elimination</b>
```
Harry is friends with Ron and Hermione.
-----------------
Harry is friends with Hermione.
```

If an AND proposition is true, then any one atomic proposistion within it is true as well.

```
a ^ B
-----
a
````

<b>Double negation Elimination</b>

```
It is not true that Harry did not pass the test.
-------------------------
Harry passed the test.
```

A proposition that is negated twice is true.

```
!(!(a))
-------
a
```

<b>Implication Elimination</b>

```
If it is raining, then Harry is inside.
-------------------------
It is not raining or Harry is inside.
```

An implication is equivalent to an Or relation between the negated antecedent (left most proposition) and the consequent (right most).

```
a -> B
--------
!(a) v B
```

Since <b>P -> Q</b> and <b>!P v Q</b> have the same truth value assignment, we know them to be equivalent logically. Remember, if the antecedent (P) is false the implication is true always. Or, if the antecedent is true and and the consequent is true then the implication is true.

```
P        = false
Q        = false
P -> Q   = true
!P v Q   = true

P        = false
Q        = true
P -> Q   = true
!P v Q   = true

P        = true
Q        = false
P -> Q   = false
!P v Q   = false

P        = true
Q        = true
P -> Q   = true
!P v Q   = true
```

<b>Biconditional Elimination</b>

```
It is raining if and only if Harry is inside.
---------------------------------------------
If it is raining, then Harry is inside and if Harry is inside then it is raining.
```

A Biconditional proposition is equivalent to an implication and its inverse with an And connective.

```
a <-> B
-------------------
(a -> B) ^ (B -> a)
```

<b>De Morgan's Law</b>

```
It is not true that both Harry and Ron passed the test.
---------------------------------------------
Harry did not pass the test or Ron did not pass the test.
```

It is possible to turn an And connective into an Or connective by moving the Not around.

```
!(a ^ B)
-----------
!(a) v !(B)
```

Similarly it's possible to conclude the inverse, turn an Or connective into an And connective.

```
It is not true that Harry or Ron passed the test.
-----
Harry did not pass the test and Ron did not pass the test.
```
```
!(a v B)
-----------
!(a) ^ !(B)
```

<b>Distributive Property</b>

```
(a ^ (B v C))
-----------------
(a ^ B) v (a ^ C)
```
```
(a v (B ^ C))
-----------------
(a v B) ^ (a v C)
```

A proposition with two or more elements that are grouped with And or Or connectives can be distributed (broken down) into smaller units consisting of And and Or.

<b>Knowledge and Search Problems</b>
<br />
There is a link here from Inference Rules to how we solved Search problems. 

- We can treat sentences as states.
- The initial state is the starting knowledge base.
- Actions are the inference rules.
- Transition model is the new knowledge base after inference.
- Goal test is the check statement we're trying to prove.
- Path cost function is the number of steps in proof.

Shows how versatile search problems can be, allowing us to derive new information based on existing knowledge using inference rules.

<b>Resolution</b>
<br />
One of the more common ways to solve a proof with a knowledge base. It's a powerful inference rule that states that if one of two atomic propositions in an Or proposition is false, the other has to be true.

```
Ron is in the Great Hall or Herminone is in the library.
Ron is not in the Great Hall.
------------------------------
Hermione is in the library
```

The two statements conflict with each other.

```
P v Q
!(P)
-----
Q
```

Resolution relies on complementary literals, two of the same atomic propsition where is negated and the other is not. Such as P and !P.

Resolution can be further generalized. Suppose we add another proposition.

```
Ron is in the Great Hall or Herminone is in the library.
Ron is not in the Great Hall or Harry is sleeping.
--------------------------------------
Hermione is in the library or Harry is sleeping.
```

```
P v Q
!(P) v R
--------
Q v R
```

Remember, P and Q can be multiple OR symbols.
Can always resolve the two rules together.

Complementary literals allow us to generate new sentences through inference by resolution. Thus, inference algorithms locate complementary literals to generate new knowledge.

A <b>clause</b> is a disjunction of literals (a proposition symbol or negation of a proposition symbol, such as P or !P). A <b>disjunction</b> consists of propositions that are connected with an Or logical connective (P v Q v R). A <b>conjunction</b> consits of propositions that are connected with an And logical connective. Clauses allow us to convert any logical statement into a <b>Conjunctive Normal Form (CNF)</b>, which is a conjunction of clauses. For example: (A v B v C) ^ (D v !E) ^ (F v G).

<b>Conjunctive Normal Form</b>
<br />
Logical sentence that is a conjunction of clauses. Every clause is held in parentheses. These clauses are joined with AND. Within the clause, the propositions are joined by OR. We can take any number of sentences and turn it into conjunctive normal form using a logical formula.

Conversion to CNF
We take all the symbols that are not part of CNF, such as biconditionals, and translate them.

Steps:
- Eliminate Biconditionals:
    <br />
    Turn (a <-> B) into (a -> B) AND (B -> a)

- Eliminate Implicatations:
    <br />
    Turn (a -> B) into !(a) OR B

- Move negation inwards until only literals are being negated (and not clauses) using De Morgan's law.
    <br />
    Turn !(a AND B) into !(A) OR !(B)

- Use distributive law to distribute OR wherever possible.
    <br />
    Turn (!P ^ !Q) v R into (!P v R) ^ (!Q v R)

Example converting (P v Q) -> R to Conjuntive Normal Form.

- (P v Q) -> R
- !(P v Q) v R # Eliminate implication
- (!P ^ !Q) v R # De Morgan's Law
- (!P v R) ^ (!Q v R) # Distributive Law

<b>Inference By Resolution</b>
<br />
Taking the above example, at this point, we can run an inference algorithm on the conjunctive normal form. Occasionally, through the process of inference by resolution, we might end up in cases where a clause contains the same literal twice. In these cases, a process called <b>factoring</b> is used, where the duplicate literal is removed. For example, (P ∨ Q ∨ S) ∧ (!P ∨ R ∨ S) allow us to infer by resolution that (Q ∨ S ∨ R ∨ S). The duplicate S can be removed to give us (Q ∨ R ∨ S).impossible for P and !(P) to hold at the same time. This in fact is the basis for inference by resolution algortihtm.

Resolving a literal and its negation, i.e. !P and P, gives the <b>empty clause ()</b>. The empty clause is always false, and this makes sense because it is impossible that both P and ¬P are true. This fact is used by the resolution algorithm.

To deteremine if KB entails a:
<br />
    - Check if (KB ^ !(a)) is a contradiction? If we assume something is False and prove it's true, then it must be true.
<br />
    - Then KB entails a. Otherwise no entailment.

<b>Proof By Contradiction</b>
<br />
Proof by contradiction is a tool used often in computer science. If our knowledge base is true, and it contradicts ¬α, it means that ¬α is false, and, therefore, α must be true. More technically, the algorithm would perform the following actions:

- Convert (KB ^ !(a)) to CNF.
- Keep checking to see if we can use resolution to produce a new clause.
- If we ever produce the empty caluse (equivalent to False) we have a contradiction and KB enatils a.
- Otherwise if contradiction is not achieved and no more clauses can be inferred, there is no entailment.

<b>For Example:</b>
<br />
- Does (A v B) ^ (!(B) v C) ^ (!(C)) entail A? This is our KB.

- First, to prove by contradiction, we assume A is false:
<br /> 
(A v B) ^ (!(B) v C) ^ (!(C)) ^ (!(A))
- This is in CNF, there are 4 different clauses:
    1. (A v B)
    2. (!(B) v C)
    3. (!(C))
    4. (!(A))
- Now we can start generating new information: since we know C is false, the only way (!(B) v C) can be true is if B is false too. So, we can add (!B) to the knowledge base.
<br />
(A v B) ^ (!(A)) ^ (!B)
- Next, since we know (!B), the only way (A v B) can be true is if A is true, so we can add (A) to the knowledge base.
<br />
(!(A)) ^ (A)
- Now our KB has two complementary literals, (A) and (!A). We resolve them arriving at the empty set. The empty set is false by definition, so we have arrived as a contradiction and the statement originally is true.
<br />
()

We don't need to model check all worlds. Instead, we use the resolution algorithm to see if we reach a contradiction. There are many different algortihms that can be used for this. All based on propositional logic. It's not the only logic that exists and there are some limitations to it.


### First Order Logic

First order logic is another type of logic that allows us to express more complex ideas more succinctly than propositional logic. First order logic uses two types of symbols: Constant Symbols and Predicate Symbols. Constant symbols represent objects, while predicate symbols are like relations or functions that take an argument and return a true or false value.

For example, we return to the logic puzzle with different people and house assignments at Hogwarts. The constant symbols are people or houses, like Minerva, Pomona, Gryffindor, Hufflepuff, etc. The predicate symbols are properties that hold true or false of some constant symbols. For example, we can express the idea that Minerva is a person using the sentence Person(Minerva). Similarly, we can express the idea the Gryffindor is a house using the sentence House(Gryffindor). All the logical connectives work in first order logic the same way as before. For example, ¬House(Minerva) expresses the idea that Minerva is not a house. A predicate symbol can also take two or more arguments and express a relation between them. For example, BelongsTo expresses a relation between two arguments, the person and the house to which the person belongs. Thus, the idea that Minerva belongs to Gryffindor can be expressed as BelongsTo(Minerva, Gryffindor). First order logic allows having one symbol for each person and one symbol for each house. This is more succinct than propositional logic, where each person—house assignment would require a different symbol.

<b>Universal Quantification</b>
<br />
Quantification is a tool that can be used in first order logic to represent sentences without using a specific constant symbol. Universal quantification uses the symbol ∀ to express “for all.” So, for example, the sentence ∀x. BelongsTo(x, Gryffindor) → ¬BelongsTo(x, Hufflepuff) expresses the idea that it is true for every symbol that if this symbol belongs to Gryffindor, it does not belong to Hufflepuff.

<b>Existential Quantification</b>
<br />
Existential quantification is an idea parallel to universal quantification. However, while universal quantification was used to create sentences that are true for all x, existential quantification is used to create sentences that are true for at least one x. It is expressed using the symbol ∃. For example, the sentence ∃x. House(x) ∧ BelongsTo(Minerva, x) means that there is at least one symbol that is both a house and that Minerva belongs to it. In other words, this expresses the idea that Minerva belongs to a house.

Existential and universal quantification can be used in the same sentence. For example, the sentence ∀x. Person(x) → (∃y. House(y) ∧ BelongsTo(x, y)) expresses the idea that if x is a person, then there is at least one house, y, to which this person belongs. In other words, this sentence means that every person belongs to a house.

There are other types of logic as well, and the commonality between them is that they all exist in pursuit of representing information. These are the systems we use to represent knowledge in our AI.