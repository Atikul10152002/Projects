
// Synthetic Division
Clr List 1
"How Many Nums" ? -> U
For 1 -> X To U
"X" ? -> List 1[X]
Next
"Factorial" ? -> F
List 1[1] -> L #RUN
For 2 -> X To Dim List 1
List 1[X] -> 0
If (L*F) + O = 0
Then 0 -> L #RUN
"No Remainder!"
Else ((L*F)+O) -> L #RUN
IfEnd
Next

