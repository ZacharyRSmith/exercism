import java.time.DayOfWeek;
import java.time.LocalDate;
//import MeetupSchedule;

public class Meetup {
  private final int month;
  private final int year;
  Meetup(int month, int year) {
    this.month = month;
    this.year = year;
  }

  LocalDate day(DayOfWeek dow, MeetupSchedule sched) {
    LocalDate ld = LocalDate.of(
        year,
        month,
        (MeetupSchedule.TEENTH == sched) ? 13 : 1
    );
    ld = ld.with(dow);
    int add_weeks = (ld.getMonthValue() != month) ? 1 : 0;
    switch (sched) {
      case FIRST:                  break;
      case SECOND: add_weeks += 1; break;
      case THIRD:  add_weeks += 2; break;
      case FOURTH: add_weeks += 3; break;
      case LAST:   add_weeks += 4; break;
      case TEENTH:
          add_weeks = (ld.getDayOfMonth() < 13) ? 1 : 0;
          break;
    }
    ld = ld.plusWeeks(add_weeks);
    while (ld.getMonthValue() != month) {
      ld = ld.minusWeeks(1);
    }
    return ld;
  }
}

// import org.joda.time.DateTime;

// /**
//  * Calculates the date of meetups.
//  */
// public class Meetup {

//   static int month;

//   static int year;

//   Meetup(int month, int year) {
//     this.month = month;
//     this.year = year;
//   }

//   /**
//    * @param dayOfWeek: Weekday on which the meetup meets.
//    * @param weekOfMonth: When in the month the meetup meets.
//    * @return Date of a meetup provided meetup's day of week and week of month.
//    */
//   public final DateTime day(int dayOfWeek, MeetupSchedule weekOfMonth) {
//     return new DateTime(2013, 5, 13, 0, 0);
//   }
// }
