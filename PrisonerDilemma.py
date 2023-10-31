#importing random directory to compute random strategy of the players
import random

#import matplotlib to plot graph to monitor the activity of the players
import matplotlib.pyplot as plt

#import numpy to include numeric calculations
import numpy as np

#defining a class Player
class Player:
   
    #initializing required variables
    def __init__(self, name, strategy,sType):
        self.name = name
        self.strategy = strategy
        self.years = 0 #no.of years going to serve in the prison
        self.decision_history = []
        self.sType = sType

    #describes the action of the player
    def player_action(self, opponent):
        #s stores the value of the decision of the players
        s = self.strategy.action(self, opponent)
       
        #printing the decision and name of the player along with his strategy
        print(f"{s} - sent for {self.name} {self.sType} ")
       
        if(self.sType == "TitForTat Strategy" and opponent.decision_history != []):
            {
                print(f"Opponents({opponent.name}) last decision - {opponent.decision_history[-1]}")
            }
       
        return s

#creating a random class which describes the random strategy of the players
class Random:
    def action(self, player, opponent):
        #returns any random choice between cooperate and betray
        return random.choice(['cooperate', 'betray'])

#TitForTat class is something that returns the same decision as the other player decided
class TitForTat:
    def action(self, player, opponent):
        if  opponent.decision_history == []:
            return 'cooperate'
        else:
            return opponent.decision_history[-1]
       
#this class always return the decision as cooperate
class AlwaysCooperate:
    def action(self, player, opponent):
        return 'cooperate'

#this class always returns the decision as betray
class AlwaysBetray:
    def action(self, player, opponent):
        return 'betray'

#Class alternate returns the alternate of the player's prev decision
class Alternate:
    def __init__(self):
        self.last_action = None

    def action(self, player, opponent):
        if not self.last_action:
            self.last_action = 'betray'
            return self.last_action
        elif self.last_action == 'cooperate':
            self.last_action = 'betray'
            return self.last_action
        else:
            self.last_action = 'cooperate'
            return self.last_action



