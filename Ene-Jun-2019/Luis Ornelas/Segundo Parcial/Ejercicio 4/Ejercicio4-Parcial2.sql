SELECT Email FROM Users;

SELECT COUNT(Gender) AS Female FROM Users WHERE Gender='F';
SELECT COUNT(Gender) AS Male FROM Users WHERE Gender='M';

SELECT First, Last, Location, Email FROM Users;
