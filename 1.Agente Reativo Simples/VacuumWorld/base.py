from random import randint

'''
    Classe referente ao ambiente no qual o agente estará inserido
'''
class Environment:
    def __init__(self, isDirtyA, isDirtyB, agentLocation):
        self.isDirtyA = isDirtyA;
        self.isDirtyB = isDirtyB;
        self.agentLocation = agentLocation;
        
    def update(self, action_name):
        print("\nAção:");
        if(action_name == "Aspirar"):
            if(self.agentLocation):
                self.isDirtyA = False;
                print("    O agente limpou a sala A");
            else:
                self.isDirtyB = False;
                print("    O agente limpou a sala B");
        elif(action_name == "Direita"):
            if(self.agentLocation):
                self.agentLocation = False;
                self.isDirtyA = bool(randint(0, 1));
            print("    O agente foi para a sala B");
        elif(action_name == "Esquerda"):
            if(not(self.agentLocation)):
                self.agentLocation = True;
                self.isDirtyB = bool(randint(0, 1));
            print("    O agente foi para a sala A");
        else:
            print("O agente não foi programado para esta percepção");
        
    def print_dados(self):
        print("\nDados do Ambiente:");
        print("    isDirtyA: ", self.isDirtyA);
        print("    isDirtyB: ", self.isDirtyB);
        print("    agentLocation: ", self.agentLocation);

'''
    Classe referente a percepção que será capturada pelo agente
'''
class Perception:
    def __init__(self, location, isDirty):
        self.location = location;
        self.isDirty = isDirty;

'''
    Classe referente a ação que será realizada pelo agente
'''
class Action:
    def __init__(self, name):
        self.name = name;  

'''
    Classe referente ao agente
'''
class Agent:
    def perceives(self, environment):
        if(environment.agentLocation):
            return Perception(environment.agentLocation, environment.isDirtyA);
        else:
            return Perception(environment.agentLocation, environment.isDirtyB);
        
    def act(self, perception):
        if(perception.isDirty):
            return Action("Aspirar");
        elif(perception.location):
            return Action("Direita");
        else:
            return Action("Esquerda");
        
'''
    Classe referente as configurações de ambiente, agente e número de passos do mesmo
'''
class VacuumWorld:
    isDirtyA = bool(input("A sala A está suja ? "));
    isDirtyB = bool(input("A sala B está suja ? "));
    agentLocation = bool(input("Agent na sala A(True) ou B(False) ? "));
    n = int(input("Número de passos: "));
    
    environment = Environment(isDirtyA, isDirtyB, agentLocation);
    environment.print_dados();
    
    agent = Agent();
    isDirty = True;
    
    while(n > 0):  
        perception = agent.perceives(environment);
        action = agent.act(perception);
        
        environment.update(action.name);
        
        environment.print_dados();
         
        n -= 1; 
