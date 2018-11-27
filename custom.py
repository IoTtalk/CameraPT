import DAN

ServerIP = '140.113.199.249'   #=None:AutoSearch, or ='IP':Connect to this IP
Comm_interval = 0.5 # unit:second

def profile_init():
    DAN.profile['dm_name']='CameraPT'
    DAN.profile['d_name']=DAN.profile['dm_name']+'.'+DAN.get_mac_addr()[-4:]

def odf():  # int only
    return [
        ('Up', 0, 'Up'),
        ('Down', 0, 'Down'),
        ('Left', 0, 'Left'),
        ('Right', 0, 'Right'),
    ]

def idf():
    return [
     #  ('PIN1', float),
     #  ('PIN2', int),
     #  ('PIN3', str),
    ]
