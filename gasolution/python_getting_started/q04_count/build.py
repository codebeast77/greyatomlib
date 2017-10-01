import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

def deliveries_count(data):

    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'RT Ponting':
                count += 1

    return count