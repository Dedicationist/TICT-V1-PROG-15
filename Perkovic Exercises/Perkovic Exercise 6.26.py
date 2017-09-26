def week():
    weekdays= {'Mo':'Monday','Tu':'Tuesday','Th':'Thursday','Fr':'Friday','Sa':'Saturday','Su':'Sunday'}
    while True:
        dag = input('Enter a day abbreviation: ')
        print('{} stands for {}'.format(dag, weekdays[dag]))
week()