class PrisonerDilemma:
    def __init__(self, rounds, player1, player2):
        self.rounds = rounds
        self.player1 = player1
        self.player2 = player2
        self.results = []

    def play_game(self):
        for i in range(self.rounds):
            print(f"Round {i+1}")
            p1_decision = self.player1.player_action(self.player2)
            p2_decision = self.player2.player_action(self.player1)
            print("\n")
            years = self.get_years(p1_decision, p2_decision)
            self.player1.years += years[0]
            self.player2.years += years[1]
            print("Prison Time ")
            print(f"Player1 - {years[0]}\t Player2 - {years[1]}\n")
            self.player1.decision_history.append(p1_decision)
            self.player2.decision_history.append(p2_decision)
            self.results.append((p1_decision, p2_decision, years))
           
            input("Press key to continue")
       
        print("\t\t\tTotal Prison Time at the end")
        print(f"\tPlayer1({self.player1.name}) - {self.player1.years}\t\t Player2({self.player1.name}) - {self.player2.years}\n")
       
        input("Press key to continue")
       
        return self.results

    def get_years(self, p1_decision, p2_decision):
        if p1_decision == 'cooperate' and p2_decision == 'cooperate':
            return (1, 1)
        elif p1_decision == 'cooperate' and p2_decision == 'betray':
            return (3, 0)
        elif p1_decision == 'betray' and p2_decision == 'cooperate':
            return (0, 3)
        else:
            return (2, 2)


       
    def print_statistics(self):
        num_cooperate = 0
        num_betray = 0
        num_mutual_cooperate = 0
        num_mutual_betray = 0
        num_p1_betray_p2_cooperate = 0
        num_p1_cooperate_p2_betray = 0

        for result in self.results:
            p1_decision = result[0]
            p2_decision = result[1]

            if p1_decision == 'cooperate' and p2_decision == 'cooperate':
                num_cooperate += 2
                num_mutual_cooperate += 1
            elif p1_decision == 'cooperate' and p2_decision == 'betray':
                num_betray += 1
                num_p1_betray_p2_cooperate += 1
            elif p1_decision == 'betray' and p2_decision == 'cooperate':
                num_betray += 1
                num_p1_cooperate_p2_betray += 1
            else:
                num_mutual_betray += 1
               
           
        print(f"{self.player1.name}'s decision history: {self.player1.decision_history}")
        print(f"{self.player2.name}'s decision history: {self.player2.decision_history}")

        print(f"Number of rounds both players cooperated: {num_mutual_cooperate}")
        print(f"Number of rounds both players betrayed: {num_mutual_betray}")
        print(f"Number of rounds {self.player1.name} cooperated and {self.player2.name} betrayed: {num_p1_cooperate_p2_betray}")
        print(f"Number of rounds {self.player1.name} betrayed and {self.player2.name} cooperated: {num_p1_betray_p2_cooperate}")
        print(f"Number of times {self.player1.name} cooperated: {num_cooperate}")
        print(f"Number of times {self.player1.name} betrayed: {num_betray}")
       
       
        if num_mutual_cooperate !=0 and num_mutual_betray !=0 and  num_mutual_betray !=0 and  num_p1_betray_p2_cooperate !=0:
            y = np.array([num_mutual_cooperate, num_mutual_betray, num_mutual_betray, num_p1_betray_p2_cooperate])
            mylabels = ["Both Cooperated", "Both Betrayed", "Alice cooperated and Bob betrayed", "Alice betrayed and Bob cooperated"]
            myexplode = [0.2, 0, 0, 0]
            mycolors = ["teal", "hotpink", "purple", "tan"]
       
            plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
            plt.show()
           
        elif num_mutual_cooperate !=0 and num_mutual_betray !=0 and  num_mutual_betray ==0 and  num_p1_betray_p2_cooperate ==0:
            y = np.array([num_mutual_cooperate, num_mutual_betray])
            mylabels = ["Both Cooperated", "Both Betrayed"]
            myexplode = [0.2, 0]
            mycolors = [ "purple", "tan"]
       
            plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
            plt.show()
           
        elif num_mutual_cooperate !=0 and num_mutual_betray ==0 and  num_mutual_betray !=0 and  num_p1_betray_p2_cooperate ==0:
            y = np.array([num_mutual_cooperate,num_mutual_betray])
            mylabels = ["Both Cooperated", "Alice cooperated and Bob betrayed"]
            myexplode = [0.2, 0]
            mycolors = ["teal", "purple"]
       
            plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
            plt.show()
           
        elif num_mutual_cooperate !=0 and num_mutual_betray ==0 and  num_mutual_betray ==0 and  num_p1_betray_p2_cooperate !=0:
            y = np.array([num_mutual_cooperate, num_p1_betray_p2_cooperate])
            mylabels = ["Both Cooperated", "Alice betrayed and Bob cooperated"]
            myexplode = [0.2, 0]
            mycolors = ["teal","tan"]
       
            plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
            plt.show()
           
        elif num_mutual_cooperate ==0 and num_mutual_betray !=0 and  num_mutual_betray !=0 and  num_p1_betray_p2_cooperate ==0:
             y = np.array([ num_mutual_betray, num_mutual_betray])
             mylabels = [ "Both Betrayed", "Alice cooperated and Bob betrayed"]
             myexplode = [0.2, 0]
             mycolors = ["teal",  "tan"]
         
             plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
             plt.show()
           
        elif num_mutual_cooperate ==0 and num_mutual_betray !=0 and  num_mutual_betray ==0 and  num_p1_betray_p2_cooperate !=0:
            y = np.array([num_mutual_betray,num_p1_betray_p2_cooperate])
            mylabels = ["Both Betrayed",  "Alice betrayed and Bob cooperated"]
            myexplode = [0.2, 0]
            mycolors = ["teal", "hotpink"]
       
            plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
            plt.show()
           
        elif num_mutual_cooperate ==0 and num_mutual_betray !=0 and  num_mutual_betray !=0 and  num_p1_betray_p2_cooperate !=0:
            y = np.array([num_mutual_betray, num_mutual_betray, num_p1_betray_p2_cooperate])
            mylabels = ["Both Betrayed", "Alice cooperated and Bob betrayed", "Alice betrayed and Bob cooperated"]
            myexplode = [0.2, 0, 0]
            mycolors = ["hotpink", "purple", "tan"]
       
            plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
            plt.show()
           
       
           
        elif num_mutual_cooperate ==0 and num_mutual_betray ==0 and  num_mutual_betray !=0 and  num_p1_betray_p2_cooperate !=0:
            y = np.array([ num_p1_betray_p2_cooperate])
            mylabels = [ "Alice cooperated and Bob betrayed", "Alice betrayed and Bob cooperated"]
            myexplode = [0.2, 0]
            mycolors = ["hotpink",  "tan"]
       
            plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
            plt.show()
           
        elif num_mutual_cooperate !=0 and num_mutual_betray ==0 and  num_mutual_betray !=0 and  num_p1_betray_p2_cooperate !=0:
            y = np.array([num_mutual_cooperate, num_mutual_betray, num_mutual_betray, num_p1_betray_p2_cooperate])
            mylabels = ["Both Cooperated", "Alice cooperated and Bob betrayed", "Alice betrayed and Bob cooperated"]
            myexplode = [0.2, 0, 0.1]
            mycolors = ["teal", "purple", "tan"]
       
            plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
            plt.show()
           
        elif num_mutual_cooperate !=0 and num_mutual_betray !=0 and  num_mutual_betray ==0 and  num_p1_betray_p2_cooperate !=0:
            y = np.array([num_mutual_cooperate, num_mutual_betray, num_p1_betray_p2_cooperate])
            mylabels = ["Both Cooperated", "Both Betrayed",  "Alice betrayed and Bob cooperated"]
            myexplode = [0.2, 0, 0]
            mycolors = ["teal", "hotpink",  "tan"]
       
            plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
            plt.show()
           
        elif num_mutual_cooperate !=0 and num_mutual_betray !=0 and  num_mutual_betray !=0 and  num_p1_betray_p2_cooperate ==0:
             y = np.array([num_mutual_cooperate, num_mutual_betray, num_mutual_betray])
             mylabels = ["Both Cooperated", "Both Betrayed", "Alice cooperated and Bob betrayed"]
             myexplode = [0.2, 0, 0]
             mycolors = ["teal", "hotpink", "purple"]
         
             plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode,startangle=90)
             plt.show()
           
           
        mylabels = ["Both Cooperated", "Both Betrayed", "A cooperated", "A betrayed"]
         
        y = np.array([num_mutual_cooperate, num_mutual_betray, num_mutual_betray, num_p1_betray_p2_cooperate])
       
       
        plt.bar(mylabels,y,width=.2,color = "purple")
        plt.show()

        input("Press enter to continue")


