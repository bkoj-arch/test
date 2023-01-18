       IDENTIFICATION DIVISION.
       PROGRAM-ID. OualidPrecision.

       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  DB2-CONNECTION-PARAM.
           05  DB-NAME              PIC X(8).
           05  DB-USER              PIC X(8).
           05  DB-PASSWORD          PIC X(8).

       PROCEDURE DIVISION.
       MAIN-LOGIC.

       MOVE 'DB2'             TO DB-NAME
       MOVE 'Oualid'           TO DB-USER
       MOVE 'Precision'        TO DB-PASSWORD

       CALL "CONNECT" USING DB-NAME, DB-USER, DB-PASSWORD
       .
       .
       .
       CALL "DISCONNECT" USING DB-NAME

