exception=['hotmail.com', 'HOTMAIL.COM', 'Hotmail.com', 'HOTMAIL.com', 'HoTMaiL.CoM', 'HotMail.com', 'hotmail.COM', 'hotmail.Com', 'HOtmail.com', 'hoTmail.com', 'HOTmAIL.COM', 'HoTmAiL.CoM', 'hotmail.cOm', 'HOTmail.com', 'HoTMAIL.COM', 'hotmAIL.COM', 'HotMail.Com', 'HOTMail.com', 'hOtmail.com']
with open('combo.txt') as combo, open('combonew.txt', 'w') as new:
    for line in combo:
        for i in exception:
            if i in line:
                new.write(line)