if __name__ == '__main__':
    rounds = int(input("Enter number of rounds to be played : "))
   
    p1 = Player('Alice', Random(),"Random Strategy")
    p2 = Player('Bob', Alternate(),"Alternate Strategy")


   
    game = PrisonerDilemma(rounds, player1=p1, player2=p2)
    results = game.play_game()
    game.print_statistics()
   
    print("\n")


    p1 = Player('Alice', Random(),"Random Strategy")
    p2 = Player('Bob',Random(),"Random Strategy")

    game = PrisonerDilemma(rounds, player1=p1, player2=p2)
    results = game.play_game()
    game.print_statistics()

    print("\n")

    p1 = Player('Alice', TitForTat(),"TitForTat Strategy")
    p2 = Player('Bob', AlwaysBetray(),"AlwaysBetray Strategy")

    game = PrisonerDilemma(rounds, player1=p1, player2=p2)
    results = game.play_game()
    game.print_statistics()
   
    print("\n")

    p1 = Player('Alice', TitForTat(),"TitForTat Strategy")
    p2 = Player('Bob', TitForTat(),"TitForTat Strategy")

    game = PrisonerDilemma(rounds, player1=p1, player2=p2)
    results = game.play_game()
    game.print_statistics()

    print("\n")

    p1 = Player('Alice', AlwaysCooperate(),"AlwaysCooperate Strategy")
    p2 = Player('Bob', AlwaysCooperate(),"AlwaysCooperate Strategy")

    game = PrisonerDilemma(rounds, player1=p1, player2=p2)
    results = game.play_game()
    game.print_statistics()
   
    print("\n")

    p1 = Player('Alice',  AlwaysBetray(),"AlwaysBetray Strategy")
    p2 = Player('Bob', AlwaysBetray(),"AlwaysBetray Strategy")

    game = PrisonerDilemma(rounds, player1=p1, player2=p2)
    results = game.play_game()
    game.print_statistics()
   
    print("\n")

    p1 = Player('Alice', AlwaysCooperate(),"AlwaysCooperate Strategy")
    p2 = Player('Bob', AlwaysBetray(),"AlwaysBetray Strategy")

    game = PrisonerDilemma(rounds, player1=p1, player2=p2)
    results = game.play_game()
    game.print_statistics()