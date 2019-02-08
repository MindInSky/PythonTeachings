from datetime import datetime

today = datetime.today().day

if today == 'Saturday':
    print('PArty!')
elif today == 'Sunday':
    print('Moar pari!')
else:
    print('Work,work,work')
