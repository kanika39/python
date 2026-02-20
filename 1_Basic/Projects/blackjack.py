import random
class card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):#called when print is invoked on an obj
        return f"{self.rank['rank']} of {self.suit}"

class deck:
    def __init__(self):#self is not a keyword but is written for instance to access class
        self.cards=[]
        suits=['hearts','spades','clubs','diamonds']
        ranks=[
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank":"10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit,rank))# this line is adding each card object into cards list
    def shuffle(self):
        if len(self.cards)>1:
             random.shuffle(self.cards)

    def deal(self, num):
        cards_dealt=[]
        for x in range(num): 
            if len(self.cards)>0:
                cards_dealt.append(self.cards.pop())
        return cards_dealt

class hand:
    def __init__(self , dealer = False):
        self.cards=[]
        self.value=0
        self.dealer=dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)
    
    def calculate_value(self):
        self.value=0
        has_ace=False

        for card in self.cards:
            card_value =int(card.rank["value"])
            self.value+=card_value
            if card.rank["rank"]== 'A':
                has_ace = True

        if has_ace and self.value>21:
            self.value-=10
    
    def get_value(self):
        self.calculate_value() # we are calling calculate_value function only with the instance
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self,show_all_dealers_card=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealers_card and not self.is_blackjack():
                print('hidden')
            else:
                print(card)
        
        if not self.dealer: 
            print("value: ",self.get_value())
        print()

class game:
    def play(self):
        game_number=0
        games_to_play=0
        
        while games_to_play<=0:
            try:
                games_to_play=int(input("How many games do you want to play? "))
            
            except:
                print("You must enter a number")
        
        while games_to_play > game_number:
            game_number+=1
            
            d=deck()
            d.shuffle()

            player_hand=hand()
            dealer_hand=hand(dealer=True)

            for i in range(2):
                player_hand.add_card(d.deal(1))
                dealer_hand.add_card(d.deal(1))

            print()
            print('*'*30)
            print(f"Game {game_number} of {games_to_play}")
            print('*'*30)

            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand,dealer_hand):
                continue

            choice=""
            while player_hand.get_value() < 21 and choice not in ['s',"stand"]:
                choice=input("Please choose 'hit' or 'Stand': ").lower()
                print()
                while choice not in ['h','s','hit','stand']:
                    choice=input("Please enter 'hit' or 'Stand' (or H/S)").lower()
                    print()
                if choice in ["h","hit"]:
                    player_hand.add_card(d.deal(1))
                    player_hand.display()
            
            if self.check_winner(player_hand,dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(d.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealers_card=True)

            if self.check_winner(player_hand,dealer_hand):
                continue

            print("Final result")
            print("your hand: " , player_hand_value)
            print("Dealer's hand: " , dealer_hand_value)

            self.check_winner(player_hand,dealer_hand,True)

        print("\nThank's for playing")

    def check_winner(self,player_hand,dealer_hand,game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("you busted dealer wins! 😂")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted you win! 🥳")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack() :
                print("It's a tie! both have blackjack 😏")
                return True
            elif player_hand.is_blackjack() :
                print("It's a blackjack! you win 🥳")
                return True
            elif dealer_hand.is_blackjack() :
                print("It's a blackjack! Dealer win 😭")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("you win! 🥳")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("tie! 🥳")
            else:
                print("dealer won")
            return True
        return False
        
g=game()
g.play()
