package Map;

import java.util.ArrayList;
import java.util.List;

public class State {
    public String name;
    public List<Transition> edges;
    public State father;
    public State(String name, List<Transition> edges){
        this.name = name;
        this.edges = edges;
    }
    public State(){
        this.name = "";
        this.edges = new ArrayList<Transition>();
    }

    public String show(){
        var s = String.format("%s:\n", this.name);
        for (Transition transition : edges) {
            s+=transition.show();
        }
        return s;
    }
}
