import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

def BC_runs(data):

    runs = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'BB McCullum':
                runs += delivery_info['runs']['batsman']

    return(runs)