# print everything between *** START and *** END
pbpaste | sed '/\*\*\* START.*/q' | wc -l | bc | (read start; pbpaste | sed -e 1,"$start"d) | pbpaste | sed '/\*\*\* END.*/q' | sed -e '$d'
