# Robot Name

Write a program that manages robot factory settings.

When robots come off the factory floor, they have no name.

The first time you boot them up, a random name is generated, such as
RX837 or BC811.

Every once in a while we need to reset a robot to its factory settings,
which means that their name gets wiped. The next time you ask, it will
respond with a new name.

Random names means a risk of collisions. In some exercism language
tracks there are tests to ensure that the same name is never used twice.

## Making the Test Suite Pass

1. Get [PHPUnit].

        % wget --no-check-certificate https://phar.phpunit.de/phpunit.phar
        % chmod +x phpunit.phar

2. Execute the tests for an assignment.

        % phpunit.phar wordy/wordy_test.php

[PHPUnit]: http://phpunit.de


## Source

A debugging session with Paul Blackwell at gSchool. [view source](http://gschool.it)