import org.junit.Ignore;
import org.junit.Test;

import static org.junit.Assert.*;

public class BobTest {
    private final Bob bob = new Bob();

    @Test
    // @Ignore
    public void saySomething() {
        assertEquals(
            "Whatever.",
            bob.hey("Tom-ay-to, tom-aaaah-to.")
        );
    }

    @Test
    // @Ignore
    public void shouting() {
        assertEquals(
            "Whoa, chill out!",
            bob.hey("WATCH OUT!")
        );
    }

    @Test
    // @Ignore
    public void askingAQuestion() {
        assertEquals(
            "Sure.",
            bob.hey("Does this cryogenic chamber make me look fat?")
        );
    }

    @Test
    // @Ignore
    public void askingANumericQuestion() {
        assertEquals(
            "Sure.",
            bob.hey("You are, what, like 15?")
        );
    }

    @Test
    // @Ignore
    public void talkingForcefully() {
        assertEquals(
            "Whatever.",
            bob.hey("Let's go make out behind the gym!")
        );
    }

    @Test
    // @Ignore
    public void usingAcronymsInRegularSpeech() {
        assertEquals(
            "Whatever.", bob.hey("It's OK if you don't want to go to the DMV.")
        );
    }

    @Test
    // @Ignore
    public void forcefulQuestions() {
        assertEquals(
            "Whoa, chill out!", bob.hey("WHAT THE HELL WERE YOU THINKING?")
        );
    }

    @Test
    // @Ignore
    public void shoutingNumbers() {
        assertEquals(
            "Whoa, chill out!", bob.hey("1, 2, 3 GO!")
        );
    }

    @Test
    // @Ignore
    public void onlyNumbers() {
        assertEquals(
            "Whatever.", bob.hey("1, 2, 3")
        );
    }

    @Test
    // @Ignore
    public void questionWithOnlyNumbers() {
        assertEquals(
            "Sure.", bob.hey("4?")
        );
    }

    @Test
    // @Ignore
    public void shoutingWithSpecialCharacters() {
        assertEquals(
            "Whoa, chill out!", bob.hey("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!")
        );
    }

    @Test
    // @Ignore
    public void shoutingWithUmlauts() {
        assertEquals(
            "Whoa, chill out!", bob.hey("\u00dcML\u00c4\u00dcTS!")
        );
    }

    @Test
    // @Ignore
    public void calmlySpeakingWithUmlauts() {
        assertEquals(
            "Whatever.", bob.hey("\u00dcML\u00e4\u00dcTS!")
        );
    }

    @Test
    // @Ignore
    public void shoutingWithNoExclamationMark() {
        assertEquals(
            "Whoa, chill out!", bob.hey("I HATE YOU")
        );
    }

    @Test
    // @Ignore
    public void statementContainingQuestionMark() {
        assertEquals(
            "Whatever.", bob.hey("Ending with ? means a question.")
        );
    }

    @Test
    // @Ignore
    public void prattlingOn() {
        assertEquals(
            "Sure.", bob.hey("Wait! Hang on. Are you going to be OK?")
        );
    }

    @Test
    // @Ignore
    public void silence() {
        assertEquals(
            "Fine. Be that way!", bob.hey("")
        );
    }

    @Test
    // @Ignore
    public void prolongedSilence() {
        assertEquals(
            "Fine. Be that way!", bob.hey("    ")
        );
    }
}
