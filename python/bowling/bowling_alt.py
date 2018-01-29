sum(frame.score(self) for frame in frames)


class BowlingGame(object):
    def __init__(self):
        pass
        # [Frame]

    def get_throws_after_frame(self, frameID):
        throws = []
        next_frame = self.get_frame_after_frame(frameID)
        throws.append(next_frame.throws)
        if len(next_frame.throws) == 0:
            # We've reached the end of this BowlingGame.
            return throws
        elif len(throws) == 1:  # Strikes need the next 2 throws, so get more.
            next_next_frame = self.get_throws_after_frame(next_frame.id)
            throws.append(next_next_frame.throws)
        return throws


Frame:
    isStrike
    isSpare
    score(self, game)
        game.get_throws_after_frame(self)
    [Throw]


class Frame(object):
    """Frame"""
    def __init__(self):
        self.first_throw_pins = 0
        self.is_strike = False
        self.is_spare = False
        self.second_throw_pins = 0
        self.throws_done = 0
        self.score = 0

    @property
    def is_done(self):
        return self.throws_done == 2 or self.first_throw_pins == 10

    def notify(self, notif):
        if self.is_spare:
            self.score += notif.first_throw_pins
        elif self.is_strike:
            self.score += notif.first_throw_pins + notif.second_throw_pins

    def roll(self, pins):
        self.throws_done += 1
        self.score += pins
        if self.throws_done == 1:
            self.first_throw_pins = pins
            if self.score == 10:
                self.is_strike = True
        else:
            self.second_throw_pins = pins
            if self.score == 10:
                self.is_spare = True
        return self


class BowlingGame(object):
    def __init__(self):
        self.frames = [Frame() for i in range(10)]
        self.frame_num = 0

    def get_frame(self, frame_num):
        if 0 <= frame_num <= 9:
            return self.frames[frame_num]
        else:
            return Frame() # Enhance return Null type

    def roll(self, pins):
        crnt_frame = self.get_frame(self.frame_num)
        crnt_frame.roll(pins)
        if (crnt_frame.is_done):
            last_frame = self.get_frame(self.frame_num - 1)
            notifRes = last_frame.notify(crnt_frame)
            # next_to_last_frame = self.get_frame(self.frame_num - 2)
            # next_to_last_frame.notify(notifRes)
            self.frame_num += 1

    def score(self):
        for frame in self.frames:
            print(frame.score)
        return sum(frame.score for frame in self.frames)
