Set up a basic latest Django installation

 Extend the User model to have

a birthday field of type date

a random number field of type integer that is assigned a value from 1-100 on creation

 Create views for: list of all users, viewing, adding, editing and deleting a single user

 Create two template tags:

a tag that will display "allowed" if the user is > 13 years old otherwise display "blocked"

a tag that will display the BizzFuzz result of the random number that was generated for the user. The BizzFuzz specification is that for multiples of three print "Bizz" instead of the number and for the multiples of five print "Fuzz". For numbers which are multiples of both three and five print "BizzFuzz"

add a column to the list view after the birthday column 

add a column to the list view after the random number column that uses the BizzFuzz tag

 Unit tests

 Optional task: Create a download link on the list view. The link would return the list of results in Excel's format