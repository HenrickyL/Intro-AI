public enum ActionEnum{
    aspire, toRight, toLeft
}

public class Action{
    public ActionEnum Name { get; set; }

    public Action(ActionEnum name){
        this.Name = name;
    }
}