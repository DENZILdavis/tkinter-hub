# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:25:15 2020

@author: denzil davis
"""


class learnersMentors():
  stack=[]
  def addStacks(self):

    stack=[]

  def setMentorOrLearner(self,stack):
    choice=input("are you a learner?then enter y\n else enter n")
    if(choice=='y' or choice=='Y'):
      stack.append("learner")
    else:
      stack.append("mentor")
      def setAvailableTime(self,stack):
        time=int(input("enter your availablr time\nenter statrting time"))


        stack.append(time)
      def getMentor(self,stack,time):
        for i in stack:
          if (i==time):
            print(i)



obj=learnersMentors()
obj.addStacks()
obj.setMentorOrLearner()
try:
  obj.setAvailableTIme()
  print("u r a mentor")
except:
  print("u r a learner")
obj.getMentor()
