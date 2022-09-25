import Map.Map;
public class App {
    public static void main(String[] args) throws Exception {
        var map = Map.readData("data.txt");
        map.show();
    }
}
