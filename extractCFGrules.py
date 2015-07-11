# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:10:03 2015

@author: nausheenfatma
"""

from Stack import Stack

class ExtractCFG :
    def __init__(self):
        self.production_rules={}
        self.train_file_path="data/English_Parsed_Train.txt"
        self.output_file_path="output/CFGrules.txt"
        self.non_terminal_file_path="output/non_terminals.txt"
    
    def find_rules(self):
        inputfile=open(self.train_file_path,"r")
        outputfile=open(self.output_file_path,"w")
        non_terminal_file_path=open(self.non_terminal_file_path,"w")
        t=[]
        for sentence in inputfile :
            stack=Stack()
            tokens=sentence.split()
            for token in tokens:
                #print "token",token
                if not token == ')':
                    stack.push(token)         # push tokens in stack
                else :       
                        # time to find rules
                    rule_stack=Stack()
                    while stack.peek()!='(' : # while beginning bracket is not encountered
                        popped=stack.pop()
                        rule_stack.push(popped)
                    stack.pop()               # pop the left bracket (
                    lhs=rule_stack.pop()
                   # print "lhs",lhs
                    outputfile.write(lhs)
                    outputfile.write("->")
                    if lhs not in t:
                        t.append(lhs)
                        non_terminal_file_path.write(lhs)
                        non_terminal_file_path.write(" ")
                    stack.push(lhs)  #push back the lhs to the stack
                    while not rule_stack.isEmpty():
                        pop_item=rule_stack.pop()
                        #print "pop_item",pop_item
                        outputfile.write(pop_item)
                        outputfile.write(" ")
                    outputfile.write("\n")
        outputfile.close()
        inputfile.close()
def main():
    ex=ExtractCFG()
    ex.find_rules()


if __name__=="__main__" : main()
    
