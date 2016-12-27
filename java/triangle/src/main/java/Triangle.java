/**
 * Tells type of triangle.
 */
public class Triangle {
  private TriangleKind kind;

  Triangle(double x, double y, double z) throws TriangleException {
    if (!isValidInput(x, y, z)) throw new TriangleException();
    setKind(x, y, z);
  }

  public TriangleKind getKind() {
    return this.kind;
  }

  private boolean isValidInput(double x, double y, double z) {
    if (x <= 0 || y <= 0 || z <= 0) return false;
    // The following line validates the triangle inequality theorem: z ≤ x + y
    // where x,y, and z are the lengths of the sides of a triangle. In other words, the
    // sum of the lengths of any two sides of a triangle always exceeds or is equal to
    // the length of the third side.
    if (x > y + z || y > x + z || z > x + y) return false;
    return true;
  }

  private void setKind(double x, double y, double z) {
    if (x == y && y == z) {
      this.kind = TriangleKind.EQUILATERAL;
    } else if (x == y || y == z || x == z) {
      this.kind = TriangleKind.ISOSCELES;
    } else {
      this.kind = TriangleKind.SCALENE;
    }
  }
}
