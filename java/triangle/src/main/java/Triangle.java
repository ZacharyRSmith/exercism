/**
 * Tells type of triangle.
 */
public class Triangle {
  private double x, y, z;
  private TriangleKind kind;

  Triangle(double x, double y, double z) throws TriangleException {
    this.x = x;
    this.y = y;
    this.z = z;
    if (isInvalidTriangle()) throw new TriangleException();
    setKind(x, y, z);
  }

  public TriangleKind getKind() {
    return this.kind;
  }

  private boolean isInvalidTriangle() {
    boolean sideMissing = x <= 0 || y <= 0 || z <= 0;
    // The following line validates the triangle inequality theorem: z ≤ x + y
    // where x,y, and z are the lengths of the sides of a triangle. In other words, the
    // sum of the lengths of any two sides of a triangle always exceeds or is equal to
    // the length of the third side.
    boolean violatesTriangleTheorem = x > y + z || y > x + z || z > x + y;
    return sideMissing || violatesTriangleTheorem;
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
