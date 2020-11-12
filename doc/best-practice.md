best practice.

An example of how you can add a new vocables.

Add date from now:

.1 :myNewVocables 
.1 [kbd]F12[/kbd] you see that it not already exist
.1 [kbd]F7[/kbd] thats for add new vovable.
    .1 field 1: datum
    .1 field 3: 
    
FormatTime, timestampyyMMddHHmmss , %A_now%,dd.MM.YYYY
clipboard := timestampyyMMddHHmmss
