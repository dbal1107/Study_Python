# flowchart : https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# ascii art : https://ascii.co.uk/art

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
input('')
print("""
               ,-=-.
              /     )
             (  c/=(
              `-( _/
              _/ (_
            /  `-- )
          <  ,   ) )>
        /  \/ \   (/\\
      / ,'    )    \ \\
  -=` /      /     |  \\
   \-`      /      |  '\|
           <_./    |
          /        |
         /   ,     |
        <,_./      |
       /           |
      /_           |
     |  ``--.__.-='!
     | /         \ !
'`'"' ("" '`'`"' `) \_'"'`"" "``''"''`" "'"`'''
    (_ \_        '"`=-'`"               `" "
  '"" `-'`"            '"'`'
         '`'"'                     '""`'"
""")
load = input('You run and find load. Where you go? : "Left" or "Right" >>> ').lower()
print()

if load == 'left' :
    choose = input('You can choose about "Swim" or "Wait" >>> ').lower()
    print()
    if choose == 'wait' :
        door = input('Door is appear! What color\'s door open? : "Red" / "Blue" / "Yellow" >>> ').lower()
        print()
        if door == 'yellow' : 
            print('You win!!!!\n')
        elif door == 'red' :
            print('You burned by fire....')
            print('Game Over\n')
        elif door == 'blue' :
            print('You eaten by beasts....')
            print('Game Over\n')
        else:
            print('Game Over\n')
    else :
        print('''
                         ___
               /`  _\\
               |  / 0|--.
          -   / \_|0`/ /.`'._/)
      - ~ -^_| /-_~ ^- ~_` - -~ _
      -  ~  -| |   - ~ -  ~  -
     jgs     \ \, ~   -   ~
              \_|
        ''')
        input('')
        print('You attacked by trout....')
        print('Game Over\n')
else : 
    print('You fall into a hole....')
    print('Game Over\n')
