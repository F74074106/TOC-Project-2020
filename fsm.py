from transitions.extensions import GraphMachine

from utils import send_text_message

import random


class TocMachine(GraphMachine):

    

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "start" 

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    


    def on_exit_user(self,event):
        global answer_1
        global answer_2
        global answer_3
        global answer_4
        
        global index
        global ans
       
        x = ['0','1','2','3','4','5','6','7','8','9']
        ans = ['12','13','14','15']
        

        index = random.randint(0,9)

        answer_1 = x[index]
        x[index] = '11'
        
        while x[index]=='11':
            index = random.randint(0,9)

        answer_2 = x[index]
        x[index] = '11'

        while x[index]=='11':
            index = random.randint(0,9)

        answer_3 = x[index]
        x[index] = '11'

        while x[index]=='11':
            index = random.randint(0,9)

        answer_4 = x[index]
        x[index] = '11'
      
        ans[0] = answer_1
        ans[1] = answer_2
        ans[2] = answer_3
        ans[3] = answer_4

        print(ans)
      
    def on_enter_state1(self, event):
        print("I'm entering state1")

        
        
        reply_token = event.reply_token
        send_text_message(reply_token, "please enter 4 digit number")



        guess_num = event.message.text
        
        
        
  
        
        #self.guess()
        
        
        
        


    def on_exit_state1(self,event):
        print("Leaving state1")


    def on_enter_state2(self,event):

        print("I'm entering state2")
        reply_token = event.reply_token
      
      
        global guess_num


        guess_num=event.message.text

        print(guess_num)


        if (guess_num >= "0" and guess_num <= "9999"):
            
            self.gogo(event)
        else:
            send_text_message(reply_token, "please enter 4 digit number")
            self.back(event)


    def on_exit_state2(self,event):
        print("Leaving state2")

    def on_enter_state3(self,event):


        global a
        global b

        a = 0
        b = 0

        reply_token = event.reply_token
        
        for i in range(4):
            if guess_num[i] == ans[i]:
                a = a + 1
        

        for i in range(4):
            for j in range(4):
                if ans[i] == guess_num[j]:
                    b = b + 1
                    
        b = b -a

        if a == 4:
            send_text_message(reply_token, "win")
            self.back(event)
            
        else :
            #send_text_message(reply_token,"hi")
            send_text_message(reply_token,"%dA%dB"%(a,b))
            self.backback(event)