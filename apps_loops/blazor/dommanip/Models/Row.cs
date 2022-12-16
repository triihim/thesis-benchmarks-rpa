namespace Models;

public record Row {
  public Row(int rowId, int value)
  {
    this.RowId = rowId;
    this.Value = value;
  }
  public int RowId;
  public int Value;
}