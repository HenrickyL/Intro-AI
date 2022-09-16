public class Perception{
    public bool Location { get; set; }
    public bool IsDirty { get; set; }

    public Perception(bool location, bool isDirt){
        this.IsDirty = isDirt;
        this.Location = location;
    }
}