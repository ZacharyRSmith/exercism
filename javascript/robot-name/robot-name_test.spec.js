var Robot = require('./robot-name');

describe("Robot", function() {
  it("has a name", function() {
    var robot = new Robot();
    expect(robot.name).toMatch(/^[A-Z]{2}\d{3}$/);
  });

  it("name is the same each time", function() {
    var robot = new Robot();
    expect(robot.name).toEqual(robot.name);
  });

    it("different robots have different names", function() {
      var usedNames= {};

      var i = 0,
          max = 10000;

      for (i; i < max; i++) {
        var newRobot = new Robot();
        usedNames[newRobot.name] = true;
      }

      expect(Object.keys(usedNames).length).toEqual(10000);
    });

  it("is able to reset the name", function() {
    var robot = new Robot();
    var originalName = robot.name;
    robot.reset();
    var newName = robot.name;
    expect(newName).toMatch(/^[A-Z]{2}\d{3}$/);
    expect(originalName).not.toEqual(newName);
  });

  it("should set a unique name after reset", function() {
    var usedNames= {};
    var robot = new Robot();
    usedNames[robot.name] = true;

    var i = 0,
        max = 10000;

    for (i; i < max; i++) {
      robot.reset();
      usedNames[robot.name] = true;
    }

    expect(Object.keys(usedNames).length).toEqual(10001);
  });
});
