SET
search_path TO 'frag';

SET
jit TO off;

WITH activity AS (SELECT b1.student,
                         b1.points / 100 AS b1_activity,
                         b2.points / 100 AS b2_activity,
                         b3.points / 100 AS b3_activity
                  FROM ptsum_activity_1 AS b1
                           JOIN ptsum_activity_2 AS b2 ON b1.student = b2.student
                           JOIN ptsum_activity_3 AS b3 ON b1.student = b3.student),

     presence AS (SELECT b1.student,
                         b1.points / 100 AS b1_presence,
                         b2.points / 100 AS b2_presence,
                         b3.points / 100 AS b3_presence
                  FROM ptsum_presence_1 AS b1
                           JOIN ptsum_presence_2 AS b2 ON b1.student = b2.student
                           JOIN ptsum_presence_3 AS b3 ON b1.student = b3.student),

     review AS (SELECT b1.student,
                       b2.points / 100 AS b2_review,
                       b3.points / 100 AS b3_review,
                       b4.points / 100 AS b4_review
                FROM ptsum_review_1 AS b1
                         JOIN ptsum_review_2 AS b2 ON b1.student = b2.student
                         JOIN ptsum_review_3 AS b3 ON b1.student = b3.student
                         JOIN ptsum_review_4 AS b4 ON b1.student = b4.student),

     practice AS (SELECT b1.student,
                         b1.points / 100 AS b1_practice,
                         b2.points / 100 AS b2_practice,
                         b3.points / 100 AS b3_practice
                  FROM ptsum_practice_1 AS b1
                           JOIN ptsum_practice_2 AS b2 ON b1.student = b2.student
                           JOIN ptsum_practice_3 AS b3 ON b1.student = b3.student),

     set AS (SELECT b1.student,
                    b1.points / 100 AS b1_set,
                    b2.points / 100 AS b2_set,
                    b3.points / 100 AS b3_set
             FROM ptsum_set_1 AS b1
                      JOIN ptsum_set_2 AS b2 ON b1.student = b2.student
                      JOIN ptsum_set_3 AS b3 ON b1.student = b3.student),

     exam AS (SELECT student,
                     points / 100 AS b4_exam
              FROM ptsum_exam)

SELECT practice.b1_practice,
       presence.b1_presence,
       activity.b1_activity,
       set.b1_set,

       practice.b2_practice,
       presence.b2_presence,
       activity.b2_activity,
       set.b2_set,
       review.b2_review,

       practice.b3_practice,
       presence.b3_presence,
       activity.b3_activity,
       set.b3_set,
       review.b3_review,

       review.b4_review,
       exam.b4_exam

FROM activity
         JOIN presence ON activity.student = presence.student
         JOIN review ON activity.student = review.student
         JOIN practice ON activity.student = practice.student
         JOIN set ON activity.student = set.student
         JOIN exam ON activity.student = exam.student;
