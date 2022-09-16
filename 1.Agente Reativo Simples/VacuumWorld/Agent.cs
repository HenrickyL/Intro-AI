public class Agent{
    public Perception Perceives(bool location,bool isDirt)
    {
        return new Perception(location, isDirt);
    }

    public Action Act(Perception perception)
    {
        if(perception.IsDirty)
            return new Action(ActionEnum.aspire);
        else if(perception.Location)
            return new Action(ActionEnum.toRight);
        else
            return new Action(ActionEnum.toLeft);
    }
}