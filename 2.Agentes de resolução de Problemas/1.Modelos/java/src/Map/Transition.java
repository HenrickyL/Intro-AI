package Map;

public class Transition {
    public String target;
    public String cost;

    public Transition(String target, String cost){
        this.target = target;
        this.cost = cost;
    }

    public String show(){
        String s = String.format("\tname: %s - cost: %s\n", this.target, this.cost);
        return s;
    }
}
