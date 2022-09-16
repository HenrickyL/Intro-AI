using System;

public class Environment{
    public bool IsDirtyA { get; set; }
    public bool IsDirtyB { get; set; }
    public bool AgentLocation { get; set; }
    private bool autoDirty;
    private Random random = new Random();
    public Agent? Agent { get; set; }
    public Environment(bool dirtyA, bool dirtyB, bool agentLoc, bool autoDirty = false)
    {
        this.IsDirtyA = dirtyA;
        this.IsDirtyB = dirtyB;
        this.AgentLocation = agentLoc;
        this.autoDirty = autoDirty;
        Console.Clear();
        Console.WriteLine("Initial State");
        ShowState();
    }
    private void ShowState(){
        var res = "---------\n";
        // res+="\nDados do Ambiente:";
        // res+="\n\tisDirtyA: "+ this.IsDirtyA;
        // res+="\n\tisDirtyB: "+ this.IsDirtyB;
        // res+="\n\tagentLocation: " + this.AgentLocation;
        res+="|   |   |\n";

        if(AgentLocation)
            res+="| @ |   |\n";
        else
            res+="|   | @ |\n";
        res+= "|"+(IsDirtyA?"...":"   ")+"|"+(IsDirtyB?"...":"   ")+"|\n";
        res+="---------";
        Console.WriteLine(res);
        Console.ReadKey();
        Console.Clear();
    }
    public void Update() {
        if(Agent != null){
            var perception = Agent.Perceives(AgentLocation, AgentLocation? IsDirtyA: IsDirtyB);
            var action = Agent.Act(perception);
            switch (action.Name)
            {
                case ActionEnum.aspire:
                    if(AgentLocation){
                        IsDirtyA = false;
                    }else{
                        IsDirtyB = false;
                    }
                    Console.WriteLine(">>>Agent clear room "+(AgentLocation?"A":"B"));
                    break;
                case ActionEnum.toLeft:
                    if(AgentLocation){
                        Console.WriteLine("I can't go left");
                    }else{
                        Console.WriteLine(">>>Agent go to room A");
                        AgentLocation = true;
                        if(autoDirty){
                            IsDirtyB = random.Next(2) == 1;
                            if(IsDirtyB)
                                Console.WriteLine("<<< room A got dirty!");
                        }
                    }
                    break;
                case ActionEnum.toRight:
                    if(AgentLocation){
                        Console.WriteLine(">>>Agent go to room B");
                        AgentLocation = false;
                        if(autoDirty){
                            IsDirtyA = random.Next(2) == 1;
                            if(IsDirtyA)
                                Console.WriteLine("<<< room B got dirty!");
                        }
                    }else{
                        Console.WriteLine("I can't go right");
                    }
                    break;
                default:
                    Console.WriteLine("Action invalid");
                    break;
            }
        }else{
            Console.WriteLine("no agent in the room");
        }
        ShowState();
    }
}