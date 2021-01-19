import itertools as it
import os
from sys import argv 

def relation(A, B) -> str:
    if all(a > b for a, b in zip(A, B)):
        return ">"
    elif all(a < b for a, b in zip(A, B)):
        return "<"
    return "#"

def file_to_dict(file_name: str) -> {str: [int]}:
    scorecard = {}
    if not os.path.exists(file_name):
        print(f"file {file_name} not found")
        exit(1)
    for line in open(file_name):
        marks = line.strip().split()
        scorecard[marks[0]] = [int(score) for score in marks[1:]]
    return scorecard

def relation_pairs(scorecard: {str: [int]}) -> {str} :
    rels = set()
    for key1, key2 in it.combinations(scorecard.keys(), 2):
        rel = relation(scorecard[key1], scorecard[key2])
        if rel == ">":
            rels.add(key1 + key2)
        elif rel == "<":
            rels.add(key2 + key1)
    return rels

def rules_and_removables(relations: {str}) -> {str} :
    first = set([x[0] for x in relations])
    second = set([x[1] for x in relations])
    both = first & second
    removables = set()
    for a_student, b_student in it.product(first, second):
        if a_student + b_student in relations:
            for student in both:
                if a_student + student in relations and student + b_student in relations:
                    removables.add(a_student + b_student)
    return removables

rels = relation_pairs(file_to_dict('data.txt'))
removables = rules_and_removables(rels)
minimal = sorted(set(rels) ^ removables)

print("ALL relations\n", rels)
print("Removables\n", removables)
print("Minimal\n", minimal)

with open("vanchi.dot", "w") as f:
    print("digraph vanchi {", file=f)
    for relation in minimal:
        print("\t%s -> %s;" %(relation[0], relation[1]), file=f)
    print("}", file=f)

os.system("dot -Tpng vanchi.dot > vanchi.png")
