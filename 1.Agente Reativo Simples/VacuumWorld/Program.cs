
class Program{
    public static void Main(){
        Console.Clear();
        Console.WriteLine("Room A dirty?");
        var isDirtA = Int32.Parse(Console.ReadLine())>0;
        Console.WriteLine("Room B dirty?");
        var isDirtB = Int32.Parse(Console.ReadLine())>0;
        Console.WriteLine("Agent in room A?");
        var agentLoc = Int32.Parse(Console.ReadLine())>0;
        Console.WriteLine("Iterations?");
        var n = Int32.Parse(Console.ReadLine());

        var environment = new Environment(isDirtA, isDirtB,agentLoc, true);
        var agent = new Agent();
        environment.Agent = agent;
        while(n>0){
            environment.Update();
            n--;
        }
        
    }
}