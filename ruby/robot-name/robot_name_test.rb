#!/usr/bin/env ruby
gem 'minitest', '>= 5.0.0'
require 'minitest/autorun'
require_relative 'robot_name'

class RobotTest < Minitest::Test
  COMMAND_QUERY = <<-MSG
    Command/Query Separation:
    Query methods should generally not change object state.
  MSG

  NAME_REGEXP = /^[A-Z]{2}\d{3}$/

  def test_has_name
    assert_match NAME_REGEXP, Robot.new.name
  end

  def test_name_sticks
    robot = Robot.new
    robot.name
    assert_equal robot.name, robot.name
  end

  def test_different_robots_have_different_names
    refute_equal Robot.new.name, Robot.new.name
  end

  def test_different_robots_have_different_names_better_test
    used_names = { }

    for i in 1..10000 do
      name = Robot.new.name

      refute used_names[name]

      used_names[name] = true
    end
  end

  def test_creation_of_name_with_zero_padded_digits
    found_zero_padded = false

    for i in 1..10000 do
      name = Robot.new.name

      if name[2] == '0'
        found_zero_padded = true
      end
    end

    assert found_zero_padded
  end

  def test_creation_of_name_with_repeated_letters
    found_repeated_letters = false

    for i in 1..10000 do
      name = Robot.new.name

      if name[0..1] == 'AA'
        found_repeated_letters = true
      end
    end

    assert found_repeated_letters
  end

  def test_reset_name
    robot = Robot.new
    name = robot.name
    robot.reset
    name2 = robot.name
    assert name != name2
    assert_equal name2, robot.name, COMMAND_QUERY
    assert_match NAME_REGEXP, name2
  end
end
