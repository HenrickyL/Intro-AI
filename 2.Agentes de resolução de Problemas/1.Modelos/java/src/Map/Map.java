package Map;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
public class Map {
    public List<State> states;
    public Map(){
        this.states = new ArrayList<State>();
    }
    public void show() {
        for (State state : states) {
            System.out.println(state.show());
        }
    }
    public static Map readData(String filename){
        try{
            File file = new File(filename);
            Scanner read = new Scanner(file);
            var map = new Map();
            while(read.hasNextLine()){
                var line = read.nextLine().split(":");
                var city = line[0].strip();
                var transitions = new ArrayList<Transition>();
                if(line.length >1){
                    var targets = line[1].strip().split(",");
                    if(targets.length >0){
                        for (var t : targets) {
                            var x = t.split("-");
                            transitions.add(new Transition(x[0],x[1]));
                        }
                    }
                }
                map.states.add(new State(city,transitions));
            }
            read.close();
            return map;
        }catch(FileNotFoundException e){
            e.printStackTrace();
            return null;
        }
    }
}
